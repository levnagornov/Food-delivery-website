from enum import unique
from flask_sqlalchemy import SQLAlchemy
#from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class User(db.Model):
    """"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    orders_id = db.Column(db.Float, nullable=False)
    orders = []


class Dish(db.Model):
    """"""
    __tablename__ = "dishes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    price = db.Column(db.String, nullable=False)
    description = db.Column(db.Float, nullable=False)
    picture = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Float, nullable=False)
    category = []


class Category(db.Model):
    """"""
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    dish_id = db.Column(db.String, nullable=False)
    dish = db.Column(db.Float, nullable=False)


class Order(db.Model):
    """"""
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    sum = db.Column(db.String, nullable=False)
    status = db.Column(db.Float, nullable=False)
    email = db.Column(db.Float, nullable=False)
    phone = db.Column(db.Float, nullable=False)
    address = db.Column(db.Float, nullable=False)
    dish_id = db.Column(db.Float, nullable=False)
    dish = []