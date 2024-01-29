from src.Database import Database
from time import time
import json
from flask import jsonify,session
import datetime


db = Database.get_connection()
users_collection = db.auth

class Auth:
    @staticmethod
    def register(username, password,vehicleType,vehicleNumber):
        # Check if user already exists
        if users_collection.find_one({"username": username}):
            return "User already exists"

        # Insert new user into the database
        users_collection.insert_one({"username": username, "password": password,"vehicleType":vehicleType,"vehicleNumber":vehicleNumber})
        return "Registration successful"

    @staticmethod
    def login(username, password):
        # Find the user in the database
        user = users_collection.find_one({"username": username})

        if user:
            # Check if the passwords match
            if password == user['password']:
                session['authenticated'] = True
                return "Login successful"
            else:
                return "Wrong password"
        else:
            return "User not found"
