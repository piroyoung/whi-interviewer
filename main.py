from typing import List

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from interviewer.model.environment import Environments
from interviewer.model.orm import Message
from interviewer.model.orm import User
from interviewer.repository.message import DatabaseMessageRepository
from interviewer.repository.message import MessageRepository
from interviewer.repository.post import PostRepository
from interviewer.repository.post import TeamsPostRepository
from interviewer.repository.user import DatabaseUserRepository
from interviewer.repository.user import UserRepository

if __name__ == "__main__":
    env: Environments = Environments()
    engine: Engine = create_engine(f"mssql+pyodbc:///?odbc_connect={env.mssql_connection_string}")

    user_repository: UserRepository = DatabaseUserRepository(engine)
    message_repository: MessageRepository = DatabaseMessageRepository(engine)
    post_repository: PostRepository = TeamsPostRepository(endpoint=env.teams_incoming_webhook)

    users: List[User] = user_repository.get_random(env.number_of_users)
    messages: List[Message] = message_repository.get_random(1)
    post_repository.post(messages[0], users=users)
