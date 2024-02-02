import re
from datetime import datetime
from bs4 import BeautifulSoup
from .utils import get_html, save_post

def extract_date_from_url(url):
    # Используем регулярное выражение
    match = re.search(r'/(\d{4}/\d{2}/\d{2})/', url)
    
    if match:
        date_str = match.group(1)
        # Преобразуем строку в формат datetime
        return datetime.strptime(date_str, "%Y/%m/%d")
    
    return None

def get_githubblog_snippets():
    url = 'https://techcrunch.com/category/startups/'
    html = get_html(url)

    if not html:
        print("HTML не получен.")
        return

    
    soup = BeautifulSoup(html, 'html.parser')
    all_posts = soup.find_all('a', class_='post-block__title__link')

    for post_link in all_posts:
        title = post_link.text.strip()
        source = post_link['href']

        post_html = get_html(source)

        if not post_html:
            print(f"HTML для поста {title} не получен.")
            continue

        post_soup = BeautifulSoup(post_html, 'html.parser')
        text_element = post_soup.find('div', class_='article-content')  
        text = text_element.text.strip() if text_element else "No text available"
        
        byline_wrapper_element = post_soup.find('div', class_='article__byline-wrapper')
        if byline_wrapper_element:
            byline_element = byline_wrapper_element.find('div', class_='article__byline')
            if byline_element:
                author_element = byline_element.find('a', href=True)
                author = author_element.text.strip() if author_element else "No author available"

                # Извлекаем дату из URL
                created_at = extract_date_from_url(source)
                category = "it_news"

            else:
                author = "No author available"
                created_at = "No date available"
        else:
            author = "No author available"
            created_at = "No date available"

        save_post(title, text, created_at, author, source, category=category)


if __name__ == "__main__":
    get_githubblog_snippets()
