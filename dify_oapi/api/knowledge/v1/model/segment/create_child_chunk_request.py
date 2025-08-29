from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .create_child_chunk_request_body import CreateChildChunkRequestBody


class CreateChildChunkRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.document_id: str | None = None
        self.segment_id: str | None = None
        self.request_body: CreateChildChunkRequestBody | None = None

    @staticmethod
    def builder() -> CreateChildChunkRequestBuilder:
        return CreateChildChunkRequestBuilder()


class CreateChildChunkRequestBuilder:
    def __init__(self):
        create_child_chunk_request = CreateChildChunkRequest()
        create_child_chunk_request.http_method = HttpMethod.POST
        create_child_chunk_request.uri = (
            "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks"
        )
        self._create_child_chunk_request = create_child_chunk_request

    def build(self) -> CreateChildChunkRequest:
        return self._create_child_chunk_request

    def dataset_id(self, dataset_id: str) -> CreateChildChunkRequestBuilder:
        self._create_child_chunk_request.dataset_id = dataset_id
        self._create_child_chunk_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> CreateChildChunkRequestBuilder:
        self._create_child_chunk_request.document_id = document_id
        self._create_child_chunk_request.paths["document_id"] = document_id
        return self

    def segment_id(self, segment_id: str) -> CreateChildChunkRequestBuilder:
        self._create_child_chunk_request.segment_id = segment_id
        self._create_child_chunk_request.paths["segment_id"] = segment_id
        return self

    def request_body(self, request_body: CreateChildChunkRequestBody) -> CreateChildChunkRequestBuilder:
        self._create_child_chunk_request.request_body = request_body
        self._create_child_chunk_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
