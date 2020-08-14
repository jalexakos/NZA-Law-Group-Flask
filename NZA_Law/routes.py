from NZA_Law import app, db, Message, mail
from flask import render_template, request, redirect, url_for

# Forms import
# from NZA_Law.forms import [INSERT FORMS HERE]

# Models import
# from NZA_Law.models import [INSERT MODELS HERE]

# Flask Login import
from flask_login import login_required, login_user, current_user, logout_user

# Home route - Josh
@app.route('/')
def home():
    return render_template("index.html")

# Register route - Mike


# Create Case route - Leland


# Retrieve Case route - Stephanie


# Updating Case route - Stephanie


# Deleting Case route - Stephanie


# Login route - Josh


# Logout route - Josh