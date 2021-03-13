from flask import Flask

# TODO: Import Config Object for Flask Project
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Import for Login Manager
from flask_login import UserMixin

# Import for Flask Login
from flask_login import LoginManager

# Import for AuthLib integrations
from authlib.integrations.flask_client import OAuth

# Import for Flask-Marshmallow
from flask_marshmallow import Marshmallow

from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

db = SQLAlchemy(app) #review what's going on here and next line
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'signin' #Specify what page to load for Non-Authed users

oauth = OAuth(app)

ma = Marshmallow(app)

from drone_api import routes, models
