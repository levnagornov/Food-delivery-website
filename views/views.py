from collections import OrderedDict
from re import U

from flask import render_template, request, Blueprint, session, redirect, url_for, flash
from flask_login import LoginManager, login_required, logout_user, current_user, login_user

from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.sql import func

from forms import CartForm, LoginForm, RegisterForm
from models import *


view_blp = Blueprint("view_blp", __name__)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(int(user_id))


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
        category_with_dishes=category_with_dishes,
        order_sum=session['order_sum'],
        order_amount=session['order_amount'],
    )


@view_blp.route("/removefromcart/<dish_id>", methods=["GET", "POST"])
def render_removefromcart(dish_id):
    """Endpoint to remove dish from user cart."""

    dish = db.session.query(Dish).get(int(dish_id))
    if dish is None:
        return render_page_not_found(404, msg="Такого товара не существует.")
    
    cart = session.get("cart", OrderedDict())
    if not cart.get(dish_id):
        return render_page_not_found(404, msg="Товар не в корзине.")
    
    if cart[dish_id] == 1:
        cart.pop(dish_id)
    else:
        cart[dish_id] -= 1
    session['cart'] = cart

    order = [
        (db.session.query(Dish).get(int(dish_id)), amount)
        for dish_id, amount in cart.items()
    ]

    session['order_amount'] = len(order)
    session['order_sum'] = sum(
        [dish.price * amount for dish, amount in order]
    )

    return redirect(url_for("view_blp.render_cart"))


@view_blp.route("/addtocart/<dish_id>", methods=["GET", "POST"])
def render_addtocart(dish_id):
    """Endpoint to add dish in user cart."""

    dish = db.session.query(Dish).get(int(dish_id))
    if dish is None:
        return render_page_not_found(404, msg="Такого товара не существует.")
    
    cart = session.get("cart", OrderedDict())
    if not cart.get(dish_id):
        cart[dish_id] = 1
    else:
        cart[dish_id] += 1
    session['cart'] = cart

    order = [
        (db.session.query(Dish).get(int(dish_id)), amount)
        for dish_id, amount in cart.items()
    ]

    session['order_amount'] = len(order)
    session['order_sum'] = sum(
        [dish.price * amount for dish, amount in order]
    )

    return redirect(url_for("view_blp.render_cart"))


@view_blp.route("/resetcart/", methods=["GET", "POST"])
def render_resetcart():
    """Endpoint to reset user cart."""

    session.pop('cart')

    return redirect(url_for("view_blp.render_cart"))


@view_blp.route("/cart/", methods=["GET", "POST"])
def render_cart():
    """Cart page with user's selected products"""

    cart = session.get("cart", {})
    order = [
        (db.session.query(Dish).get(int(dish_id)), amount)
        for dish_id, amount in cart.items()
    ]

    form = CartForm()

    if request.method == "POST" and form.validate_on_submit():
        pass

    return render_template(
        "cart.html", 
        cart=order, 
        order_sum=session['order_sum'],
        order_amount=session['order_amount'],
        form=form
    )


@view_blp.route("/account/", methods=["GET", "POST"])
def render_account():
    """Personal account page"""

    return render_template("account.html")


@view_blp.route("/auth/", methods=["GET", "POST"])
def render_auth():
    """Authentication page"""

    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user = db.session.query(User).filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("view_blp.render_index"))

        flash('Авторизация не успешна. Пожалуйста, проверьте пароль и электронную почту', 'danger')

    return render_template('auth.html', form=form)


@view_blp.route("/register/", methods=["GET", "POST"])
def render_register():
    """User register page"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()

    if request.method == "POST" and form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # user_exists = db.session.query(User).filter(User.email==email).first()
        
        # if user_exists:
            # error_msg = "Пользователь существует"
            # return render_template("register.html", error_msg=error_msg, form=form)     

        user = User(email=email, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("view_blp.render_index"))

    return render_template("register.html", form=form)


@view_blp.route("/logout/", methods=["GET", "POST"])
def render_logout():
    """Logout of authorized user page"""
    logout_user()
    return redirect(url_for('view_blp.render_index'))


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