import abc
import random
from dataclasses import asdict
from dataclasses import dataclass
from logging import Logger
from logging import getLogger
from typing import List, Dict

from sqlalchemy.orm import Session

from ..model.orm import Message
from ..util import Describable
from ..util import observe

_logger: Logger = getLogger(__name__)


class MessageRepository(Describable):
    @abc.abstractmethod
    def get(self) -> Message:
        raise NotImplementedError()


@dataclass(frozen=True)
class StaticMessageRepository(MessageRepository):
    # just for debug
    m: Message

    def describe(self) -> Dict:
        return asdict(self)

    @observe(logger=_logger)
    def get(self) -> Message:
        return self.m


@dataclass(frozen=True)
class DatabaseMessageRepository(MessageRepository):
    session: Session

    def describe(self) -> Dict:
        return {}

    @observe(logger=_logger)
    def get(self) -> Message:
        messages: List[Message] = self.session.query(Message).all()
        return random.sample(messages, k=1)[0]
