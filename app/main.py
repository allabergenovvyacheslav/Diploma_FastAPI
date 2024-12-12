from fastapi import FastAPI

from app.routers import category, products

app = FastAPI()

# Главный файл, в котором запускается приложение и подключаются маршруты


# Подключаем маршруты из файлов category.py и products.py
app.include_router(category.router)
app.include_router(products.router)


@app.get('/')
async def welcome() -> dict:
    """Главная страница"""
    return {'message': 'Welcome to the store'}
