from pydantic import BaseModel


# Здесь описаны модели данных (schemas) с использованием Pydantic


class Product(BaseModel):
    id: int
    name: str
    descriptions: str
    cost: float
    quantity: int
    category_id: int  # Поле для указания, к какой категории относится продукт

    class Config:
        from_attributes = True  # Позволяет преобразовывать данные из объектов базы данных


class ProductCreate(BaseModel):  # Для создания или обновления продукта
    name: str
    descriptions: str
    cost: float
    quantity: int
    category_id: int
