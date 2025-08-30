from pydantic import BaseModel

from .knowledge_types import TagType


class CreateTagRequestBody(BaseModel):
    name: str | None = None
    type: TagType | None = None

    @staticmethod
    def builder() -> "CreateTagRequestBodyBuilder":
        return CreateTagRequestBodyBuilder()


class CreateTagRequestBodyBuilder:
    def __init__(self):
        self._create_tag_request_body = CreateTagRequestBody()

    def build(self) -> CreateTagRequestBody:
        return self._create_tag_request_body

    def name(self, name: str) -> "CreateTagRequestBodyBuilder":
        self._create_tag_request_body.name = name
        return self

    def type(self, type_value: TagType) -> "CreateTagRequestBodyBuilder":
        self._create_tag_request_body.type = type_value
        return self
