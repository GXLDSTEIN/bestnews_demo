from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for, get_flashed_messages
)
from flask_login import login_user, logout_user, current_user

from bestnews_demo import data, db

from .constants import (
    ECONOMIC_NEWS_CATEGORY,
    ENTERTAINMENT_NEWS_CATEGORY,
    HEADLINES,
    IT_NEWS_CATEGORY,
    TITLES,
    YOUR_NEWS_CATEGORY,
)
from .data import get_posts_db
from .forms import LoginForm, RegistrationForm
from .model import User

views = Blueprint("views", __name__)


@views.route("/")
def index():
    context = {
        ECONOMIC_NEWS_CATEGORY: data.economic_news,
        IT_NEWS_CATEGORY: data.it_news,
        ENTERTAINMENT_NEWS_CATEGORY: data.entertainment_news,
        YOUR_NEWS_CATEGORY: data.your_news,
    }
    flash_messages = get_flashed_messages()
    return render_template("index.html", flash_messages=flash_messages, **context)


@views.route("/post/<news_id>")
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


def all_posts():
    posts = []
    for _, news in get_posts_db().items():
        posts.extend(news)
    title = "All News"
    headline = "Latest News from all categories"
    return render_template(
        "posts_page.html", posts=posts, title=title, headline=headline
    )


@views.route("/posts")
def get_posts():
    all_news = get_posts_db()
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


@views.route("/login")
def login():
    title = "Authorization"
    login_form = LoginForm()
    return render_template("login.html", page_title=title, form=login_form)


@views.route("/process-login", methods=["POST"])
def process_login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("You are logged in")
            return redirect(url_for("views.index"))
    flash("Incorrect username or password")
    return redirect(url_for("views.login"))


@views.route("/logout")
def logout():
    logout_user()
    flash("You are logged out")
    return redirect(url_for("views.index"))


@views.route("/register")
def register():
    if current_user.is_authenticated:
        return redirect(url_for('views.index'))
    form = RegistrationForm()
    title = "Registration"
    return render_template('registration.html',
            page_title=title, form=form)
    

@views.route("/process-reg", methods=["POST"])
def process_reg():
    form = RegistrationForm()

    if request.method == "POST" and form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('You are successfully registered!')
        return redirect(url_for('views.login'))

    flash('Please, check the entered information')
    for field, errors in form.errors.items():
        for error in errors:
            flash('Error in the field "{}": - {}'.format(
                getattr(form, field).label.text,
                error
            ))
    return redirect(url_for('views.register'))
