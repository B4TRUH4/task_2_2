import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

BASE_URL = 'https://spimex.com'
DOWNLOAD_DIR = 'bulletins'
PAGE_URL = 'https://spimex.com/markets/oil_products/trades/results/?page=page-'

BREAKPOINT_YEAR = 2023

COLUMNS = [
    'код инструмента',
    'наименование инструмента',
    'базис поставки',
    'объем договоров в единицах измерения',
    'обьем договоров, руб.',
    'количество договоров, шт.',
]
