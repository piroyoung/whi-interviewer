import abc
from dataclasses import dataclass

import requests

from ..view.card import Card


class PostRepository(abc.ABC):
    @abc.abstractmethod
    def post(self, card: Card) -> None:
        pass


@dataclass(frozen=True)
class PrintPostRepository(PostRepository):
    # just for debug
    def post(self, card: Card) -> None:
        print(card)


@dataclass(frozen=True)
class TeamsPostRepository(PostRepository):
    endpoint: str

    def post(self, card: Card) -> None:
        body = card.render()
        response: requests.Response = requests.post(self.endpoint, json=body)
        return None
