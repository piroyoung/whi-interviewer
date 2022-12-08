import abc
import random
from dataclasses import dataclass
from logging import Logger
from logging import getLogger
from typing import Dict
from typing import List

from sqlalchemy.orm import Session

from ..model.orm import User
from ..util import Describable
from ..util import observe

_logger: Logger = getLogger(__name__)


class UserRepository(Describable):
    @abc.abstractmethod
    def get_random(self, max_k: int) -> List[User]:
        raise NotImplementedError()


@dataclass(frozen=True)
class DatabaseUserRepository(UserRepository):
    session: Session

    def describe(self) -> Dict:
        return {}

    @observe(logger=_logger)
    def get_random(self, max_k: int) -> List[User]:
        messages: List[User] = self.session.query(User).all()
        return random.sample(messages, k=max_k)
