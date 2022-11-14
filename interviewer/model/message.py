from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class Message:
    body: str

    def __str__(self):
        return self.body

    def as_teams_body(self) -> Dict:
        return {
            "text": self.body
        }
