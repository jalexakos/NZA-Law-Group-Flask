from NZA_Law import app, db, login

# Password security
from werkzeug.security import generate_password_hash, check_password_hash

# Datetime from flask
from datetime import datetime

from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return Lawyer.query.get(int(user_id)) # This connects to the lawyer class that will be built here

# Lawyer class - Mike



# Case class - Leland


