# 🚗 Loyal Automotive

**Loyal Automotive** is a web application for managing bike service bookings, spare parts, users, and mechanics. Built using **Flask**, **SQLite**, and **Bootstrap**, this system supports role-based access for Admins, Customers, and Mechanics.

---

## 🛠️ Features

- 🔐 User Registration & Login (Role-based: Admin, Customer, Mechanic)
- 🧾 Book Bike Services
- 🛒 Spare Parts Store (with images, stock, price & description)
- 💖 Wishlist & Cart System
- 📦 Order Management
- ⚙️ Admin Dashboard:
  - Manage Users
  - View Bookings
  - Low Stock Alerts
  - Add Spare Parts
- 👨‍🔧 Mechanic Dashboard (View/Update Assigned Services)
- 👤 User Dashboard & Profile Management
- 💳 **Payment Integration** *(Coming Soon)*

---

## 💻 Tech Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, Bootstrap 5, Jinja2
- **Database**: SQLite
- **Authentication**: Flask-Login

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Anusreemanoj1/loyal-automotive.git
   cd loyal-automotive

python -m venv venv
venv\Scripts\activate   # On Windows

pip install -r requirements.txt

python app.py

Email: admin@example.com
Password: admin123

loyal-automotive/
├── app.py                 # Main Flask application
├── models.py              # SQLAlchemy models
├── forms.py               # Flask-WTF forms
├── requirements.txt       # Python dependencies
├── static/
│   └── images/            # Spare part images
├── templates/             # All HTML templates
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── spare_parts.html
│   └── ...
├── database/
│   └── loyalautomotive.db # SQLite database file
└── README.md

## 📸 Screenshots

### 🏠 Home Page  
![Home Page](https://github.com/Anusreemanoj1/loyal-automotive/blob/main/screenshots/home%20page.png?raw=true)

### 🔐 Login Page  
![Login Page](https://github.com/Anusreemanoj1/loyal-automotive/blob/main/screenshots/login%20page.png?raw=true)

### 🧑 User Dashboard  
![User Dashboard](https://github.com/Anusreemanoj1/loyal-automotive/blob/main/screenshots/user%20page.png?raw=true)

### 🛠️ Admin Dashboard  
![Admin Dashboard](https://github.com/Anusreemanoj1/loyal-automotive/blob/main/screenshots/admin%20dashboard%20page.png?raw=true)

### ➕ Add Spare Parts Page  
![Add Spare Parts](https://github.com/Anusreemanoj1/loyal-automotive/blob/main/screenshots/add%20spare%20parts%20page.png?raw=true)

### 🧰 Spare Parts View Page  
![Spare Parts View](https://github.com/Anusreemanoj1/loyal-automotive/blob/main/screenshots/spare%20parts%20view%20page.png?raw=true)

### 🛒 Cart Page  
![Cart Page](https://github.com/Anusreemanoj1/loyal-automotive/blob/main/screenshots/cart%20page.png?raw=true)

### 💖 Wishlist Page  
![Wishlist Page](https://github.com/Anusreemanoj1/loyal-automotive/blob/main/screenshots/wishlist%20page.png?raw=true)

### 📦 Booking Service Page  
![Booking Service](https://github.com/Anusreemanoj1/loyal-automotive/blob/main/screenshots/booking%20service%20page.png?raw=true)

### 📅 Booking Management Page  
![Booking Page](https://github.com/Anusreemanoj1/loyal-automotive/blob/main/screenshots/booking%20page.png?raw=true)

### ⚠️ Low Stock Page  
![Stock Page](https://github.com/Anusreemanoj1/loyal-automotive/blob/main/screenshots/stock%20page.png?raw=true)

# Navigate to your project folder
cd "C:\Users\anusr\OneDrive\Desktop\loyal automotive"

# Initialize Git and push to your GitHub repository
git init
git add .
git commit -m "Initial commit - Loyal Automotive web app"
git branch -M main
git remote add origin https://github.com/Anusreemanoj1/loyal-automotive.git
git push -u origin main

