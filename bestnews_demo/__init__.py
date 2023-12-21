from flask import Flask, render_template, request, abort
from bestnews_demo import data
from .data import get_posts
from .constants import TITLES, HEADLINES


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        context = {
            "economic_news": data.economic_news,
            "it_news": data.it_news,
            "entertainment_news": data.entertainment_news,
            "your_news": data.your_news,
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
