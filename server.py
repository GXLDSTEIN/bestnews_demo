from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        economic_news=data.economic_news,
        it_news=data.it_news,
        entertainment_news=data.entertainment_news,
    )


@app.route("/post/<news_id>")
def post(news_id):
    news_id = int(news_id)
    return render_template(
        "post.html",
        news_id=news_id,
        title=data.it_news[news_id]["title"],
        text=data.it_news[news_id]["text"],
        author=data.it_news[news_id]["author"],
        created_at=data.it_news[news_id]["created_at"],
    )


if __name__ == "__main__":
    app.run(debug=True)
