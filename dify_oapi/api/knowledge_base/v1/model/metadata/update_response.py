from __future__ import annotations

from pydantic import BaseModel

from dify_oapi.api.knowledge_base.v1.model.dataset.metadata_info import MetadataInfo


class UpdateResponse(BaseModel):
    id: str
    type: str
    name: str

    @staticmethod
    def builder() -> UpdateResponseBuilder:
        return UpdateResponseBuilder()

    def to_metadata_info(self) -> MetadataInfo:
        return MetadataInfo(id=self.id, type=self.type, name=self.name)


class UpdateResponseBuilder:
    def __init__(self):
        self._response = UpdateResponse(id="", type="", name="")

    def build(self) -> UpdateResponse:
        return self._response

    def id(self, id: str) -> UpdateResponseBuilder:
        self._response.id = id
        return self

    def type(self, type: str) -> UpdateResponseBuilder:
        self._response.type = type
        return self

    def name(self, name: str) -> UpdateResponseBuilder:
        self._response.name = name
        return self