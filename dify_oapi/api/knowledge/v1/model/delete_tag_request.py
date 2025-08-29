from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .delete_tag_request_body import DeleteTagRequestBody


class DeleteTagRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: DeleteTagRequestBody | None = None

    @staticmethod
    def builder() -> "DeleteTagRequestBuilder":
        return DeleteTagRequestBuilder()


class DeleteTagRequestBuilder:
    def __init__(self):
        delete_tag_request = DeleteTagRequest()
        delete_tag_request.http_method = HttpMethod.DELETE
        delete_tag_request.uri = "/v1/datasets/tags"
        self._delete_tag_request = delete_tag_request

    def build(self) -> DeleteTagRequest:
        return self._delete_tag_request

    def request_body(self, request_body: DeleteTagRequestBody) -> "DeleteTagRequestBuilder":
        self._delete_tag_request.request_body = request_body
        self._delete_tag_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
