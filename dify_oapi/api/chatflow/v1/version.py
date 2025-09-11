from dify_oapi.core.model.config import Config

from .resource.annotation import Annotation
from .resource.application import Application
from .resource.chatflow import Chatflow
from .resource.conversation import Conversation
from .resource.feedback import Feedback
from .resource.file import File
from .resource.tts import TTS


class V1:
    def __init__(self, config: Config) -> None:
        self.chatflow = Chatflow(config)
        self.file = File(config)
        self.feedback = Feedback(config)
        self.conversation = Conversation(config)
        self.tts = TTS(config)
        self.application = Application(config)
        self.annotation = Annotation(config)
