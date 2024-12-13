from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship
from app.backend.db import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    slug = Column(String, unique=True, index=True)
    # отношение "один ко многим" между таблицами (Category.products список продуктов, связанных с категорией)
    products = relationship('Product', back_populates='category')
