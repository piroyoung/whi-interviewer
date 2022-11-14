from interviewer.model.environment import Environments
from interviewer.model.message import Message
from interviewer.model.user import User
from interviewer.repository.message import MessageRepository
from interviewer.repository.message import StaticMessageRepository
from interviewer.repository.post import PostRepository
from interviewer.repository.post import TeamsPostRepository

if __name__ == "__main__":
    foo: User = User(email="foo@microsoft.com", name="foo")
    bar: User = User(email="bar@microsoft.com", name="bar")
    baz: User = User(email="baz@microsoft.com", name="baz")

    message: Message = Message(to_users=[foo, bar, baz], body="What is your favorite food?")
    env: Environments = Environments()
    message_repository: MessageRepository = StaticMessageRepository(message)
    # post_repository: PostRepository = PrintPostRepository()
    post_repository: PostRepository = TeamsPostRepository(endpoint=env.teams_incoming_webhook)

    message: Message = message_repository.get()
    post_repository.post(message)
