from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class ListMetadataRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None

    @staticmethod
    def builder() -> ListMetadataRequestBuilder:
        return ListMetadataRequestBuilder()


class ListMetadataRequestBuilder:
    def __init__(self):
        list_metadata_request = ListMetadataRequest()
        list_metadata_request.http_method = HttpMethod.GET
        list_metadata_request.uri = "/v1/datasets/:dataset_id/metadata"
        self._request = list_metadata_request

    def build(self) -> ListMetadataRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> ListMetadataRequestBuilder:
        self._request.dataset_id = dataset_id
        self._request.paths["dataset_id"] = dataset_id
        return self