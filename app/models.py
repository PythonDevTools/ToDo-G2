import datetime
from sqlalchemy import Column, Boolean, Integer, String, DateTime
from .db import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    done = Column(Boolean, default=False)
    due = Column(DateTime, default=datetime.datetime.utcnow)