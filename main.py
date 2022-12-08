from logging import Handler
from logging import INFO
from logging import StreamHandler
from logging import basicConfig

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from interviewer.model.environment import Environments
from interviewer.repository.message import DatabaseMessageRepository
from interviewer.repository.message import MessageRepository
from interviewer.repository.post import PostRepository
from interviewer.repository.post import TeamsPostRepository
from interviewer.repository.user import DatabaseUserRepository
from interviewer.repository.user import UserRepository
from interviewer.service.interviewer import InterviewerBatch
from interviewer.service.migration import DatabaseMigration

_h: Handler = StreamHandler()

basicConfig(
    level=INFO,
    handlers=[_h]
)

if __name__ == "__main__":
    env: Environments = Environments()
    engine: Engine = create_engine(f"mssql+pyodbc:///?odbc_connect={env.mssql_connection_string}")
    DatabaseMigration(engine=engine).run()

    with Session(autocommit=True, autoflush=True, bind=engine) as session:
        user_repository: UserRepository = DatabaseUserRepository(session=session)
        message_repository: MessageRepository = DatabaseMessageRepository(session=session)
        post_repository: PostRepository = TeamsPostRepository(endpoint=env.teams_incoming_webhook)

        b: InterviewerBatch = InterviewerBatch(
            user_repository=user_repository,
            message_repository=message_repository,
            post_repository=post_repository,
            n_users=env.number_of_users
        )
        b.run()
