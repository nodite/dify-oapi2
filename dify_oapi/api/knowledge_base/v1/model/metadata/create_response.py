from __future__ import annotations

from pydantic import BaseModel

from dify_oapi.api.knowledge_base.v1.model.dataset.metadata_info import MetadataInfo


class CreateMetadataResponse(BaseModel):
    id: str
    type: str
    name: str

    @staticmethod
    def builder() -> CreateMetadataResponseBuilder:
        return CreateMetadataResponseBuilder()

    def to_metadata_info(self) -> MetadataInfo:
        return MetadataInfo(id=self.id, type=self.type, name=self.name)


class CreateMetadataResponseBuilder:
    def __init__(self):
        self._response = CreateMetadataResponse(id="", type="", name="")

    def build(self) -> CreateMetadataResponse:
        return self._response

    def id(self, id: str) -> CreateMetadataResponseBuilder:
        self._response.id = id
        return self

    def type(self, type: str) -> CreateMetadataResponseBuilder:
        self._response.type = type
        return self

    def name(self, name: str) -> CreateMetadataResponseBuilder:
        self._response.name = name
        return self