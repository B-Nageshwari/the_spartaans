# Import necessary libraries and modules
from flask import Flask, render_template, redirect, url_for, request, session , Blueprint
from src import get_config
from blueprints import home, api
from src.Database import Database
from src.Auth import Auth

# Configure the database connection
db = Database.get_connection()

bp = Blueprint("api", __name__, url_prefix="/api")

# Home blueprint routes
@bp.route("/maps")
def maps():
    # Check if the user is authenticated before rendering the maps page
    if 'authenticated' in session and session['authenticated']:
        return render_template('maps.html')
    else:
        # Redirect to login if the user is not authenticated
        return redirect(url_for('home.login'))

# API blueprint routes
@bp.route("/login", methods=['POST'])
def login():
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        result = Auth.login(username, password)
        if result == "Login successful":
            # Set a session variable or cookie to track the authenticated user
            session['authenticated'] = True
            # Redirect to the maps page
            return redirect(url_for('api.maps'))
        else:
            return str(result)
        
@bp.route("/register", methods=['POST'])
def register():
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
            return redirect(url_for('api.maps'))
        else:
            return str(result)


