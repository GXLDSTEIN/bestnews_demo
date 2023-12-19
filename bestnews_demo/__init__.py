from flask import Flask, render_template
from bestnews_demo import data


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        context = {
            "economic_news": data.economic_news,
            "it_news": data.it_news,
            "entertainment_news": data.entertainment_news,
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

    return app
