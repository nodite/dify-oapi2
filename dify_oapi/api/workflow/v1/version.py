from dify_oapi.api.dify.v1.resource.audio import Audio
from dify_oapi.api.dify.v1.resource.feedback import Feedback
from dify_oapi.api.dify.v1.resource.file import File
from dify_oapi.api.dify.v1.resource.info import Info
from dify_oapi.core.model.config import Config

from .resource.workflow import Workflow


class V1:
    def __init__(self, config: Config):
        self.workflow = Workflow(config)
        # System APIs - delegate to dify module
        self.file = File(config)
        self.audio = Audio(config)
        self.info = Info(config)
        self.feedback = Feedback(config)
