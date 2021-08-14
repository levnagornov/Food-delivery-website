from flask import render_template, request

from app import app


@app.route("/", methods=["GET", "POST"])
def render_index():
    """Main page"""
    pass


@app.route("/cart/", methods=["GET", "POST"])
def render_cart():
    """Cart page with user's selected products"""
    pass


@app.route("/account/", methods=["GET", "POST"])
def render_account():
    """Personal account page"""
    pass


@app.route("/auth/", methods=["GET", "POST"])
def render_auth():
    """Authentication page"""
    pass


@app.route("/register/", methods=["GET", "POST"])
def render_register():
    """User register page"""
    pass


@app.route("/logout/", methods=["GET", "POST"])
def render_logout():
    """Logout of authorized user page"""
    pass


@app.route("/ordered/", methods=["GET", "POST"])
def render_ordered():
    "Submit of order page"
    pass
