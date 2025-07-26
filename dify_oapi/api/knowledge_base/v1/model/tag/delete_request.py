from __future__ import annotations

from pydantic import BaseModel

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class DeleteTagRequestBody(BaseModel):
    tag_id: str = ""


class DeleteTagRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: DeleteTagRequestBody | None = None

    @staticmethod
    def builder() -> DeleteTagRequestBuilder:
        return DeleteTagRequestBuilder()


class DeleteTagRequestBuilder:
    def __init__(self):
        delete_tag_request = DeleteTagRequest()
        delete_tag_request.http_method = HttpMethod.DELETE
        delete_tag_request.uri = "/v1/datasets/tags"
        self._request = delete_tag_request

    def build(self) -> DeleteTagRequest:
        return self._request

    def tag_id(self, tag_id: str) -> DeleteTagRequestBuilder:
        if self._request.request_body is None:
            self._request.request_body = DeleteTagRequestBody()
        self._request.request_body.tag_id = tag_id
        self._request.body = self._request.request_body.model_dump(exclude_none=True, mode="json")
        return self