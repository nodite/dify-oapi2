from dify_oapi.api.dify.v1.resource.audio import Audio
from dify_oapi.api.dify.v1.resource.feedback import Feedback
from dify_oapi.api.dify.v1.resource.file import File
from dify_oapi.api.dify.v1.resource.info import Info
from dify_oapi.core.model.config import Config

from .resource.annotation import Annotation
from .resource.chatflow import Chatflow
from .resource.conversation import Conversation


class V1:
    def __init__(self, config: Config) -> None:
        # Business-specific APIs
        self.chatflow = Chatflow(config)
        self.conversation = Conversation(config)
        self.annotation = Annotation(config)
        # System APIs - direct use of dify module
        self.file = File(config)
        self.tts = Audio(config)
        self.application = Info(config)
        self.feedback = Feedback(config)
