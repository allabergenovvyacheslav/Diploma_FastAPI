from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import Annotated

from app.schemas.products import Product, ProductCreate
from app.backend.db_depends import get_db

router = APIRouter(prefix='/products', tags=['Products'], )

# Annotated для аннотирования зависимостей FastAPI, таких как база данных
DbSession = Annotated[Session, Depends(get_db)]


@router.get('/', response_model=list[Product])
async def get_all_products(db: DbSession):
    """Получить список всех продукты"""

    # выбирает все записи из таблицы продуктов
    query = text('SELECT * FROM products')
    result = db.execute(query).fetchall()

    # объект Product для формирования ответа
    return [
        Product(
            id=row.id,
            name=row.name,
            descriptions=row.descriptions,
            cost=row.cost,
            quantity=row.quantity,
            slug=row.slug,
            category_id=row.category_id
        ) for row in result
    ]


@router.post('/create', response_model=Product)
async def create_product(product: ProductCreate, db: DbSession):
    """Создать продукт"""

    # INSERT INTO products, который добавляет новый продукт
    query = text('INSERT INTO products (name, descriptions, cost, quantity, slug, category_id)'
                 'VALUES (:name, :descriptions, :cost, :quantity, :slug, :category_id')
    db.execute(query,
               {'name': product.name,
                'descriptions': product.descriptions,
                'cost': product.cost,
                'quantity': product.quantity,
                'slug': product.slug,
                'category_id': product.category_id},
               )
    db.commit()

    # дополнительный запрос SELECT, чтобы вернуть данные добавленного продукта
    select_query = text('SELECT * FROM products WHERE name = :name AND slug = :slug')
    result = db.execute(select_query,
                        {'name': product.name, 'slug': product.slug}).fetchone()
    return Product(id=result.id,
                   name=result.name,
                   descriptions=result.descriptions,
                   cost=result.cost,
                   quantity=result.quantity,
                   slug=result.slug,
                   category_id=result.category_id)



@router.put('/update', response_model=ProductCreate)
async def update_product(product_id: int, product: ProductCreate, db: DbSession):
    """Обновить продукт"""

    # SELECT, чтобы убедиться, что продукт существует
    select_query = text('SELECT * FROM products WHERE id = :id')
    result = db.execute(select_query, {'id': product_id}).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail='Products not found')

    # UPDATE products обновляет запись с указанным id
    update_query = text(
        'UPDATE products SET name = :name, descriptions = :descriptions, cost = :cost,'
        'quantity = :quantity, slug = :slug, category_id = :category_id WHERE id = :id'
    )
    db.execute(update_query,
               {'id': product_id,
                'name': product.name,
                'descriptions': product.descriptions,
                'cost': product.cost,
                'quantity': product.quantity,
                'slug': product.slug,
                'category_id': product.category_id},
               )
    db.commit()

    # Возвращаем обновленные данные после повторного SELECT
    update_result = db.execute(select_query, {'id': product_id}).fetchone()
    return Product(id=update_result.id,
                   name=update_result.name,
                   descriptions=update_result.descriptions,
                   cost=update_result.cost,
                   quantity=update_result.quantity,
                   slug=update_result.slug,
                   category_id=update_result.category_id)


@router.delete('/delete/{product_id}')
async def delete_product(product_id: int, db: DbSession):
    """Удалить продукт"""

    # проверяется существование продукта в базе
    select_query = text('SELECT * FROM products WHERE id = :id')
    result = db.execute(select_query, {'id': product_id}).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail='Products not found')

    # запрос DELETE FROM products и возвращается сообщение Product deleted
    delete_query = text('DELETE FROM products WHERE id = :id')
    db.execute(delete_query, {'id': product_id})
    db.commit()
    return {'message': 'Product deleted'}
