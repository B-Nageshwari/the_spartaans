from flask import Blueprint, render_template, redirect, url_for, request, session
import json
from src.Auth import Auth


#bp = Blueprint("home", __name__, url_prefix="/")
bp = Blueprint("parking", __name__, url_prefix="/")


@bp.route("/")
def home():
     return render_template('index.html', session=session)


@bp.route("/login")
def login():
     return render_template('login.html', session=session)


@bp.route("/register")
def register():
     return render_template('register.html', session=session)


@bp.route("/dash")
def dashboard():
     return render_template('dashboard.html', session=session)


@bp.route("/blog")
def blog():
     return render_template('blog.html', session=session)


@bp.route("/contact")
def contact():
     return render_template('contact.html', session=session)
