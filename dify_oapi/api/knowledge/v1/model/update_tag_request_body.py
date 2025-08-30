from pydantic import BaseModel


class UpdateTagRequestBody(BaseModel):
    tag_id: str | None = None
    name: str | None = None

    @staticmethod
    def builder() -> "UpdateTagRequestBodyBuilder":
        return UpdateTagRequestBodyBuilder()


class UpdateTagRequestBodyBuilder:
    def __init__(self):
        self._update_tag_request_body = UpdateTagRequestBody()

    def build(self) -> UpdateTagRequestBody:
        return self._update_tag_request_body

    def tag_id(self, tag_id: str) -> "UpdateTagRequestBodyBuilder":
        self._update_tag_request_body.tag_id = tag_id
        return self

    def name(self, name: str) -> "UpdateTagRequestBodyBuilder":
        self._update_tag_request_body.name = name
        return self
