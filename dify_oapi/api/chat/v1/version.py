from dify_oapi.api.dify.v1.resource.audio import Audio
from dify_oapi.api.dify.v1.resource.feedback import Feedback
from dify_oapi.api.dify.v1.resource.file import File
from dify_oapi.api.dify.v1.resource.info import Info
from dify_oapi.core.model.config import Config

from .resource.annotation import Annotation
from .resource.chat import Chat
from .resource.conversation import Conversation
from .resource.message import Message


class V1:
    def __init__(self, config: Config):
        # Business-specific APIs
        self.chat = Chat(config)
        self.conversation = Conversation(config)
        self.annotation = Annotation(config)
        self.message = Message(config)
        # System APIs - direct use of dify module
        self.file = File(config)
        self.audio = Audio(config)
        self.app = Info(config)
        self.feedback = Feedback(config)
