from dify_oapi.api.dify.v1.resource.audio import Audio
from dify_oapi.api.dify.v1.resource.feedback import Feedback
from dify_oapi.api.dify.v1.resource.file import File
from dify_oapi.api.dify.v1.resource.info import Info
from dify_oapi.core.model.config import Config

from .resource.annotation import Annotation
from .resource.completion import Completion


class V1:
    def __init__(self, config: Config):
        # Business-specific APIs
        self.completion: Completion = Completion(config)
        self.annotation: Annotation = Annotation(config)
        # System APIs - direct use of dify module
        self.file: File = File(config)
        self.audio: Audio = Audio(config)
        self.info: Info = Info(config)
        self.feedback: Feedback = Feedback(config)
