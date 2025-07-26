from __future__ import annotations

from pydantic import BaseModel

from dify_oapi.api.knowledge_base.v1.model.dataset.tag_info import TagInfo


class UpdateTagResponse(BaseModel):
    id: str
    name: str
    type: str
    binding_count: int

    @staticmethod
    def builder() -> UpdateTagResponseBuilder:
        return UpdateTagResponseBuilder()

    def to_tag_info(self) -> TagInfo:
        return TagInfo(id=self.id, name=self.name, type=self.type, binding_count=self.binding_count)


class UpdateTagResponseBuilder:
    def __init__(self):
        self._response = UpdateTagResponse(id="", name="", type="", binding_count=0)

    def build(self) -> UpdateTagResponse:
        return self._response

    def id(self, id: str) -> UpdateTagResponseBuilder:
        self._response.id = id
        return self

    def name(self, name: str) -> UpdateTagResponseBuilder:
        self._response.name = name
        return self

    def type(self, type: str) -> UpdateTagResponseBuilder:
        self._response.type = type
        return self

    def binding_count(self, binding_count: int) -> UpdateTagResponseBuilder:
        self._response.binding_count = binding_count
        return self