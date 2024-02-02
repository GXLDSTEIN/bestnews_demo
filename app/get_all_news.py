from app import create_app
from app import techcrunch
from app import refinery29
from app import cnbc

app = create_app()
with app.app_context():
    # refinery29.get_refinery29_snippets()
    techcrunch.get_githubblog_snippets()
    # cnbc.get_cnbc_snippets()