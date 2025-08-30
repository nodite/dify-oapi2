from dify_oapi.core.model.config import Config

from .resource.workflow import Workflow


class V1:
    def __init__(self, config: Config):
        self.workflow = Workflow(config)
