"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from Collector_V3 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/login')
def login():
    return render_template(
        'login.html',
        title='Login'
        )

def register():
    return render_template(
        'regester.html',
        title='Register'
        )

def logout():
    flash('You have been logged out!')
    return redirect(url_for('home'))

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
