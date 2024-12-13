from sqlalchemy import String, Integer, Float, Column, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    descriptions = Column(String, nullable=True)
    cost = Column(Float, index=True)
    quantity = Column(Integer, index=True)
    slug = Column(String, unique=True, index=True)
    # связь с Category
    category_id = Column(Integer, ForeignKey('categories.id'))
    # связь "многие к одному" между таблицами (Product.category отношение к категории продукта)
    category = relationship('Category', back_populates='products')
