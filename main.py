from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
async def root() -> dict:
    return {'message': 'Hello, FastAPI'}


@app.get('/items/{item_id}')
async def read_item(item_id: int) -> dict:
    return {'item_id': item_id, 'name': f'Item {item_id}'}


class Item(BaseModel):
    name: str
    price: float


@app.post('/items/')
async def create_item(item: Item) -> dict:
    return {'name': item.name, 'price': item.price}


@app.put('/items/{item_id')
async def update_item(item_id: int, item: Item) -> dict:
    return {'item_id': item_id, 'name': item.name, 'price': item.price}


@app.delete('/items/{item_id')
async def delete_item(item_id: int) -> dict:
    return {'item_id': item_id, 'message': 'Item deleted'}


@app.post("/products/")
async def create_product():
    """
    Создает новый продукт в системе.
    - **name**: название продукта
    - **price**: цена продукта
    - **quantity**: количество на складе
    """
    return
