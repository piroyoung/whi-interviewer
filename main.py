from interviewer.repository.message import MessageRepository
from interviewer.repository.message import StaticMessageRepository
from interviewer.model.message import Message
from interviewer.repository.post import PostRepository
from interviewer.repository.post import PrintPostRepository

if __name__ == "__main__":
    message_repository: MessageRepository = StaticMessageRepository("What is your favorite food?")
    post_repository: PostRepository = PrintPostRepository()

    message: Message = message_repository.get()
    post_repository.post(message)



