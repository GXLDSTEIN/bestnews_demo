from flask import Flask, render_template, request, abort
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
from .model import db, Post, User


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route("/")
    def index():
        context = {
            ECONOMIC_NEWS_CATEGORY: data.economic_news,
            IT_NEWS_CATEGORY: data.it_news,
            ENTERTAINMENT_NEWS_CATEGORY: data.entertainment_news,
            YOUR_NEWS_CATEGORY: data.your_news,
        }
        return render_template("index.html", **context)

    @app.route("/post/<news_id>")
    def post(news_id):
        try:
            news_id = int(news_id)
            context = {
                "title": data.it_news[news_id]["title"],
                "text": data.it_news[news_id]["text"],
                "author": data.it_news[news_id]["author"],
                "created_at": data.it_news[news_id]["created_at"],
            }
            print(context)
            return render_template("post.html", **context)
        except (IndexError, ValueError):
            return "404"

    @app.route("/all_posts")
    def all_posts():
        posts = []
        for _, news in get_posts().items():
            posts.extend(news)
        title = "All News"
        headline = "Latest News from all categories"
        return render_template(
            "posts_page.html", posts=posts, title=title, headline=headline
        )

    @app.route("/posts")
    def get_posts_by_category():
        all_news = get_posts()
        category = request.args.get("category")
        if category is None or category == "":
            return all_posts()
        if category not in TITLES or category not in HEADLINES:
            abort(404, f"Category '{category}' not found")
        posts = all_news.get(category, [])
        title = TITLES.get(category)
        headline = HEADLINES.get(category)
        return render_template(
            "posts_page.html", posts=posts, title=title, headline=headline
        )

    return app
