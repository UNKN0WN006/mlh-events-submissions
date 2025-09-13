from flask import Flask, render_template, request, redirect, session
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = 'key'

# Create database and users table
def make_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, pwd TEXT)''')
    conn.commit()
    conn.close()

make_db()

# Save user with hashed password
def save_user(name, pwd):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    hashed = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
    c.execute('INSERT INTO users (name, pwd) VALUES (?, ?)', (name, hashed))
    conn.commit()
    conn.close()

# Check user login
def check_user(name, pwd):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT pwd FROM users WHERE name=?', (name,))
    row = c.fetchone()
    conn.close()
    if row:
        return bcrypt.checkpw(pwd.encode(), row[0])
    return False

@app.route('/')
def home():
    return redirect('/login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        pwd = request.form['pwd']
        # Only create account if username does not exist
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('SELECT id FROM users WHERE name=?', (name,))
        exists = c.fetchone()
        conn.close()
        if exists:
            return render_template('signup.html', error='Username already exists!')
        # Save user and fetch stored hash
        save_user(name, pwd)
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('SELECT pwd FROM users WHERE name=?', (name,))
        row = c.fetchone()
        conn.close()
        stored_hash = row[0].decode() if row else ''
        return render_template('done.html', name=name, hash=stored_hash)
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        pwd = request.form['pwd']
        # Brute-force protection: track failed attempts in session
        if 'tries' not in session:
            session['tries'] = 0
        if session['tries'] >= 5:
            return 'Too many failed attempts. Try later.'
        if check_user(name, pwd):
            session['user'] = name
            session['tries'] = 0
            # Fetch hash from DB
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute('SELECT pwd FROM users WHERE name=?', (name,))
            row = c.fetchone()
            conn.close()
            user_hash = row[0].decode() if row else ''
            return redirect(f'/welcome?name={name}&hash={user_hash}')
        else:
            session['tries'] += 1
            return f'Wrong info! Attempts left: {5-session["tries"]}'
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    name = request.args.get('name', 'User')
    user_hash = request.args.get('hash', '')
    return render_template('welcome.html', name=name, user_hash=user_hash)


# Health check route for Render
@app.route('/healthz')
def healthz():
    return "OK", 200

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
