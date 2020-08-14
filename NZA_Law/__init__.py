from flask import Flask

from config import Config

# Importing Flask DB and Migrator
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Importing Flask Mail and Flask Login
from flask_mail import Mail, Message
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)
mail = Mail(app)

#Configuring Login
login = LoginManager(app)
login.login_view = 'login' # Specifying which page to load when a user is non-authenticated

from NZA_Law import routes, models 