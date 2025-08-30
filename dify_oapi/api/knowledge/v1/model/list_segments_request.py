"""List segments request model."""

from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .knowledge_types import SegmentStatus


class ListSegmentsRequest(BaseRequest):
    """Request model for list segments API."""

    def __init__(self) -> None:
        super().__init__()
        self.dataset_id: str | None = None
        self.document_id: str | None = None

    @staticmethod
    def builder() -> ListSegmentsRequestBuilder:
        return ListSegmentsRequestBuilder()


class ListSegmentsRequestBuilder:
    """Builder for ListSegmentsRequest."""

    def __init__(self) -> None:
        list_segments_request = ListSegmentsRequest()
        list_segments_request.http_method = HttpMethod.GET
        list_segments_request.uri = "/v1/datasets/:dataset_id/documents/:document_id/segments"
        self._list_segments_request = list_segments_request

    def build(self) -> ListSegmentsRequest:
        return self._list_segments_request

    def dataset_id(self, dataset_id: str) -> ListSegmentsRequestBuilder:
        self._list_segments_request.dataset_id = dataset_id
        self._list_segments_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> ListSegmentsRequestBuilder:
        self._list_segments_request.document_id = document_id
        self._list_segments_request.paths["document_id"] = document_id
        return self

    def keyword(self, keyword: str) -> ListSegmentsRequestBuilder:
        self._list_segments_request.add_query("keyword", keyword)
        return self

    def status(self, status: SegmentStatus) -> ListSegmentsRequestBuilder:
        self._list_segments_request.add_query("status", status)
        return self

    def page(self, page: int) -> ListSegmentsRequestBuilder:
        self._list_segments_request.add_query("page", str(page))
        return self

    def limit(self, limit: int) -> ListSegmentsRequestBuilder:
        self._list_segments_request.add_query("limit", str(limit))
        return self
