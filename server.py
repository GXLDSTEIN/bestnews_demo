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


if __name__ == "__main__":
    app.run(debug=True)
