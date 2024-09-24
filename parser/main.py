import os

from config import DOWNLOAD_DIR
from db_operations import save_trading_results
from download import parse_page, download_file
from processing import read_table


def main():
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
    links = parse_page()
    for link, trade_date in links:
        filename = f'{DOWNLOAD_DIR}/{trade_date}.xls'
        download_file(link, filename)
        df = read_table(filename)
        save_trading_results(df, trade_date)


if __name__ == '__main__':
    main()
