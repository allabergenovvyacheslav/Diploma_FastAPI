from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'sqlite:///./shop_db' # Путь к базе данных SQLite

# движок для подключения к базе данных. check_same_thread = False проверка_одного_потока
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

# сессии для работы с БД, autoflush запись изменений в БД, bind привязка к движку, autocommit автозакрытие транзакции
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base базовый класс для всех моделей (наследодатель)
Base = declarative_base()