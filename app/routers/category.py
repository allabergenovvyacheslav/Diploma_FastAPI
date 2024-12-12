from fastapi import APIRouter, HTTPException
from app.schemas.category import Category, CategoryCreate

# Маршруты для категорий

router = APIRouter(prefix='/categories', tags=['Categories'],)


@router.get('/', response_model=list[Category])
async def get_all_categories():
    """Получить все категории"""
    pass


@router.post('/', response_model=Category)
async def create_category(category: CategoryCreate):
    """Создать новую категорию"""
    pass


@router.put('/{category_id}', response_model=Category)
async def update_category(category_id: int, category: CategoryCreate):
    """Обновить категорию"""
    pass


@router.delete('/{category_id}')
async def delete_category(category_id: int):
    """Удалить категорию"""
    pass