import abc
from dataclasses import dataclass
from typing import Dict
from typing import List

from ..model.orm import Message
from ..model.orm import User


class Card(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def render(self) -> Dict:
        pass


@dataclass(frozen=True)
class InterviewCard(Card):
    message: Message
    users: List[User]

    @staticmethod
    def __user_to_mention_entity(user: User) -> Dict:
        return {
            "type": "mention",
            "text": f"<at>{user.name}</at>",
            "mentioned": {
                "id": user.email,
                "name": user.name
            }
        }

    def render(self) -> Dict:
        mention_texts: str = " ".join([f"<at>{user.name}</at>\n\n" for user in self.users])
        entities: List[Dict] = [InterviewCard.__user_to_mention_entity(user) for user in self.users]
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
                                "text": f"{mention_texts} {self.message.message}"
                            }
                        ],
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                        "version": "1.0",
                        "msteams": {
                            "width": "full",
                            "entities": entities
                        }
                    }
                }
            ]
        }


