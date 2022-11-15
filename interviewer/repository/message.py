import abc
import random
from dataclasses import dataclass
from typing import List

from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from ..model.orm import Message


class MessageRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_random(self, max_k: int) -> List[Message]:
        raise NotImplementedError()


@dataclass(frozen=True)
class StaticMessageRepository(MessageRepository):
    m: Message

    def get_random(self, max_k: int) -> List[Message]:
        assert max_k > 0
        return [self.m]


@dataclass(frozen=True)
class DatabaseMessageRepository(MessageRepository):
    engine: Engine

    def get_random(self, max_k: int) -> List[Message]:
        with Session(autocommit=True, autoflush=True, bind=self.engine) as session:
            messages: List[Message] = session.query(Message).all()
            return random.sample(messages, k=max_k)
