from pydantic import BaseModel


# Здесь описаны модели данных (schemas) с использованием Pydantic


class Category(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True  # Позволяет преобразовывать данные из объектов базы данных


class CategoryCreate(BaseModel):
    name: str  # id генерируется автоматически
