from datetime import datetime

economic_news = [
    {
        "news_id": 50,
        "title": "news1",
        "text": "all content of the news 1 - very long news article",
        "summary": "short summary of the news 1",  # TODO: text[:140]
        "created_at": datetime(2027, 12, 31, 10, 30, 00),
        "author": "David Blaine",
    },
    {
        "news_id": 18,
        "title": "news2",
        "text": "all content of the news 1 - very long news article",
        "summary": "Brief content of the news 2",
        "created_at": datetime(2027, 12, 31, 10, 30, 00),
        "author": "David Blaine",
    }
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
    {
        "news_id": 60,
        "title": "news1",
        "text": "all content of the news 1 - very long news article",
        "summary": "short summary of the news 1",  # TODO: text[:140]
        "created_at": datetime(2027, 12, 31, 10, 30, 00),
        "author": "David Blaine",
    },
    {
        "news_id": 13,
        "title": "news2",
        "text": "all content of the news 1 - very long news article",
        "summary": "Brief content of the news 2",
        "created_at": datetime(2027, 12, 31, 10, 30, 00),
        "author": "David Blaine",
    }
    # ...
]

your_news = [
    {
        "news_id": 34,
        "title": "Updated Title 1",
        "text": "Updated content of the news 1 - very long news article",
        "summary": "Updated summary of the news 1",
        "created_at": datetime(2027, 12, 31, 10, 30, 00),
        "author": "John Doe",
    },
    {
        "news_id": 44,
        "title": "Updated Title 2",
        "text": "Updated content of the news 2 - very long news article",
        "summary": "Updated content of the news 2",
        "created_at": datetime(2027, 12, 31, 10, 30, 00),
        "author": "Jane Doe",
    }
    # ...
]


def get_posts():
    return {
        "it_news": it_news,
        "economic_news": economic_news,
        "entertainment_news": entertainment_news,
        "your_news": your_news,
    }
