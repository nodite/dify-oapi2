from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class ListRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None

    @staticmethod
    def builder() -> ListRequestBuilder:
        return ListRequestBuilder()


class ListRequestBuilder:
    def __init__(self):
        list_request = ListRequest()
        list_request.http_method = HttpMethod.GET
        list_request.uri = "/v1/datasets/:dataset_id/metadata"
        self._list_request = list_request

    def build(self) -> ListRequest:
        return self._list_request

    def dataset_id(self, dataset_id: str) -> ListRequestBuilder:
        self._list_request.dataset_id = dataset_id
        self._list_request.paths["dataset_id"] = dataset_id
        return self
