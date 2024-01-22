from flask import Flask, render_template, request, abort, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from bestnews_demo import data
from .data import get_posts
from .constants import (
    YOUR_NEWS_CATEGORY,
    IT_NEWS_CATEGORY,
    ECONOMIC_NEWS_CATEGORY,
    ENTERTAINMENT_NEWS_CATEGORY,
    HEADLINES,
    TITLES,
)
from .forms import LoginForm
from .model import db, Post, User
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
