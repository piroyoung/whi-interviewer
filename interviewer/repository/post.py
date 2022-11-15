import abc
from dataclasses import dataclass
from typing import List

import requests

from ..model.orm import Message
from ..model.orm import User


class PostRepository(abc.ABC):
    @abc.abstractmethod
    def post(self, message: Message, users: List[User]) -> None:
        pass


@dataclass(frozen=True)
class PrintPostRepository(PostRepository):
    # just for debug
    def post(self, message: Message, users: List[User]) -> None:
        print(message, users)


@dataclass(frozen=True)
class TeamsPostRepository(PostRepository):
    endpoint: str

    def post(self, message: Message, users: List[User]) -> None:
        body = message.to(users)
        response: requests.Response = requests.post(self.endpoint, json=body)
        return None
