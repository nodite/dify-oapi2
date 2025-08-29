"""List documents request model."""

from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class ListDocumentsRequest(BaseRequest):
    """Request model for list documents API."""

    def __init__(self) -> None:
        super().__init__()
        self.dataset_id: str | None = None

    @staticmethod
    def builder() -> ListDocumentsRequestBuilder:
        return ListDocumentsRequestBuilder()


class ListDocumentsRequestBuilder:
    """Builder for ListDocumentsRequest."""

    def __init__(self) -> None:
        list_documents_request = ListDocumentsRequest()
        list_documents_request.http_method = HttpMethod.GET
        list_documents_request.uri = "/v1/datasets/:dataset_id/documents"
        self._list_documents_request = list_documents_request

    def build(self) -> ListDocumentsRequest:
        return self._list_documents_request

    def dataset_id(self, dataset_id: str) -> ListDocumentsRequestBuilder:
        self._list_documents_request.dataset_id = dataset_id
        self._list_documents_request.paths["dataset_id"] = dataset_id
        return self

    def keyword(self, keyword: str) -> ListDocumentsRequestBuilder:
        self._list_documents_request.add_query("keyword", keyword)
        return self

    def page(self, page: int) -> ListDocumentsRequestBuilder:
        self._list_documents_request.add_query("page", str(page))
        return self

    def limit(self, limit: int) -> ListDocumentsRequestBuilder:
        self._list_documents_request.add_query("limit", str(limit))
        return self
