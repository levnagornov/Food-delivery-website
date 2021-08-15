from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

from models import db
from config import Config
from views.views import view_blp

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(view_blp)

# CSRF token for correct work of WTForms module
csrf = CSRFProtect(app)  

# initializing database
db.init_app(app)
migrate = Migrate(app, db, render_as_batch=True)


if __name__ == "__main__":
    app.run()