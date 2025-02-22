from estudo import db, login_manager  # import the db variable from the estudo package
from datetime import datetime  # import the datetime class from the datetime module
from flask_login import UserMixin  # import the UserMixin class from the flask_login module

@login_manager.user_loader  # use the user_loader decorator
def load_user(user_id):  # create a function called load_user that takes user_id as an argument
    return User.query.get(int(user_id))  # return the user with the specified user_id


class User(db.Model, UserMixin):  # create a class called User that inherits from db.Model
    id = db.Column(db.Integer, primary_key=True)  # create a column called id
    nome = db.Column(db.String(100), nullable=True)
    sobrenome = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True, unique=True)  # create a column called email
    senha = db.Column(db.String(100), nullable=True)  # create a column called password
    posts = db.relationship('Post', backref='user', lazy=True)  # create a relationship between the User and Post classes

class Contato(db.Model):  # create a class called Contato that inherits from db.Model
    id = db.Column(db.Integer, primary_key=True)  # create a column called id
    date_created = db.Column(db.DateTime, default=datetime.now)  # create a column called date_created
    name = db.Column(db.String(100), nullable=True)  # create a column called name
    email = db.Column(db.String(100), nullable=True)  # create a column called email
    assunto = db.Column(db.String(100), nullable=True)  # create a column called assunto
    message = db.Column(db.Text, nullable=True)  # create a column called message
    ansewered = db.Column(db.Integer, default=0)  # create a column called ansewered

class Post(db.Model):  # create a class called Post that inherits from db.Model
    id = db.Column(db.Integer, primary_key=True)  # create a column called id
    date_created = db.Column(db.DateTime, default=datetime.now)  # create a column called date_created
    mensagem = db.Column(db.Text, nullable=True)  # create a column called mensagem
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # create a column called user_id

