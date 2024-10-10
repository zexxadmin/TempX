from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

# Load config.json
def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

# Save config.json
def save_config(data):
    with open('config.json', 'w') as file:
        json.dump(data, file, indent=4)

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Sign Up page route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Load current users
        config = load_config()
        if 'users' not in config:
            config['users'] = {}

        # Store the new user's details in config.json
        config['users'][username] = password
        save_config(config)
        return redirect(url_for('success'))

    return render_template('signup.html')

# Sign In page route
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Load current users
        config = load_config()
        if username in config['users'] and config['users'][username] == password:
            return redirect(url_for('success'))
        else:
            return "Invalid login. Please try again."

    return render_template('signin.html')

# Success page after sign in or sign up
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    # Listen on all interfaces and set the port to 5000
    app.run(host='0.0.0.0', port=5000, debug=True)