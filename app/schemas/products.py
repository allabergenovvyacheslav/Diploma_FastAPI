from pydantic import BaseModel, ConfigDict


# Здесь описаны модели данных (schemas) с использованием Pydantic
# Схемы используются для валидации данных, передаваемых в роутеры или возвращаемых из них


class ProductBase(BaseModel):
    name: str
    descriptions: str
    cost: float
    slug: str
    quantity: int
    category_id: int  # Поле для указания, к какой категории относится продукт


class ProductCreate(ProductBase):  # Для создания или обновления продукта, базовые поля наследуются
    pass # id генерируется автоматически (наследует базовые поля)


class Product(ProductBase):
    id: int # наследует базовые поля и содержит дополнительные поля: id

    class Config:
        from_attributes = True  # Позволяет работать с данными ORM
