from estudo import db  # import the db variable from the estudo package
from datetime import datetime  # import the datetime class from the datetime module

class Contato(db.Model):  # create a class called Contato that inherits from db.Model
    id = db.Column(db.Integer, primary_key=True)  # create a column called id
    date_created = db.Column(db.DateTime, default=datetime.now)  # create a column called date_created
    name = db.Column(db.String(100), nullable=False)  # create a column called name
    email = db.Column(db.String(100), nullable=False)  # create a column called email
    assunto = db.Column(db.String(100), nullable=False)  # create a column called assunto
    message = db.Column(db.Text, nullable=False)  # create a column called message
    ansewered = db.Column(db.Integer, default=0)  # create a column called ansewered
