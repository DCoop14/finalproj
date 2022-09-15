from secrets import token_hex
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    contribution_id = db.relationship("Contribution")


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Charity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(200))
    img_url =  db.Column(db.String(400))
    type =  db.Column(db.String(50))
    # contribution_id = db.relationship("Contribution")
    

    def __init__(self, location, img_url, type):
        self.location = location
        self.img_url = img_url
        self.type = type
        
        
class Contribution(db.Model):
    id = db.Column(db.String, primary_key=True)
    amount = db.Column(db.Integer)
    charity_id2 = db.Column(db.String)
    # charity_id = db.Column(db.Integer, db.ForeignKey('charity.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # user_rel = db.relationship("User")


    def __init__(self, amount, charity_id, user_id):
        self.id = token_hex(16)
        self.amount = amount
        self.charity_id2 = charity_id
        self.user_id = user_id


class Goal(db.Model):
    id = db.Column(db.String, primary_key=True)
    amount = db.Column(db.Integer)
    # charity_id = db.Column(db.String)
    # charity_id = db.Column(db.Integer, db.ForeignKey('charity.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # user_rel = db.relationship("User")


    def __init__(self, amount, user_id):
        self.id = token_hex(16)
        self.amount = amount
        # self.charity_id2 = charity_id
        self.user_id = user_id

class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    charity_id = db.Column(db.Integer, db.ForeignKey('charity.id'), nullable=False)
    hours = db.Column(db.Integer)

    def __init__(self, user_id, charity_id, hours):
        self.user_id = user_id
        self.charity_id = charity_id
        self.hours = hours