from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from config import DATABASE_URL

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)


def get_session() -> Session:
    """Возвращает сессию"""
    return Session()


def prepare_database() -> None:
    """Пересоздает таблицы"""
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
