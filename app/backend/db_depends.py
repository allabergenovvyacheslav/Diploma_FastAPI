# добавим зависимость для создания и закрытия сессии при каждом запросе
from sqlalchemy.orm import Session
from fastapi import Depends

from app.backend.db import SessionLocal


# get_db используется как зависимость в маршрутах, для получения доступа к базе данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
