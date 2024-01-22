from datetime import datetime

from .constants import (
    ECONOMIC_NEWS_CATEGORY,
    ENTERTAINMENT_NEWS_CATEGORY,
    IT_NEWS_CATEGORY,
    YOUR_NEWS_CATEGORY,
)

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
    },
    {
        "news_id": 25,
        "title": "Exciting Developments in Space Exploration",
        "text": "The latest advancements in space exploration have captivated the world. Scientists have made significant strides in understanding the cosmos, with new missions and discoveries pushing the boundaries of human knowledge.",
        "summary": "Explore the mysteries of the universe with the latest in space exploration.",
        "created_at": datetime(2023, 12, 17, 12, 15, 00),
        "author": "Space Enthusiast",
    },
    {
        "news_id": 37,
        "title": "Health Tech Revolutionizing Medical Care",
        "text": "Health technology continues to revolutionize the medical field, offering innovative solutions for patient care. From telemedicine to wearable devices, these technologies are shaping the future of healthcare.",
        "summary": "Discover how health tech is transforming the way we approach medical care.",
        "created_at": datetime(2023, 12, 18, 15, 45, 00),
        "author": "Medical Innovator",
    },
    {
        "news_id": 42,
        "title": "Culinary Delights: Trends in Gastronomy",
        "text": "Gastronomy enthusiasts rejoice as new culinary trends take center stage. From experimental flavors to sustainable practices, the world of food is evolving, offering exciting experiences for foodies everywhere.",
        "summary": "Indulge in the latest culinary trends and gastronomic adventures.",
        "created_at": datetime(2023, 12, 19, 10, 0, 00),
        "author": "Food Connoisseur",
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
        IT_NEWS_CATEGORY: it_news,
        ECONOMIC_NEWS_CATEGORY: economic_news,
        ENTERTAINMENT_NEWS_CATEGORY: entertainment_news,
        YOUR_NEWS_CATEGORY: your_news,
    }
