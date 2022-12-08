from dataclasses import dataclass
from logging import Logger
from logging import getLogger
from typing import Dict
from typing import List

from ..model.orm import Message
from ..model.orm import User
from ..repository.message import MessageRepository
from ..repository.post import PostRepository
from ..repository.user import UserRepository
from ..util import Describable
from ..util import observe
from ..view.card import Card
from ..view.card import InterviewCard

_logger: Logger = getLogger(__name__)


@dataclass(frozen=True)
class InterviewerBatch(Describable):
    user_repository: UserRepository
    message_repository: MessageRepository
    post_repository: PostRepository
    n_users: int

    def describe(self) -> Dict:
        return {"n_users": self.n_users}

    @observe(logger=_logger)
    def run(self) -> None:
        users: List[User] = self.user_repository.get_random(self.n_users)
        messages: List[Message] = self.message_repository.get_random(1)
        card: Card = InterviewCard(message=messages[0], users=users)
        self.post_repository.post(card)
