from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("sqlite:///todo.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

class Class_my_db(DeclarativeBase):
    pass


