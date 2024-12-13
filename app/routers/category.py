from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import Annotated

from app.schemas.category import Category, CategoryCreate
from app.backend.db_depends import get_db

# Annotated для аннотирования зависимостей FastAPI, таких как база данных
DbSession = Annotated[Session, Depends(get_db)]

# Маршруты для категорий
router = APIRouter(prefix='/categories', tags=['Categories'], )


@router.get('/', response_model=list[Category])
async def get_all_categories(db: DbSession):
    """Получить список всех категорий"""

    # возвращает все записи из таблицы categories, все строки из запроса fetchall()
    query = text('SELECT * FROM categories')
    result = db.execute(query).fetchall()
    return [Category(id=row.id, name=row.name, slug=row.slug) for row in result]


@router.post('/create', response_model=Category)
async def create_category(category: CategoryCreate, db: DbSession):
    """Создать новую категорию"""

    # INSERT INTO categories добавляет новую запись в таблицу
    query = text('SELECT * FROM categories (name, slug) VALUES (:name, :slug)')
    db.execute(query, {'name': category.name, 'slug': category.slug})
    db.commit()

    # Возвращаем созданную категорию
    select_query = text('SELECT * FROM categories WHERE name = :name')
    result = db.execute(select_query, {'name': category.name}).fetchone()
    return Category(id=result.id, name=result.name, slug=result.slug)


@router.put('/update', response_model=Category)
async def update_category(category_id: int, category: CategoryCreate, db: DbSession):
    """Обновить категорию"""

    # выполняется SELECT по id, чтобы убедиться, что запись существует
    select_query = text('SELECT * FROM categories WHERE id = :id')
    result = db.execute(select_query, {'id': category_id}).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail='Category not found')

    # UPDATE categories изменяет запись с заданным id
    update_query = text('UPDATE categories SET name = :name, slug = :slug WHERE id = :id')
    db.execute(update_query, {'id': category_id, 'name': category.name, 'slug': category.slug})
    db.commit()

    # выполняется SELECT, чтобы получить обновленные данные
    update_result = db.execute(select_query, {'id': category_id}).fetchone()
    return Category(id=update_result.id, name=update_result.name, slug=update_result.slug)


@router.delete('/delete/{category_id}')
async def delete_category(category_id: int, db: DbSession):
    """Удалить категорию"""

    # проверяем, существует ли категория с данным id
    select_query = text('SELECT * FROM categories WHERE id = :id')
    result = db.execute(select_query, {'id': category_id}).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail='Category not found')

    # удаляет запись с указанным id из таблицы
    delete_query = text('DELETE FROM categories WHERE id = :id')
    db.execute(delete_query, {'id': category_id})
    return {'message': 'Category delete'}
