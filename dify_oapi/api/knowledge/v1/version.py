from dify_oapi.core.model.config import Config

from .resource.chunk import Chunk
from .resource.dataset import Dataset
from .resource.document import Document
from .resource.model import Model
from .resource.segment import Segment
from .resource.tag import Tag


class V1:
    def __init__(self, config: Config):
        self.dataset = Dataset(config)
        self.document = Document(config)
        self.segment = Segment(config)
        self.chunk = Chunk(config)
        self.tag = Tag(config)
        self.model = Model(config)
