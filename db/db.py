from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

import settings

BASE = declarative_base()

engine = create_engine(settings.DB_URL)

def get_session():
    session = sessionmaker(bind=engine)
    return session

