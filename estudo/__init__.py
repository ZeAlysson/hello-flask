from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # import the SQLAlchemy class from the flask_sqlalchemy module
from flask_migrate import Migrate  # import the Migrate class from the flask_migrate module
from dotenv import load_dotenv  # import the load_dotenv function from the dotenv module

from flask_login import LoginManager  # import the LoginManager class from the flask_login module
from flask_bcrypt import Bcrypt  # import the Bcrypt class from the flask_bcrypt module


import os  # import the os module
load_dotenv('.env')  # load the .env file

app = Flask(__name__)  # create an instance of the Flask class
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')  # set the database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # set the track modifications to False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')  # set the secret key

db = SQLAlchemy(app)  # create an instance of the SQLAlchemy class
migrate = Migrate(app, db)  # create an instance of the Migrate class
login_manager = LoginManager(app)  # create an instance of the LoginManager class
login_manager.login_view = 'homepage'  # set the login view
bCrypt = Bcrypt(app)  # create an instance of the Bcrypt class

from estudo.views import homepage  # import the views module
from estudo.models import Contato  # import the models module