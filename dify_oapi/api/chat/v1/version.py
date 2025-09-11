from dify_oapi.core.model.config import Config

from .resource.annotation import Annotation
from .resource.app import App
from .resource.audio import Audio
from .resource.chat import Chat
from .resource.conversation import Conversation
from .resource.feedback import Feedback
from .resource.file import File
from .resource.message import Message


class V1:
    def __init__(self, config: Config):
        self.chat = Chat(config)
        self.file = File(config)
        self.feedback = Feedback(config)
        self.conversation = Conversation(config)
        self.audio = Audio(config)
        self.app = App(config)
        self.annotation = Annotation(config)
        self.message = Message(config)
