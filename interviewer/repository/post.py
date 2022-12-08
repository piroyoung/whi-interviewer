import abc
from dataclasses import asdict
from dataclasses import dataclass
from logging import Logger
from logging import getLogger
from typing import Dict

import requests

from ..util import Describable
from ..util import observe
from ..view.card import Card

_logger: Logger = getLogger(__name__)


class PostRepository(Describable):
    @abc.abstractmethod
    def post(self, card: Card) -> None:
        pass


@dataclass(frozen=True)
class PrintPostRepository(PostRepository):
    # just for debug

    def describe(self) -> Dict:
        return asdict(self)

    @observe(logger=_logger)
    def post(self, card: Card) -> None:
        print(card)


@dataclass(frozen=True)
class TeamsPostRepository(PostRepository):
    endpoint: str

    def describe(self) -> Dict:
        return asdict(self)

    @observe(logger=_logger)
    def post(self, card: Card) -> None:
        body = card.render()
        response: requests.Response = requests.post(self.endpoint, json=body)
        return None
