import abc
import random
from dataclasses import dataclass
from typing import List

from sqlalchemy.orm import Session

from ..model.orm import Message


class MessageRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_random(self, max_k: int) -> List[Message]:
        raise NotImplementedError()


@dataclass(frozen=True)
class StaticMessageRepository(MessageRepository):
    # just for debug
    m: Message

    def get_random(self, max_k: int) -> List[Message]:
        assert max_k > 0
        return [self.m]


@dataclass(frozen=True)
class DatabaseMessageRepository(MessageRepository):
    session: Session

    def get_random(self, max_k: int) -> List[Message]:
        messages: List[Message] = self.session.query(Message).all()
        return random.sample(messages, k=max_k)
