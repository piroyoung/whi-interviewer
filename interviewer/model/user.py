from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class User:
    email: str
    name: str

    def as_teams_mention_entity(self) -> Dict:
        return {
            "type": "mention",
            "text": f"<at>{self.name}</at>",
            "mentioned": {
                "id": self.email,
                "name": self.name
            }
        }
