from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer(), primary_key=True, autoincrement=True, unique=True, nullable=False)
    email = Column(Unicode(), nullable=False)
    name = Column(Unicode(), nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)
    is_active = Column(Boolean(), default=True, nullable=False)


class Message(Base):
    __tablename__ = "Messages"
    id = Column(Integer(), primary_key=True, autoincrement=True, unique=True, nullable=False)
    message = Column(Unicode(), nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)
    is_active = Column(Boolean(), default=True, nullable=False)


class Prompt(Base):
    __tablename__ = "Prompts"
    id = Column(Integer(), primary_key=True, autoincrement=True, unique=True, nullable=False)
    system = Column(Unicode(), nullable=False)
    user = Column(Unicode(), nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)
    is_active = Column(Boolean(), default=True, nullable=False)
    assistant_message_logs = relationship("AssistantMessageLog")


class AssistantMessageLog(Base):
    __tablename__ = "AssistantMessageLogs"
    id = Column(Integer(), primary_key=True, autoincrement=True, unique=True, nullable=False)
    prompt_id = Column(Integer(), ForeignKey("Prompts.id"), nullable=False)
    message = Column(Unicode(), nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)
