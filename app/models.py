from secrets import token_hex
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

cart = db.Table('cart',
    db.Column('cart_id', db.Integer, primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('item_id', db.Integer, db.ForeignKey('item.id'))
)

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id')),
)


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    contribution_id = db.relationship("Contribution")
    apitoken = db.Column(db.String, default = None, nullable=True)

    cart = db.relationship("Item",
        secondary = cart,
        backref = 'shoppers',
        lazy = 'dynamic'
    )

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.apitoken = token_hex(16)

    def to_dict(self):
        return{
            'id' : self.id,
            'username' : self.username,
            'email' : self.email
        }
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    img_url = db.Column(db.String(300))
    caption = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, img_url, caption, user_id):
        self.title = title
        self.img_url = img_url
        self.caption = caption
        self.user_id = user_id

    def updatePostInfo(self, title, img_url, caption):
        self.title = title
        self.img_url = img_url
        self.caption = caption

    def save(self):
        db.session.add(self)
        db.session.commit()

    def saveUpdates(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    description = db.Column(db.String)
    img_url = db.Column(db.String) 

    def __init__(self, name, price, description, img_url):
        self.name = name
        self.price = price
        self.description = description
        self.img_url = img_url

    def saveItem(self):
        db.session.add(self)
        db.session.commit()  

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


   
