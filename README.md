# Loyal Automotive 🚗

An online web application for managing bike service bookings, spare parts, users, and mechanics. Built using **Flask**, **SQLite**, and **Bootstrap**.

## 🛠️ Features

- ✅ User Registration & Login (Role-based access: Admin, Customer, Mechanic)
- 🧾 Book Bike Service
- 🛒 Spare Parts Store (with images, stock, price, and description)
- ❤️ Add to Wishlist / Add to Cart
- 📦 Order Management
- ⚙️ Admin Dashboard to manage:
  - Users
  - Bookings
  - Low Stock Alerts
  - Add Spare Parts
- 👨‍🔧 Mechanic Dashboard (View/Update assigned services)
- 👤 User Dashboard & Profile Management

- 🔒 User Authentication (Login/Register)
- 🛠️ Spare Parts Browsing & Cart System
- 📝 Booking Management
- 💳 Payment Integration *(Planned)*


## 🛠️ Tech Stack

- Python (Flask)
- HTML, CSS, Bootstrap 5
- SQLite (Database)
- Flask-Login (User Authentication)
- Jinja2 (Templating)

## 📦 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/loyal-automotive.git
   cd loyal-automotive

## 📁 Project Structure

loyal-automotive/
│
├── app.py # Main Flask application
├── models.py # Database models
├── forms.py # Flask-WTForms
├── requirements.txt # Python dependencies
├── static/
│ └── images/ # Spare part images
├── templates/
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── spare_parts.html
│ └── ... # All HTML templates
├── database/
│ └── loyalautomotive.db # SQLite database file
└── README.md

shell
Copy
Edit

## 📸 Screenshots

### 🏠 Home Page
![Home Page](screenshots/home%20page.png)

### 🔐 Login Page
![Login Page](screenshots/login%20page.png)

### 🧑 User Dashboard
![User Dashboard](screenshots/user%20page.png)

### 🛠️ Admin Dashboard
![Admin Dashboard](screenshots/admin%20dashboard%20page.png)

### ➕ Add Spare Parts Page
![Add Spare Parts](screenshots/add%20spare%20parts%20page.png)

### 🧰 Spare Parts View Page
![Spare Parts View](screenshots/spare%20parts%20view%20page.png)

### 🛒 Cart Page
![Cart Page](screenshots/cart%20page.png)

### 💖 Wishlist Page
![Wishlist Page](screenshots/wishlist%20page.png)

### 📦 Booking Service Page
![Booking Service](screenshots/booking%20service%20page.png)

### 📅 Booking Management Page
![Booking Page](screenshots/booking%20page.png)

### ⚠️ Low Stock Page
![Stock Page](screenshots/stock%20page.png)


## ▶️ Running the App

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the app
python app.py
Email: admin@example.com
Password: admin123

## ✅ Code Push to GitHub – Step-by-Step

### 🟩 Step 1: Open your terminal in your project folder

```bash
cd "C:\Users\anusr\OneDrive\Desktop\loyal automotive"
git init
git add .
git commit -m "Initial commit - Loyal Automotive web app"
git remote add origin https://github.com/Anusreemanoj1/loyal-automotive.git
git branch -M main
git push -u origin main
