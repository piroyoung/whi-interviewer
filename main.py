from interviewer.model.environment import Environments
from interviewer.model.message import Message
from interviewer.repository.message import MessageRepository
from interviewer.repository.message import StaticMessageRepository
from interviewer.repository.post import PostRepository
from interviewer.repository.post import TeamsPostRepository

if __name__ == "__main__":
    env: Environments = Environments()
    message_repository: MessageRepository = StaticMessageRepository("What is your favorite food?")
    # post_repository: PostRepository = PrintPostRepository()
    post_repository: PostRepository = TeamsPostRepository(endpoint=env.teams_incoming_webhook)

    message: Message = message_repository.get()
    post_repository.post(message)
