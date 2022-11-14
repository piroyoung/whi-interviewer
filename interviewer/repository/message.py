import abc
from dataclasses import dataclass

from ..model.message import Message


class MessageRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self) -> Message:
        raise NotImplementedError()


@dataclass(frozen=True)
class StaticMessageRepository(MessageRepository):
    m: str

    def get(self) -> Message:
        return Message(self.m)
