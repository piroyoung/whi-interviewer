import abc
from dataclasses import dataclass
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
