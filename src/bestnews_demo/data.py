from datetime import datetime

economic_news = [
    {"title": "News 1", "summary": "Brief content of the news 1"},
    {"title": "News 2", "summary": "Краткое содержание новости 2"},
    # ...
]
it_news = [
    {
        "news_id": 0,
        "title": "news1",
        "text": "all content of the news 1 - very long news article",
        "summary": "short summary of the news 1",  # TODO: text[:140]
        "created_at": datetime(2027, 12, 31, 10, 30, 00),
        "author": "David Blaine",
    },
    {
        "news_id": 1,
        "title": "news2",
        "text": "all content of the news 1 - very long news article",
        "summary": "Brief content of the news 2",
        "created_at": datetime(2027, 12, 31, 10, 30, 00),
        "author": "David Blaine",
    }
    # ...
]
entertainment_news = [
    {"title": "News 1", "summary": "Brief content of the news 1"},
    {"title": "News 2", "summary": "Brief content of the news 2"},
    # ...
]


def get_posts():
    pass
