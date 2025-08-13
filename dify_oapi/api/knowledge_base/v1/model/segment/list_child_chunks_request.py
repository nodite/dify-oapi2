from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class ListChildChunksRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.document_id: str | None = None
        self.segment_id: str | None = None

    @staticmethod
    def builder() -> ListChildChunksRequestBuilder:
        return ListChildChunksRequestBuilder()


class ListChildChunksRequestBuilder:
    def __init__(self):
        list_child_chunks_request = ListChildChunksRequest()
        list_child_chunks_request.http_method = HttpMethod.GET
        list_child_chunks_request.uri = (
            "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks"
        )
        self._list_child_chunks_request = list_child_chunks_request

    def build(self) -> ListChildChunksRequest:
        return self._list_child_chunks_request

    def dataset_id(self, dataset_id: str) -> ListChildChunksRequestBuilder:
        self._list_child_chunks_request.dataset_id = dataset_id
        self._list_child_chunks_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> ListChildChunksRequestBuilder:
        self._list_child_chunks_request.document_id = document_id
        self._list_child_chunks_request.paths["document_id"] = document_id
        return self

    def segment_id(self, segment_id: str) -> ListChildChunksRequestBuilder:
        self._list_child_chunks_request.segment_id = segment_id
        self._list_child_chunks_request.paths["segment_id"] = segment_id
        return self

    def keyword(self, keyword: str) -> ListChildChunksRequestBuilder:
        self._list_child_chunks_request.add_query("keyword", keyword)
        return self

    def page(self, page: int) -> ListChildChunksRequestBuilder:
        self._list_child_chunks_request.add_query("page", page)
        return self

    def limit(self, limit: int) -> ListChildChunksRequestBuilder:
        self._list_child_chunks_request.add_query("limit", limit)
        return self
