# добавим зависимость для создания и закрытия сессии при каждом запросе
from sqlalchemy.orm import Session
from fastapi import Depends

from app.backend.db import Session


def get_db(): # get_db используется как зависимость в маршрутах, для получения доступа к базе данных
    db = Session()
    try:
        yield db
    finally:
        db.close()
