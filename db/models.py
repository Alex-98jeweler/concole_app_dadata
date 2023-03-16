from sqlalchemy import Column, Integer, String

from db.db import BASE

class Settings(BASE):

    __tablename__ = 'settings'

    id = Column('id', Integer, primary_key=True)
    token = Column('token', String(200))
    language = Column('language', String(2))
    secret = Column('secret', String(200))

