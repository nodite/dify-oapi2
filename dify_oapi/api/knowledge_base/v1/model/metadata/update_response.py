from __future__ import annotations

from pydantic import BaseModel

from dify_oapi.api.knowledge_base.v1.model.dataset.metadata_info import MetadataInfo


class UpdateMetadataResponse(BaseModel):
    id: str
    type: str
    name: str

    @staticmethod
    def builder() -> UpdateMetadataResponseBuilder:
        return UpdateMetadataResponseBuilder()

    def to_metadata_info(self) -> MetadataInfo:
        return MetadataInfo(id=self.id, type=self.type, name=self.name)


class UpdateMetadataResponseBuilder:
    def __init__(self):
        self._response = UpdateMetadataResponse(id="", type="", name="")

    def build(self) -> UpdateMetadataResponse:
        return self._response

    def id(self, id: str) -> UpdateMetadataResponseBuilder:
        self._response.id = id
        return self

    def type(self, type: str) -> UpdateMetadataResponseBuilder:
        self._response.type = type
        return self

    def name(self, name: str) -> UpdateMetadataResponseBuilder:
        self._response.name = name
        return self