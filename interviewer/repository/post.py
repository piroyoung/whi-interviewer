import abc
from dataclasses import dataclass

import requests

from ..model.message import Message


class PostRepository(abc.ABC):
    @abc.abstractmethod
    def post(self, m: Message) -> None:
        pass


@dataclass(frozen=True)
class PrintPostRepository(PostRepository):
    # just for debug
    def post(self, m: Message) -> None:
        print(m)


@dataclass(frozen=True)
class TeamsPostRepository(PostRepository):
    endpoint: str

    def post(self, m: Message) -> None:
        requests.post(self.endpoint, json=m.as_teams_body())
        return None
