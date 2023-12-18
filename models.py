from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

class Product_Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    quantitySold = db.Column(db.Integer, nullable=False)
    quantityAvailable = db.Column(db.Integer, nullable=False)


class Product_Earnings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    earnings_date = db.Column(db.DateTime, default=datetime.utcnow)
    earnings_amount = db.Column(db.Float, nullable=False)
