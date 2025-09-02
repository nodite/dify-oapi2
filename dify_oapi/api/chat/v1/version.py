from dify_oapi.core.model.config import Config

from .resource import Audio, Chat, Conversation, Feedback, File, Message


class V1:
    def __init__(self, config: Config):
        self.chat: Chat = Chat(config)
        self.file: File = File(config)
        self.feedback: Feedback = Feedback(config)
        self.conversation: Conversation = Conversation(config)
        self.audio: Audio = Audio(config)

        # DEPRECATED: Keep for backward compatibility
        self.message: Message = Message(config)
