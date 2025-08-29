from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .unbind_tags_from_dataset_request_body import UnbindTagsFromDatasetRequestBody


class UnbindTagsFromDatasetRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: UnbindTagsFromDatasetRequestBody | None = None

    @staticmethod
    def builder() -> "UnbindTagsFromDatasetRequestBuilder":
        return UnbindTagsFromDatasetRequestBuilder()


class UnbindTagsFromDatasetRequestBuilder:
    def __init__(self):
        unbind_tags_from_dataset_request = UnbindTagsFromDatasetRequest()
        unbind_tags_from_dataset_request.http_method = HttpMethod.POST
        unbind_tags_from_dataset_request.uri = "/v1/datasets/tags/unbinding"
        self._unbind_tags_from_dataset_request = unbind_tags_from_dataset_request

    def build(self) -> UnbindTagsFromDatasetRequest:
        return self._unbind_tags_from_dataset_request

    def request_body(self, request_body: UnbindTagsFromDatasetRequestBody) -> "UnbindTagsFromDatasetRequestBuilder":
        self._unbind_tags_from_dataset_request.request_body = request_body
        self._unbind_tags_from_dataset_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
