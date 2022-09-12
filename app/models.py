from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash

db = SQLAlchemy()



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    # charity_id = db.relationship("Charity", backref='user', lazy=True)
    # charity_id = db.relationship("Charity", )

#  user = User(username, email, password)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password = generate_password_hash(password)
        # self.charity_id = charity_id

class Charity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(200))
    img_url =  db.Column(db.String(400))
    type =  db.Column(db.String(50))

    def __init__(self, location, img_url, type):
        self.location = location
        self.img_url = img_url
        self.type = type
        
class Contribution(db.Model):
    amount = db.Column(db.Integer, primary_key=True)
    charity_id = db.Column(db.Integer, db.ForeignKey('charity.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, amount, charity_id, user_id):
        self.amount = amount
        self.charity_id = charity_id
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