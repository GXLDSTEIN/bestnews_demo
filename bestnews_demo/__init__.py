from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from .model import db, User
from .views import views


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login"
    app.register_blueprint(views, url_prefix="/")

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    migrate = Migrate(app, db)

    return app
