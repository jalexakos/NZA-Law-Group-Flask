from NZA_Law import app, db, login

# Password security
from werkzeug.security import generate_password_hash, check_password_hash

# Datetime from flask
from datetime import datetime

from flask_login import UserMixin

@login.user_loader
def load_user(lawyer_id):
    return Lawyer.query.get(int(lawyer_id)) # This connects to the lawyer class that will be built here

# Lawyer class - Mike
class Lawyer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    case = db.relationship('Case', backref='author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'{self.username} has been created with {self.email}'


# Case class - Leland
class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    caseNum = db.Column(db.String(200))
    caseNotes = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    lawyer_id = db.Column(db.Integer, db.ForeignKey('lawyer.id'), nullable=False)

    def __init__(self, caseNum, caseNotes, lawyer_id):
        self.caseNum = caseNum
        self.caseNotes = caseNotes
        self.lawyer_id = lawyer_id

    def __repr__(self):
        return f"The title of the case is {self.caseNum}\n and the notes {self.caseNotes}."


