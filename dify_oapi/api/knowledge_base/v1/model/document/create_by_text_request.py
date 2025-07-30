from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .create_by_text_request_body import CreateByTextRequestBody


class CreateByTextRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.request_body: CreateByTextRequestBody | None = None

    @staticmethod
    def builder() -> CreateByTextRequestBuilder:
        return CreateByTextRequestBuilder()


class CreateByTextRequestBuilder:
    def __init__(self):
        create_by_text_request = CreateByTextRequest()
        create_by_text_request.http_method = HttpMethod.POST
        create_by_text_request.uri = "/v1/datasets/:dataset_id/document/create-by-text"
        self._create_by_text_request = create_by_text_request

    def build(self) -> CreateByTextRequest:
        return self._create_by_text_request

    def dataset_id(self, dataset_id: str) -> CreateByTextRequestBuilder:
        self._create_by_text_request.dataset_id = dataset_id
        self._create_by_text_request.paths["dataset_id"] = dataset_id
        return self

    def request_body(self, request_body: CreateByTextRequestBody) -> CreateByTextRequestBuilder:
        self._create_by_text_request.request_body = request_body
        self._create_by_text_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
