from collections import Counter, OrderedDict

from flask import render_template, request, Blueprint, session, redirect
from flask.helpers import url_for

from sqlalchemy.sql import func

from models import *


view_blp = Blueprint("view_blp", __name__)


@view_blp.route("/", methods=["GET", "POST"])
def render_index():
    """Main page"""

    categories = db.session.query(Category).all()
    category_with_dishes = {
        category.title : db.session.query(Dish) \
                            .filter(Dish.category_id==category.id) \
                            .order_by(func.random()) \
                            .limit(3)
        for category in categories
    }

    return render_template(
        "index.html", 
        category_with_dishes=category_with_dishes
    )

@view_blp.route("/addtocart/<dish_id>", methods=["GET", "POST"])
def render_addtocart(dish_id):
    dish = db.session.query(Dish).get(dish_id)
    if dish is None:
        return render_page_not_found(404, msg="Такого товара не существует.")
    
    cart = session.get("cart", OrderedDict())
    if not cart.get(dish_id):
        cart[dish_id] = 1
    else:
        cart[dish_id] += 1
    session['cart'] = cart

    return redirect(url_for("view_blp.render_cart"))


@view_blp.route("/resetcart/", methods=["GET", "POST"])
def render_resetcart():
    """Endpoint to reset user cart"""

    session.pop('cart')

    return redirect(url_for("view_blp.render_cart"))


@view_blp.route("/cart/", methods=["GET", "POST"])
def render_cart():
    """Cart page with user's selected products"""

    cart = session.get("cart", {})
    cart_dish_amount = [
        (db.session.query(Dish).get(int(dish_id)), amount)
        for dish_id, amount in cart.items()
    ]

    session['order_amount'] = len(cart_dish_amount)
    session['order_sum'] = sum(
        [dish.price * amount for dish, amount in cart_dish_amount]
    )

    return render_template(
        "cart.html", 
        cart=cart_dish_amount, 
        order_sum=session['order_sum'],
        order_amount=session['order_amount']
    )


@view_blp.route("/account/", methods=["GET", "POST"])
def render_account():
    """Personal account page"""

    return render_template("account.html")


@view_blp.route("/auth/", methods=["GET", "POST"])
def render_auth():
    """Authentication page"""

    return render_template("auth.html")


@view_blp.route("/register/", methods=["GET", "POST"])
def render_register():
    """User register page"""
    
    return render_template("register.html")


@view_blp.route("/logout/", methods=["GET", "POST"])
def render_logout():
    """Logout of authorized user page"""

    return render_template("logout.html")


@view_blp.route("/ordered/", methods=["GET", "POST"])
def render_ordered():
    "Submit of order page"

    return render_template("ordered.html")


@view_blp.errorhandler(500)
def render_server_error(error, msg="Что-то не так, но мы все починим!"):
    """Handling 500 error."""

    return render_template("error.html", msg=msg), 500


@view_blp.errorhandler(404)
def render_page_not_found(
    error, msg="Ничего не нашлось! Вот неудача, отправляйтесь на главную!"
):
    """Handling 404 error"""

    return render_template("error.html", msg=msg), 404


@view_blp.errorhandler(400)
def render_bad_request(
    error, msg="Ошибка запроса! Вот неудача, отправляйтесь на главную или измените запрос!"
):
    """Handling 400 error"""

    return render_template("error.html", msg=msg), 400