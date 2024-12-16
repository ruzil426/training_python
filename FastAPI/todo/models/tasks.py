from todo.backend.db import Class_my_db
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Time
from sqlalchemy.orm import relationship
from datetime import datetime

class Task(Class_my_db):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    name = Column(String)
    due_date = Column(DateTime)
    lead_time = Column(Time)
    # check_mark = Column(Boolean, default=False)
    slug = Column(String, unique=True, index=True)
    subtask = relationship('Subtask', back_populates='tasks')

# from sqlalchemy.schema import CreateTable
# print(CreateTable(Task.__table__))
