from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

#many-to-many table Order and Dish
order_has_dish = db.Table(
    "orders_dishes",
    db.Column("order_id", db.Integer, db.ForeignKey("orders.id")),
    db.Column("dish_id", db.Integer, db.ForeignKey("dishes.id")),
)

class User(db.Model, UserMixin):
    """
    This is `User` SQLAlchemy model.
    1. `User` is related with `Order` (one-to-many);
    """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


class Dish(db.Model):
    """
    This is `Dish` SQLAlchemy model.
    1. `Dish` is related with `Category` (many-to-one);
    2. `Dish` is related with `Order` (many-to-many);
    """

    __tablename__ = "dishes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    picture = db.Column(db.String, nullable=False)
    
    category = db.relationship("Category")
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)

    orders = db.relationship("Order", secondary=order_has_dish, back_populates="dishes")


class Category(db.Model):
    """
    This is `Category` SQLAlchemy model.
    1. `Category` is related with `Dish` (one-to-many);
    """

    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)


class Order(db.Model):
    """
    This is `Order` SQLAlchemy model.
    1. `Order` is related with `User` (many-to-one);
    2. `Order` is related with `Dish` (many-to-many);
    """

    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    sum = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    address = db.Column(db.Text, nullable=False)

    user = db.relationship("User")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    dishes = db.relationship("Dish", secondary=order_has_dish, back_populates="orders")
