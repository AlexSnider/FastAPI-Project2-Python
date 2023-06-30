from sqlalchemy import Column, Integer, String
from app.db.base import base

class Category(base):
    __tablename__= 'categorias'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    slug = Column('slug', String, nullable=False)
