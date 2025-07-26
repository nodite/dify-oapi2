from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class DeleteMetadataRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.metadata_id: str | None = None

    @staticmethod
    def builder() -> DeleteMetadataRequestBuilder:
        return DeleteMetadataRequestBuilder()


class DeleteMetadataRequestBuilder:
    def __init__(self):
        delete_metadata_request = DeleteMetadataRequest()
        delete_metadata_request.http_method = HttpMethod.DELETE
        delete_metadata_request.uri = "/v1/datasets/:dataset_id/metadata/:metadata_id"
        self._request = delete_metadata_request

    def build(self) -> DeleteMetadataRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> DeleteMetadataRequestBuilder:
        self._request.dataset_id = dataset_id
        self._request.paths["dataset_id"] = dataset_id
        return self

    def metadata_id(self, metadata_id: str) -> DeleteMetadataRequestBuilder:
        self._request.metadata_id = metadata_id
        self._request.paths["metadata_id"] = metadata_id
        return self