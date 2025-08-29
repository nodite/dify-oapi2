"""Get batch indexing status request model."""

from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetBatchIndexingStatusRequest(BaseRequest):
    """Request model for get batch indexing status API."""

    def __init__(self) -> None:
        super().__init__()
        self.dataset_id: str | None = None
        self.batch: str | None = None

    @staticmethod
    def builder() -> GetBatchIndexingStatusRequestBuilder:
        return GetBatchIndexingStatusRequestBuilder()


class GetBatchIndexingStatusRequestBuilder:
    """Builder for GetBatchIndexingStatusRequest."""

    def __init__(self) -> None:
        get_batch_indexing_status_request = GetBatchIndexingStatusRequest()
        get_batch_indexing_status_request.http_method = HttpMethod.GET
        get_batch_indexing_status_request.uri = "/v1/datasets/:dataset_id/documents/:batch/indexing-status"
        self._get_batch_indexing_status_request = get_batch_indexing_status_request

    def build(self) -> GetBatchIndexingStatusRequest:
        return self._get_batch_indexing_status_request

    def dataset_id(self, dataset_id: str) -> GetBatchIndexingStatusRequestBuilder:
        self._get_batch_indexing_status_request.dataset_id = dataset_id
        self._get_batch_indexing_status_request.paths["dataset_id"] = dataset_id
        return self

    def batch(self, batch: str) -> GetBatchIndexingStatusRequestBuilder:
        self._get_batch_indexing_status_request.batch = batch
        self._get_batch_indexing_status_request.paths["batch"] = batch
        return self
