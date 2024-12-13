from fastapi import FastAPI

from app.backend.db import engine, Base
from app.routers import category, products

# Главный файл, в котором запускается приложение и подключаются маршруты
app = FastAPI()

# Подключаем маршруты/роутеров из файлов category.py и products.py
app.include_router(category.router)
app.include_router(products.router)

# Создаём таблицы в базе данных
Base.metadata.create_all(bind=engine)


@app.get('/')
async def welcome() -> dict:
    """Главная страница"""
    return {'message': 'Welcome to the store'}
