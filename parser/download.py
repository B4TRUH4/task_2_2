import os
from urllib import parse
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date

from config import BASE_URL, PAGE_URL, BREAKPOINT_YEAR


def parse_page() -> list[tuple[str, date]]:
    """Извлекает блоки, содержащие ссылки на файлы со страницы"""
    links = []
    page_num = 1
    while True:
        print(f'Страница {page_num}')
        response = requests.get(f'{PAGE_URL}{page_num}')
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        tab = soup.find(
            'div',
            class_='page-content__tabs__block',
            attrs={'data-tabcontent': '1'},
        )
        blocks = tab.find_all('div', 'accordeon-inner__item')
        for block in blocks:
            link, trade_date = parse_link(block)
            if trade_date.year < BREAKPOINT_YEAR:
                return links
            links.append((link, trade_date))
        page_num += 1


def parse_link(block) -> tuple[str, date]:
    """Извлекает ссылку на файл и дату сделки из блока"""
    link_tag = block.find('a', 'xls')
    date_tag = block.find('span')
    href = link_tag['href']

    href = parse.urljoin(BASE_URL, href.split('?')[0])
    trade_date = date_tag.text.strip()
    trade_date_obj = datetime.strptime(trade_date, '%d.%m.%Y')
    return href, trade_date_obj.date()


def download_file(url: str, filename: str) -> None:
    """Скачивает файл"""
    if os.path.exists(filename):
        print(f'Файл {filename} существует. Пропуск...')
        return
    print(f'Скачивание {filename}...')
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as f:
        f.write(response.content)
