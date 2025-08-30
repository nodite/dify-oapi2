"""Get segment request model."""

from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetSegmentRequest(BaseRequest):
    """Request model for get segment API."""

    def __init__(self) -> None:
        super().__init__()
        self.dataset_id: str | None = None
        self.document_id: str | None = None
        self.segment_id: str | None = None

    @staticmethod
    def builder() -> GetSegmentRequestBuilder:
        return GetSegmentRequestBuilder()


class GetSegmentRequestBuilder:
    """Builder for GetSegmentRequest."""

    def __init__(self) -> None:
        get_segment_request = GetSegmentRequest()
        get_segment_request.http_method = HttpMethod.GET
        get_segment_request.uri = "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id"
        self._get_segment_request = get_segment_request

    def build(self) -> GetSegmentRequest:
        return self._get_segment_request

    def dataset_id(self, dataset_id: str) -> GetSegmentRequestBuilder:
        self._get_segment_request.dataset_id = dataset_id
        self._get_segment_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> GetSegmentRequestBuilder:
        self._get_segment_request.document_id = document_id
        self._get_segment_request.paths["document_id"] = document_id
        return self

    def segment_id(self, segment_id: str) -> GetSegmentRequestBuilder:
        self._get_segment_request.segment_id = segment_id
        self._get_segment_request.paths["segment_id"] = segment_id
        return self
