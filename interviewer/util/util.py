import abc
import functools
import json
import time
import uuid
from logging import Logger
from typing import Callable
from typing import Dict


class Describable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def describe(self) -> Dict:
        raise NotImplementedError()


def observe(logger: Logger):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def decorated(self: Describable, *args, **kwargs):
            l: Logger = logger.getChild(self.__class__.__name__).getChild(func.__name__)
            transaction_id: str = str(uuid.uuid4())
            l.info(json.dumps({
                "transaction_id": transaction_id,
                "type": "start",
                "logged_at": time.time_ns(),
                "name": "{0}.{1}".format(
                    self.__class__.__name__,
                    func.__name__
                ),
                "description": self.describe()
            }))
            try:
                res = func(self, *args, **kwargs)

            finally:
                l.info(json.dumps({
                    "transaction_id": transaction_id,
                    "type": "end",
                    "logged_at": time.time_ns(),
                    "name": "{0}.{1}".format(
                        self.__class__.__name__,
                        func.__name__
                    ),
                    "description": self.describe()
                }))

            return res

        return decorated

    return decorator
