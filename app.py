from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from sqlalchemy.sql import func

from models import db, User
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

csrf = CSRFProtect(app)  # CSRF token for correct work of WTForms module

migrate = Migrate(app, db, render_as_batch=True)
db.init_app(app)


if __name__ == "__main__":
    app.run()