from dataclasses import dataclass
from typing import Dict
from typing import List

from user import User


@dataclass(frozen=True)
class Message:
    to_users: List[User]
    body: str

    def __str__(self):
        return self.body

    def as_teams_body(self) -> Dict:
        mention_texts: str = " ".join([f"<at>{user.name}</at>\n" for user in self.to_users])
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
                                "text": f"{mention_texts} {self.body}"
                            }
                        ],
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                        "version": "1.0",
                        "msteams": {
                            "entities": [user.as_teams_mention_entity() for user in self.to_users]
                        }
                    }
                }
            ]
        }
