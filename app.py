import os
from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

from forms import RegisterForm, LoginForm, ServiceBookingForm
from models import db, User, ServiceBooking, SparePart, Cart, Wishlist

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoursecretkey'

# Absolute path to database
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'database', 'loyalautomotive.db')

db.init_app(app)

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Role-check decorator
def role_required(*roles):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.role not in roles:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return wrapper

# ---------------------- Routes ----------------------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
            role='customer'
        )
        db.session.add(new_user)
        db.session.commit()
        flash('✅ Account created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            # flash('✅ Logged in successfully.', 'success')  # 🔴 Removed this line as requested
            if user.role == 'admin':
                return redirect(url_for('admin_dashboard'))
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'admin':
        return redirect(url_for('admin_dashboard'))
    return render_template('dashboard.html')

@app.route('/spare-parts')
@login_required
def spare_parts():
    parts = SparePart.query.all()
    return render_template('spare_parts.html', parts=parts)

@app.route('/spare-part/<int:part_id>')
@login_required
def view_spare_part(part_id):
    part = SparePart.query.get_or_404(part_id)
    return render_template('view_spare_part.html', part=part)

@app.route('/book-service', methods=['GET', 'POST'])
@login_required
def book_service():
    form = ServiceBookingForm()
    if form.validate_on_submit():
        booking = ServiceBooking(
            user_id=current_user.id,
            bike_model=form.bike_model.data,
            service_type=form.service_type.data,
            booking_date=form.booking_date.data
        )
        db.session.add(booking)
        db.session.commit()
        flash('✅ Service booked successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('book_service.html', form=form)

# ------------------ Cart ------------------

@app.route('/add-to-cart/<int:part_id>')
@login_required
def add_to_cart(part_id):
    existing = Cart.query.filter_by(user_id=current_user.id, part_id=part_id).first()
    if existing:
        existing.quantity += 1
    else:
        db.session.add(Cart(user_id=current_user.id, part_id=part_id, quantity=1))
    db.session.commit()
    flash('✅ Added to cart.', 'success')
    return redirect(url_for('spare_parts'))

@app.route('/cart')
@login_required
def view_cart():
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    return render_template('cart.html', cart_items=cart_items)

@app.route('/remove-from-cart/<int:cart_id>')
@login_required
def remove_from_cart(cart_id):
    item = Cart.query.get_or_404(cart_id)
    if item.user_id == current_user.id:
        db.session.delete(item)
        db.session.commit()
        flash('🗑️ Removed from cart.', 'info')
    return redirect(url_for('view_cart'))

# ------------------ Wishlist ------------------

@app.route('/add-to-wishlist/<int:part_id>')
@login_required
def add_to_wishlist(part_id):
    existing = Wishlist.query.filter_by(user_id=current_user.id, part_id=part_id).first()
    if not existing:
        db.session.add(Wishlist(user_id=current_user.id, part_id=part_id))
        db.session.commit()
        flash('💖 Added to wishlist.', 'info')
    return redirect(url_for('spare_parts'))

@app.route('/wishlist')
@login_required
def view_wishlist():
    wishlist_items = Wishlist.query.filter_by(user_id=current_user.id).all()
    return render_template('wishlist.html', wishlist_items=wishlist_items)

@app.route('/remove-from-wishlist/<int:wishlist_id>')
@login_required
def remove_from_wishlist(wishlist_id):
    item = Wishlist.query.get_or_404(wishlist_id)
    if item.user_id == current_user.id:
        db.session.delete(item)
        db.session.commit()
        flash('Removed from wishlist.', 'info')
    return redirect(url_for('view_wishlist'))

# ------------------ Admin Routes ------------------

@app.route('/admin/dashboard')
@login_required
@role_required('admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/admin/users')
@login_required
@role_required('admin')
def manage_users():
    users = User.query.all()
    return render_template('admin/manage_users.html', users=users)

@app.route('/admin/bookings')
@login_required
@role_required('admin')
def admin_bookings():
    bookings = ServiceBooking.query.all()
    return render_template('admin/bookings.html', bookings=bookings)

@app.route('/admin/low-stock')
@login_required
@role_required('admin')
def low_stock():
    low_stock_parts = SparePart.query.filter(SparePart.stock < 5).all()
    return render_template('admin/low_stock.html', parts=low_stock_parts)

@app.route('/admin/user/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        user.role = request.form['role']
        db.session.commit()
        flash('✅ User updated successfully.', 'success')
        return redirect(url_for('manage_users'))
    return render_template('admin/edit_user.html', user=user)

@app.route('/admin/user/delete/<int:user_id>')
@login_required
@role_required('admin')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.id != current_user.id:
        db.session.delete(user)
        db.session.commit()
        flash('🗑️ User deleted successfully.', 'info')
    else:
        flash('⚠️ You cannot delete your own account.', 'danger')
    return redirect(url_for('manage_users'))

@app.route('/admin/add-part', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def add_spare_part():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        stock = int(request.form['stock'])

        new_part = SparePart(name=name, description=description, price=price, stock=stock)
        db.session.add(new_part)
        db.session.commit()

        flash('Spare part added successfully!', 'success')
        return redirect(url_for('spare_parts'))

    return render_template('add_part.html')

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.username = request.form['username']
        current_user.email = request.form['email']
        if request.form['password']:
            current_user.password = generate_password_hash(request.form['password'])
        db.session.commit()
        flash('✅ Profile updated successfully.', 'success')
        return redirect(url_for('profile'))
    return render_template('profile.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        if SparePart.query.count() == 0:
            sample_parts = [
                SparePart(name="Oil Filter", description="Protects your engine with clean oil flow.", price=150, stock=18, image_url="/static/images/oil_filter.jpg"),
                SparePart(name="Air Filter", description="Keeps your engine clean and efficient by filtering dust and debris.", price=250, stock=25, image_url="/static/images/air_filter.jpg"),
                SparePart(name="Battery (12V)", description="Maintenance-free long-lasting bike battery.", price=2200, stock=8, image_url="/static/images/battery.jpg"),
                SparePart(name="Chain Sprocket Kit", description="Strong and durable chain kit for long life.", price=1500, stock=12, image_url="/static/images/chain_sprocket_kit.jpg"),
                SparePart(name="Clutch Plate Set", description="OEM quality clutch plates for better control.", price=1200, stock=10, image_url="/static/images/clutch_plate_set.jpg"),
                SparePart(name="Front Mudguard", description="Stylish and protective front mudguard.", price=850, stock=12, image_url="/static/images/front_mudguard.jpg"),
                SparePart(name="Gear Lever", description="Strong gear lever for smooth gear shifting.", price=350, stock=15, image_url="/static/images/gear_lever.jpg"),
                SparePart(name="Handle Grip Set", description="Non-slip grip set for better control.", price=120, stock=35, image_url="/static/images/handle_grip_set.jpg"),
                SparePart(name="Headlight Bulb (Halogen)", description="Bright and reliable halogen bulb for headlight.", price=200, stock=30, image_url="/static/images/headlight_bulb.jpg"),
                SparePart(name="Indicator Light Set", description="Set of 4 bright indicator lights.", price=400, stock=40, image_url="/static/images/indicator_light_set.jpg"),
                SparePart(name="Kick Lever", description="Heavy-duty kick lever for long-lasting performance.", price=250, stock=20, image_url="/static/images/kick_lever.jpg"),
                SparePart(name="Rear Shock Absorber", description="Smooth and durable rear shock absorber.", price=1800, stock=10, image_url="/static/images/rear_shock_absorber.jpg"),
                SparePart(name="Seat Cover", description="Comfortable and water-resistant seat cover.", price=400, stock=20, image_url="/static/images/seat_cover.jpg"),
                SparePart(name="Side Mirror (Pair)", description="High-quality mirrors for clear rear view.", price=300, stock=25, image_url="/static/images/side_mirror.jpg"),
                SparePart(name="Spark Plug", description="Ensure quick ignition with this premium spark plug.", price=180, stock=50, image_url="/static/images/spark_plug.jpg"),
                SparePart(name="Speedometer Cable", description="Flexible and durable speedometer cable.", price=100, stock=30, image_url="/static/images/speedometer_cable.jpg"),
                SparePart(name="Tubeless Tyre (Front)", description="Durable front tubeless tyre for better handling.", price=2300, stock=10, image_url="/static/images/tubeless_tyre_front.jpg"),
                SparePart(name="Tubeless Tyre (Rear)", description="Premium rear tubeless tyre for grip and safety.", price=2500, stock=10, image_url="/static/images/tubeless_tyre_rear.jpg"),
            ]

            db.session.bulk_save_objects(sample_parts)
            db.session.commit()
            print("✅ Sample spare parts inserted.")

    app.run(debug=True)
