from flask import Flask, render_template, request, redirect, url_for
from flask.sansio.app import App

app = Flask(__name__)

# In-memory user data for demonstration
users = {}

@app.route('/')
def home():
    return "Welcome! Go to /login or /signup"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return "User already exists!"
        users[username] = password
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            return f"Welcome, {username}!"
        return "Invalid username or password"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
