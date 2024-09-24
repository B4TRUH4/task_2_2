import datetime
import pandas as pd

from database import get_session
from models import TradingResult


def save_trading_results(df: pd.DataFrame, trade_date: datetime.date) -> None:
    """Сохраняет данные из таблицы в БД"""
    session = get_session()
    for index, row in df.iterrows():
        trading_result = TradingResult(
            exchange_product_id=row['код инструмента'],
            exchange_product_name=row['наименование инструмента'],
            oil_id=row['код инструмента'][:4],
            delivery_basis_id=row['код инструмента'][4:7],
            delivery_basis_name=row['базис поставки'],
            delivery_type_id=row['код инструмента'][-1],
            volume=row['объем договоров в единицах измерения'],
            total=row['обьем договоров, руб.'],
            count=row['количество договоров, шт.'],
            date=trade_date
        )
        session.add(trading_result)
    session.commit()
