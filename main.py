from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from interviewer.model.environment import Environments
from interviewer.repository.message import DatabaseMessageRepository
from interviewer.repository.message import MessageRepository
from interviewer.repository.post import PostRepository
from interviewer.repository.post import TeamsPostRepository
from interviewer.repository.user import DatabaseUserRepository
from interviewer.repository.user import UserRepository
from interviewer.service.interviewer import InterviewerBatch
from interviewer.service.migration import DatabaseMigration

if __name__ == "__main__":
    env: Environments = Environments()
    engine: Engine = create_engine(f"mssql+pyodbc:///?odbc_connect={env.mssql_connection_string}")

    DatabaseMigration(engine=engine).run()

    user_repository: UserRepository = DatabaseUserRepository(engine=engine)
    message_repository: MessageRepository = DatabaseMessageRepository(engine=engine)
    post_repository: PostRepository = TeamsPostRepository(endpoint=env.teams_incoming_webhook)

    b: InterviewerBatch = InterviewerBatch(
        user_repository=user_repository,
        message_repository=message_repository,
        post_repository=post_repository,
        n_users=env.number_of_users
    )
    b.run()
