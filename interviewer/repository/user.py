import abc
import random
from dataclasses import dataclass
from typing import List

from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from ..model.orm import User


class UserRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_random(self, max_k: int) -> List[User]:
        raise NotImplementedError()


@dataclass(frozen=True)
class DatabaseUserRepository(UserRepository):
    engine: Engine

    def get_random(self, max_k: int) -> List[User]:
        with Session(autocommit=True, autoflush=True, bind=self.engine) as session:
            messages: List[User] = session.query(User).all()
            return random.sample(messages, k=max_k)
