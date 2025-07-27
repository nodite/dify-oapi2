from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .retrieve_request_body import RetrieveRequestBody


class RetrieveRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.request_body: RetrieveRequestBody | None = None

    @staticmethod
    def builder() -> RetrieveRequestBuilder:
        return RetrieveRequestBuilder()


class RetrieveRequestBuilder:
    def __init__(self):
        retrieve_request = RetrieveRequest()
        retrieve_request.http_method = HttpMethod.POST
        retrieve_request.uri = "/v1/datasets/:dataset_id/retrieve"
        self._retrieve_request = retrieve_request

    def build(self) -> RetrieveRequest:
        return self._retrieve_request

    def dataset_id(self, dataset_id: str) -> RetrieveRequestBuilder:
        self._retrieve_request.dataset_id = dataset_id
        self._retrieve_request.paths["dataset_id"] = dataset_id
        return self

    def request_body(self, request_body: RetrieveRequestBody) -> RetrieveRequestBuilder:
        self._retrieve_request.request_body = request_body
        self._retrieve_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
