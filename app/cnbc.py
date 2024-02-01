import re
from datetime import datetime
from bs4 import BeautifulSoup
from .utils import get_html, save_post

def extract_date_from_url(url):
    # Используем регулярное выражение для извлечения даты из URL
    match = re.search(r'/(\d{4}/\d{2}/\d{2})/', url)
    
    if match:
        date_str = match.group(1)
        # Преобразуем строку в формат datetime
        return datetime.strptime(date_str, "%Y/%m/%d")
    
    return None

def get_cnbc_snippets():
    base_url = 'https://www.cnbc.com/world/?region=world'
    html = get_html(base_url)

    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_posts = soup.find_all('div', class_='RiverPlusCard-cardLeft')

        for post_soup in all_posts:
            headline_link = post_soup.find('a')
            author_element = post_soup.find('span', class_='RiverByline-authorByline')
            author = author_element.text.strip() if author_element else "Автор не указан"

            if headline_link:
                title = headline_link.text.strip()
                source = headline_link.get('href')
                created_at = extract_date_from_url(source)

                post_html = get_html(source)

                if post_html:
                    post_soup = BeautifulSoup(post_html, 'html.parser')
                    article_body = post_soup.find('div', class_='ArticleBody-articleBody')

                    if article_body:
                        paragraphs = article_body.find_all('p')

                        if paragraphs:
                            text = ' '.join(paragraph.text.strip() for paragraph in paragraphs)
                        else:
                            text = None  
                    else:
                        text = None  
                else:
                    text = None  
            else:
                print("Не найдена ссылка на заголовок для этого поста.")
                continue  

            # Проверяем, что все элементы не являются None перед вызовом save_news, чтобы в базу записать только валидные значения
            if all(element is not None for element in [title, created_at, author, source, text]):
                
                category = "economic_news"
                save_post(title, text, created_at, author, source, category=category)  
            else:
                print("Не удалось получить один из элементов (title, created_at, author, source, text) для этого поста.")




