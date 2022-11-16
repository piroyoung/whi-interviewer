from datetime import datetime
from typing import Dict
from typing import List

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer(), primary_key=True, autoincrement=True, unique=True, nullable=False)
    email = Column(String(), nullable=False)
    name = Column(String(), nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)

    def as_teams_mention_entity(self) -> Dict:
        return {
            "type": "mention",
            "text": f"<at>{self.name}</at>",
            "mentioned": {
                "id": self.email,
                "name": self.name
            }
        }


class Message(Base):
    __tablename__ = "Messages"
    id = Column(Integer(), primary_key=True, autoincrement=True, unique=True, nullable=False)
    message = Column(String(), nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)

    def to(self, users: List[User]) -> Dict:
        mention_texts: str = " ".join([f"<at>{user.name}</at>\n\n" for user in users])
        return {
            "type": "message",
            "attachments": [
                {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "content": {
                        "type": "AdaptiveCard",
                        "body": [
                            {
                                "type": "TextBlock",
                                "width": "full",
                                "text": f"{mention_texts} {self.message}"
                            }
                        ],
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                        "version": "1.0",
                        "msteams": {
                            "width": "full",
                            "entities": [user.as_teams_mention_entity() for user in users]
                        }
                    }
                }
            ]
        }
