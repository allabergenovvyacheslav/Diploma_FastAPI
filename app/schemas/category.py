from pydantic import BaseModel


# Здесь описаны модели данных (schemas) с использованием Pydantic
# Схемы используются для валидации данных, передаваемых в роутеры или возвращаемых из них


class CategoryBase(BaseModel):
    name: str
    slug: str


class CategoryCreate(CategoryBase):
    pass  # id генерируется автоматически, базовые поля наследуются


class Category(CategoryBase):
    id: int  # наследует базовые поля и содержит дополнительные: id

    class Config:
        from_attributes = True  # Позволяет работать с данными ORM
