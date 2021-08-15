from flask import render_template, request, Blueprint

from models import db

view_blp = Blueprint("view_blp", __name__)


@view_blp.route("/", methods=["GET", "POST"])
def render_index():
    """Main page"""

    return render_template("index.html")


@view_blp.route("/cart/", methods=["GET", "POST"])
def render_cart():
    """Cart page with user's selected products"""
    
    return render_template("cart.html")


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
