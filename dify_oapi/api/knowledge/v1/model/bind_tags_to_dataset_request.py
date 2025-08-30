from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .bind_tags_to_dataset_request_body import BindTagsToDatasetRequestBody


class BindTagsToDatasetRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: BindTagsToDatasetRequestBody | None = None

    @staticmethod
    def builder() -> "BindTagsToDatasetRequestBuilder":
        return BindTagsToDatasetRequestBuilder()


class BindTagsToDatasetRequestBuilder:
    def __init__(self):
        bind_tags_to_dataset_request = BindTagsToDatasetRequest()
        bind_tags_to_dataset_request.http_method = HttpMethod.POST
        bind_tags_to_dataset_request.uri = "/v1/datasets/tags/binding"
        self._bind_tags_to_dataset_request = bind_tags_to_dataset_request

    def build(self) -> BindTagsToDatasetRequest:
        return self._bind_tags_to_dataset_request

    def request_body(self, request_body: BindTagsToDatasetRequestBody) -> "BindTagsToDatasetRequestBuilder":
        self._bind_tags_to_dataset_request.request_body = request_body
        self._bind_tags_to_dataset_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
