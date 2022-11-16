import abc
from dataclasses import dataclass

import requests

from ..view.card import InterviewCard


class PostRepository(abc.ABC):
    @abc.abstractmethod
    def post(self, card: InterviewCard) -> None:
        pass


@dataclass(frozen=True)
class PrintPostRepository(PostRepository):
    # just for debug
    def post(self, card: InterviewCard) -> None:
        print(card.message, card.users)


@dataclass(frozen=True)
class TeamsPostRepository(PostRepository):
    endpoint: str

    def post(self, card: InterviewCard) -> None:
        body = card.render()
        response: requests.Response = requests.post(self.endpoint, json=body)
        return None
