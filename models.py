# models.py
import datetime
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"
    id = Column(String, primary_key=True)
    prompt = Column(Text)
    project_type = Column(String)
    language = Column(String)
    files = Column(Text)  # Serialized file dictionary

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    id = Column(String, primary_key=True)
    project_id = Column(String)
    sender = Column(String)  # "user" or "assistant"
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(String, primary_key=True)
    project_id = Column(String)
    message = Column(Text)
    rating = Column(String)  # e.g., "positive", "negative"
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
