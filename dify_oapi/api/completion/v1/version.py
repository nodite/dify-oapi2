from dify_oapi.core.model.config import Config

from .resource.annotation import Annotation
from .resource.audio import Audio
from .resource.completion import Completion
from .resource.feedback import Feedback
from .resource.file import File
from .resource.info import Info


class V1:
    def __init__(self, config: Config):
        self.completion: Completion = Completion(config)
        self.file: File = File(config)
        self.feedback: Feedback = Feedback(config)
        self.audio: Audio = Audio(config)
        self.info: Info = Info(config)
        self.annotation: Annotation = Annotation(config)
