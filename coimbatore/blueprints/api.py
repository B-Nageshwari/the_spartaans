# Import necessary libraries and modules
from flask import Flask, render_template, redirect, url_for, request, session
from src import get_config
from blueprints import home, api
from src.Database import Database
from src.Auth import Auth

# Create a Flask application
application = app = Flask(__name__, static_folder='assets', static_url_path="/")
app.secret_key = get_config("secret_key")

# Register blueprints
app.register_blueprint(home.bp)
app.register_blueprint(api.bp)

# Configure the database connection
db = Database.get_connection()

# Home blueprint routes
@home.bp.route("/maps")
def maps():
    # Check if the user is authenticated before rendering the maps page
    if 'authenticated' in session and session['authenticated']:
        return render_template('maps.html')
    else:
        # Redirect to login if the user is not authenticated
        return redirect(url_for('home.login'))

# API blueprint routes
@api.bp.route("/login", methods=['POST'])
def login():
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        result = Auth.login(username, password)
        if result == "Login successful":
            # Set a session variable or cookie to track the authenticated user
            session['authenticated'] = True
            # Redirect to the maps page
            return redirect(url_for('home.maps'))
        else:
            return str(result)
        
@api.bp.route("/register", methods=['POST'])
def login():
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        vehicleNumber = request.form['vehicleNumber']
        vehicleType = request.form['vehicleType']

        result = Auth.register(username, password,vehicleNumber,vehicleType)
        if result == "Registration successful":
            # Set a session variable or cookie to track the authenticated user
            session['authenticated'] = True
            # Redirect to the maps page
            return redirect(url_for('home.maps'))
        else:
            return str(result)

# Run the application
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=7000, debug=True)

