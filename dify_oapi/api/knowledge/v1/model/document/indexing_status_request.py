from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class IndexingStatusRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.batch: str | None = None

    @staticmethod
    def builder() -> IndexingStatusRequestBuilder:
        return IndexingStatusRequestBuilder()


class IndexingStatusRequestBuilder:
    def __init__(self):
        indexing_status_request = IndexingStatusRequest()
        indexing_status_request.http_method = HttpMethod.GET
        indexing_status_request.uri = "/v1/datasets/:dataset_id/documents/:batch/indexing-status"
        self._indexing_status_request = indexing_status_request

    def build(self) -> IndexingStatusRequest:
        return self._indexing_status_request

    def dataset_id(self, dataset_id: str) -> IndexingStatusRequestBuilder:
        self._indexing_status_request.dataset_id = dataset_id
        self._indexing_status_request.paths["dataset_id"] = dataset_id
        return self

    def batch(self, batch: str) -> IndexingStatusRequestBuilder:
        self._indexing_status_request.batch = batch
        self._indexing_status_request.paths["batch"] = batch
        return self
