Project Structure
flask-calculator-app/
│
├── app.py
├── templates/
│   ├── login.html
│   ├── register.html
│   └── calculator.html
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md



# 🧮 Flask Calculator App with Login & MySQL

This is a full-stack **Flask-based Calculator App** built using Python, HTML/CSS (Bootstrap), and MySQL. It includes user **registration**, **login**, **logout**, and a clean calculator interface with basic arithmetic operations. All user credentials are securely stored in a MySQL database.

---

## ✅ Features

- 🔐 User Registration & Login
- 🔒 Session-based authentication
- ➗ Calculator with addition, subtraction, multiplication, and division
- 🗄️ MySQL database integration for storing user data
- 🎨 Attractive front-end using HTML, CSS, and Bootstrap
- ⚠️ Flash messages for user feedback
- 🔙 Logout and Back to Home navigation

---

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: MySQL
- **Tools**: Git, GitHub, MySQL Workbench or phpMyAdmin

---

## 📦 Project Setup

### 1. Clone the Repository


git clone https://github.com/your-username/flask-calculator-app.git
cd flask-calculator-app
# Create venv
python -m venv venv

# Activate venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

Install Required Packages
pip install -r requirements.txt

Configure the MySQL Database
CREATE DATABASE calculator_users;
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=calculator_users
SECRET_KEY=your_secret_key_here

Run the Application
python app.py




