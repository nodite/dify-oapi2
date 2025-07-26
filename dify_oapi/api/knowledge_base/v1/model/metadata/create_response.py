from __future__ import annotations

from pydantic import BaseModel

from dify_oapi.api.knowledge_base.v1.model.dataset.metadata_info import MetadataInfo


class CreateResponse(BaseModel):
    id: str
    type: str
    name: str

    @staticmethod
    def builder() -> CreateResponseBuilder:
        return CreateResponseBuilder()

    def to_metadata_info(self) -> MetadataInfo:
        return MetadataInfo(id=self.id, type=self.type, name=self.name)


class CreateResponseBuilder:
    def __init__(self):
        self._response = CreateResponse(id="", type="", name="")

    def build(self) -> CreateResponse:
        return self._response

    def id(self, id: str) -> CreateResponseBuilder:
        self._response.id = id
        return self

    def type(self, type: str) -> CreateResponseBuilder:
        self._response.type = type
        return self

    def name(self, name: str) -> CreateResponseBuilder:
        self._response.name = name
        return self