import os
from dataclasses import dataclass


class Environments:
    @property
    def teams_incoming_webhook(self) -> str:
        tiw: str = os.environ.get("TEAMS_INCOMING_WEBHOOK")
        return "" if tiw is None else tiw
