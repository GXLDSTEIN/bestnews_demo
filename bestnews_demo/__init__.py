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

    @app.route("/posts/<category>")
    def get_posts_by_category(category):
        context = get_posts()
        try:
            if category == "it_news":
                posts = context["it_news"]
                title = "IT News"
                headline = "Stay Updated on the Latest Tech Trends"
            elif category == "economic_news":
                posts = context["economic_news"]
                title = "Economic News"
                headline = "Latest News in the Economy"
            elif category == "entertainment_news":
                posts = context["entertainment_news"]
                title = "Entertainment News"
                headline = "Discover the Latest Entertainment Stories"
            elif category == "your_news":
                posts = context["your_news"]
                title = "Blogs from You"
                headline = "Latest Stories from Readers"
            else:
                return "Invalid category"

            return render_template(
                "posts_page.html", posts=posts, title=title, headline=headline
            )
        except KeyError as e:
            return f"Error: {e}"

    return app
