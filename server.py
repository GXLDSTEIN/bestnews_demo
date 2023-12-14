from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    economic_news = [
        {"title": "News 1", "summary": "Brief content of the news 1"},
        {"title": "News 2", "summary": "Краткое содержание новости 2"},
        # ...
    ]
    it_news = [
        {"title": "News 1", "summary": "Brief content of the news 1"},
        {"title": "News 2", "summary": "Brief content of the news 2"},
        # ...
    ]
    entertainment_news = [
        {"title": "News 1", "summary": "Brief content of the news 1"},
        {"title": "News 2", "summary": "Brief content of the news 2"},
        # ...
    ]
    return render_template(
        "index.html",
        economic_news=economic_news,
        it_news=it_news,
        entertainment_news=entertainment_news,
    )


if __name__ == "__main__":
    app.run(debug=True)
