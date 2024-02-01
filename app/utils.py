#код, который используют все парсеры
import requests
from .model import Post
from . import db


def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

    try:
        result = requests.get(url, headers = headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Network error')
        return False
    

def save_post(title, text, created_at, author, source, category=None):
    post_exists = Post.query.filter(Post.source == source).count()
    if not post_exists:
        post_new = Post(title = title, text = text, created_at = created_at, author = author, source = source, category = category)
        db.session.add(post_new)
        db.session.commit()
