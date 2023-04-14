import abc
import random
from dataclasses import asdict
from dataclasses import dataclass
from logging import Logger
from logging import getLogger
from typing import List, Dict

import openai
from sqlalchemy.orm import Session

from ..model.orm import Message, Prompt
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


@dataclass(frozen=True)
class OpenAIMessageRepository(MessageRepository):
    session: Session
    api_type: str
    api_key: str
    api_base: str
    api_version: str
    model_name: str

    def describe(self) -> Dict:
        return asdict(self)

    @observe(logger=_logger)
    def get(self) -> Message:
        openai.api_key = self.api_key
        openai.api_type = self.api_type
        openai.api_base = self.api_base
        openai.api_version = self.api_version
        prompts: List[Prompt] = self.session.query(Prompt).all()
        prompt: Prompt = random.sample(prompts, k=1)[0]

        prompts = [
            {
                "role": "system",
                "content": prompt.system
            },
            {
                "role": "user",
                "content": prompt.user
            }
        ]

        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=prompts
        )
        # just for debug
        print(type(response))
        return Message(message=response.choices[0].message.content)
