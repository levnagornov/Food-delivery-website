from flask import render_template, request, Blueprint


view_blp = Blueprint("view_blp", __name__)


@view_blp.route("/", methods=["GET", "POST"])
def render_index():
    """Main page"""
    pass


@view_blp.route("/cart/", methods=["GET", "POST"])
def render_cart():
    """Cart page with user's selected products"""
    pass


@view_blp.route("/account/", methods=["GET", "POST"])
def render_account():
    """Personal account page"""
    pass


@view_blp.route("/auth/", methods=["GET", "POST"])
def render_auth():
    """Authentication page"""
    pass


@view_blp.route("/register/", methods=["GET", "POST"])
def render_register():
    """User register page"""
    pass


@view_blp.route("/logout/", methods=["GET", "POST"])
def render_logout():
    """Logout of authorized user page"""
    pass


@view_blp.route("/ordered/", methods=["GET", "POST"])
def render_ordered():
    "Submit of order page"
    pass
