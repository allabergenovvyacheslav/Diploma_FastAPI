from fastapi import APIRouter, HTTPException
from app.schemas.products import Product, ProductCreate


router = APIRouter(prefix='/products', tags=['Products'],)


@router.get('/', response_model=list[Product])
async def get_all_products():
    """Получить все продукты"""
    pass


@router.post('/', response_model=Product)
async def create_product(product: ProductCreate):
    """Создать продукт"""
    pass


@router.put('/{product_id}', response_model=ProductCreate)
async def update_product(product_id: int, product: ProductCreate):
    """Обновить продукт"""
    pass


@router.delete('/{product_id}')
async def delete_product(product_id: int):
    """Удалить продукт"""
    pass
