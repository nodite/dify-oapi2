from pydantic import BaseModel


class DeleteTagRequestBody(BaseModel):
    tag_id: str | None = None

    @staticmethod
    def builder() -> "DeleteTagRequestBodyBuilder":
        return DeleteTagRequestBodyBuilder()


class DeleteTagRequestBodyBuilder:
    def __init__(self):
        self._delete_tag_request_body = DeleteTagRequestBody()

    def build(self) -> DeleteTagRequestBody:
        return self._delete_tag_request_body

    def tag_id(self, tag_id: str) -> "DeleteTagRequestBodyBuilder":
        self._delete_tag_request_body.tag_id = tag_id
        return self
