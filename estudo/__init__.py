from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # import the SQLAlchemy class from the flask_sqlalchemy module
from flask_migrate import Migrate  # import the Migrate class from the flask_migrate module

app = Flask(__name__)  # create an instance of the Flask class
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # set the database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # set the track modifications to False

db = SQLAlchemy(app)  # create an instance of the SQLAlchemy class
migrate = Migrate(app, db)  # create an instance of the Migrate class

from estudo.views import hello_world  # import the views module
from estudo.models import Contato  # import the models module