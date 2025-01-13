"""
создать файл зависимостей
pip freeze > requirements.txt
"""

"""
установить пакеты из requirements.txt
pip install -r requirements.txt
"""

"""
alembic
Создание первой миграции
Выполните команду для автоматического создания миграции:
alembic revision --autogenerate -m "Initial migration"
Это создаст файл миграции в папке alembic/versions/
"""

"""
Примените миграцию: alembic upgrade head
После выполнения команды Alembic создаст таблицы, указанные в моделях (categories и products)
"""

"""
Миграция для обновления структуры базы данных:
alembic revision --autogenerate -m "Add description to products"
Alembic создаст файл миграции, содержащий SQL-код для добавления нового поля (description)
Примените миграцию: alembic upgrade head
"""

"""
Откат миграции:
alembic downgrade
Просмотреть текущее состояние базы:
alembic current
"""
