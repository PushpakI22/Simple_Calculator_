from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
import config


# In app.py
app = Flask(__name__, static_folder='static')
app.secret_key = 'your_secret_key'

# --- MySQL Configuration ---
db_config = {
    'host': config.host,
    'user': config.user,
    'password': config.password,
    'database': config.database
}

# --- Routes ---

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (uname, pwd))
            conn.commit()
            flash('Registration successful! Please login.')
            return redirect(url_for('login'))
        except mysql.connector.IntegrityError:
            flash('Username already exists.')
        finally:
            cursor.close()
            conn.close()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (uname, pwd))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            session['user'] = uname
            return redirect(url_for('calculator'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if 'user' not in session:
        return redirect(url_for('login'))

    result = None
    if request.method == 'POST':
        try:
            n1 = float(request.form['num1'])
            n2 = float(request.form['num2'])
            op = request.form['operation']

            if op == 'add':
                result = n1 + n2
            elif op == 'subtract':
                result = n1 - n2
            elif op == 'multiply':
                result = n1 * n2
            elif op == 'divide':
                if n2 != 0:
                    result = n1 / n2
                else:
                    result = 'Error: Divide by zero'
        except:
            result = 'Invalid input'

    return render_template('calculator.html', result=result)

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged out successfully.")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
