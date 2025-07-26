from __future__ import annotations

from pydantic import BaseModel

from dify_oapi.api.knowledge_base.v1.model.dataset.tag_info import TagInfo


class UpdateResponse(BaseModel):
    id: str
    name: str
    type: str
    binding_count: int

    @staticmethod
    def builder() -> UpdateResponseBuilder:
        return UpdateResponseBuilder()

    def to_tag_info(self) -> TagInfo:
        return TagInfo(id=self.id, name=self.name, type=self.type, binding_count=self.binding_count)


class UpdateResponseBuilder:
    def __init__(self):
        self._response = UpdateResponse(id="", name="", type="", binding_count=0)

    def build(self) -> UpdateResponse:
        return self._response

    def id(self, id: str) -> UpdateResponseBuilder:
        self._response.id = id
        return self

    def name(self, name: str) -> UpdateResponseBuilder:
        self._response.name = name
        return self

    def type(self, type: str) -> UpdateResponseBuilder:
        self._response.type = type
        return self

    def binding_count(self, binding_count: int) -> UpdateResponseBuilder:
        self._response.binding_count = binding_count
        return self