import pandas as pd
import numpy as np

from config import COLUMNS


def read_table(filename: str) -> pd.DataFrame:
    """Возвращает таблицу с итогами торгов"""
    df: pd.DataFrame = pd.read_excel(filename)
    # Нахождение начала и конца таблицы
    start_index = df[
        df.iloc[:, 1] == 'Единица измерения: Метрическая тонна'
    ].index[0]
    end_index = df.iloc[start_index:, 1][
        df.iloc[start_index:, 1] == 'Итого:'
    ].index[0]

    new_columns = df.iloc[start_index + 1].replace('\n', ' ', regex=True)
    new_columns = new_columns.str.lower()
    df.columns = new_columns

    df = df.iloc[start_index + 3: end_index, 1:]
    df = df.replace('-', np.nan)
    df = df[COLUMNS]
    df = df.dropna(subset=['количество договоров, шт.'])
    df = df[df['количество договоров, шт.'].astype(int) > 0]
    return df
