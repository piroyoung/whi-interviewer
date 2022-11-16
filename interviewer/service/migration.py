from dataclasses import dataclass

from sqlalchemy.engine import Engine

from ..model.orm import Base


@dataclass(frozen=True)
class DatabaseMigration:
    engine: Engine

    def run(self):
        Base.metadata.create_all(bind=self.engine)
        Base.metadata.reflect(bind=self.engine)
