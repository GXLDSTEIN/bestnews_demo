import re
from datetime import datetime
from bs4 import BeautifulSoup
from .utils import get_html, save_post
from urllib.parse import urljoin


def is_author_link(tag):
            return tag.name == 'a' and tag.get('href') and tag['href'].startswith('/en-us/author/')

def get_refinery29_snippets():
    base_url = 'https://www.refinery29.com/en-us/fashion'
    html = get_html(base_url)
    if not html:
            print("HTML не получен.")
            return

    soup = BeautifulSoup(html, 'html.parser')
    all_posts = soup.find_all('div', class_='card standard')

    for post_link in all_posts:
        a_tag = post_link.find('a')
        
        if not a_tag:
                print("Тег со ссылкой не найден.")
                continue
        
        title_tag = a_tag.find('div', class_='title')

        if not title_tag:
            print("Тег <div> c классом <'title'>не найден.")
            continue

        title = title_tag.text.strip()
        source = urljoin(base_url, a_tag.get('href'))
        post_html = get_html(source)
        
        if not post_html:
            print("HTML для поста не получен.")
            continue

        post_soup = BeautifulSoup(post_html, 'html.parser')
        text_element = post_soup.find('div', class_='section-text')  
        text = text_element.text if text_element else "No text available"
        
        author_link = post_soup.find(is_author_link)
        
        if author_link:
            author = author_link.text.strip()
        else:
            author = "No author available"

        created_at_tag = post_soup.find('a', href=re.compile(r'/en-us/archives/\d{4}/\d{2}/\d{2}'))
        if created_at_tag:
            created_at_text = created_at_tag.find('span').text.strip()
            created_at = datetime.strptime(created_at_text, '%B %d, %Y, %I:%M %p')
        else:
            created_at = None
        
        category = "entertainment_news"

        save_post(title, text, created_at, author, source, category=category)
        

    if __name__ == "__main__":
        get_refinery29_snippets()


