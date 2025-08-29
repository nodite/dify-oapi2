from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .update_child_chunk_request_body import UpdateChildChunkRequestBody


class UpdateChildChunkRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.document_id: str | None = None
        self.segment_id: str | None = None
        self.child_chunk_id: str | None = None
        self.request_body: UpdateChildChunkRequestBody | None = None

    @staticmethod
    def builder() -> UpdateChildChunkRequestBuilder:
        return UpdateChildChunkRequestBuilder()


class UpdateChildChunkRequestBuilder:
    def __init__(self):
        update_child_chunk_request = UpdateChildChunkRequest()
        update_child_chunk_request.http_method = HttpMethod.PATCH
        update_child_chunk_request.uri = (
            "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks/:child_chunk_id"
        )
        self._update_child_chunk_request = update_child_chunk_request

    def build(self) -> UpdateChildChunkRequest:
        return self._update_child_chunk_request

    def dataset_id(self, dataset_id: str) -> UpdateChildChunkRequestBuilder:
        self._update_child_chunk_request.dataset_id = dataset_id
        self._update_child_chunk_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> UpdateChildChunkRequestBuilder:
        self._update_child_chunk_request.document_id = document_id
        self._update_child_chunk_request.paths["document_id"] = document_id
        return self

    def segment_id(self, segment_id: str) -> UpdateChildChunkRequestBuilder:
        self._update_child_chunk_request.segment_id = segment_id
        self._update_child_chunk_request.paths["segment_id"] = segment_id
        return self

    def child_chunk_id(self, child_chunk_id: str) -> UpdateChildChunkRequestBuilder:
        self._update_child_chunk_request.child_chunk_id = child_chunk_id
        self._update_child_chunk_request.paths["child_chunk_id"] = child_chunk_id
        return self

    def request_body(self, request_body: UpdateChildChunkRequestBody) -> UpdateChildChunkRequestBuilder:
        self._update_child_chunk_request.request_body = request_body
        self._update_child_chunk_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
