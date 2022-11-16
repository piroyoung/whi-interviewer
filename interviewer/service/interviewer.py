from dataclasses import dataclass
from typing import List

from ..model.orm import Message
from ..model.orm import User
from ..repository.message import MessageRepository
from ..repository.post import PostRepository
from ..repository.user import UserRepository
from ..view.card import Card
from ..view.card import InterviewCard


@dataclass(frozen=True)
class InterviewerBatch:
    user_repository: UserRepository
    message_repository: MessageRepository
    post_repository: PostRepository
    n_users: int

    def run(self) -> None:
        users: List[User] = self.user_repository.get_random(self.n_users)
        messages: List[Message] = self.message_repository.get_random(1)
        card: Card = InterviewCard(message=messages[0], users=users)
        self.post_repository.post(card)
