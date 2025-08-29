"""Delete child chunk request model."""

from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class DeleteChildChunkRequest(BaseRequest):
    """Request model for delete child chunk API."""

    def __init__(self) -> None:
        super().__init__()
        self.dataset_id: str | None = None
        self.document_id: str | None = None
        self.segment_id: str | None = None
        self.child_chunk_id: str | None = None

    @staticmethod
    def builder() -> DeleteChildChunkRequestBuilder:
        return DeleteChildChunkRequestBuilder()


class DeleteChildChunkRequestBuilder:
    """Builder for DeleteChildChunkRequest."""

    def __init__(self) -> None:
        delete_child_chunk_request = DeleteChildChunkRequest()
        delete_child_chunk_request.http_method = HttpMethod.DELETE
        delete_child_chunk_request.uri = (
            "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks/:child_chunk_id"
        )
        self._delete_child_chunk_request = delete_child_chunk_request

    def build(self) -> DeleteChildChunkRequest:
        return self._delete_child_chunk_request

    def dataset_id(self, dataset_id: str) -> DeleteChildChunkRequestBuilder:
        self._delete_child_chunk_request.dataset_id = dataset_id
        self._delete_child_chunk_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> DeleteChildChunkRequestBuilder:
        self._delete_child_chunk_request.document_id = document_id
        self._delete_child_chunk_request.paths["document_id"] = document_id
        return self

    def segment_id(self, segment_id: str) -> DeleteChildChunkRequestBuilder:
        self._delete_child_chunk_request.segment_id = segment_id
        self._delete_child_chunk_request.paths["segment_id"] = segment_id
        return self

    def child_chunk_id(self, child_chunk_id: str) -> DeleteChildChunkRequestBuilder:
        self._delete_child_chunk_request.child_chunk_id = child_chunk_id
        self._delete_child_chunk_request.paths["child_chunk_id"] = child_chunk_id
        return self
