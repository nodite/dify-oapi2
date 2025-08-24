from dify_oapi.core.model.config import Config

from .resource.file import File
from .resource.info import Info
from .resource.log import Log
from .resource.workflow import Workflow


class V1:
    def __init__(self, config: Config):
        self.workflow: Workflow = Workflow(config)
        self.file: File = File(config)
        self.log: Log = Log(config)
        self.info: Info = Info(config)
