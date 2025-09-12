from dify_oapi.core.model.config import Config

from .resource.audio import Audio
from .resource.feedback import Feedback
from .resource.file import File
from .resource.info import Info


class V1:
    def __init__(self, config: Config):
        self.file: File = File(config)
        self.audio: Audio = Audio(config)
        self.info: Info = Info(config)
        self.feedback: Feedback = Feedback(config)
