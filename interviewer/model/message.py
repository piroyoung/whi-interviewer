from dataclasses import dataclass


@dataclass(frozen=True)
class Message:
    body: str

    def __str__(self):
        return self.body
