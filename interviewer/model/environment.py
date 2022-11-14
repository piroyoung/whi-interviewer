import os
from dataclasses import dataclass


class Environments:
    @property
    def teams_incoming_webhook(self) -> str:
        tiw: str = os.environ.get("TEAMS_INCOMING_WEBHOOK")
        assert tiw
        return tiw
