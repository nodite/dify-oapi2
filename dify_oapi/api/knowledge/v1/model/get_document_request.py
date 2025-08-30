"""Get document request model."""

from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetDocumentRequest(BaseRequest):
    """Request model for get document API."""

    def __init__(self) -> None:
        super().__init__()
        self.dataset_id: str | None = None
        self.document_id: str | None = None

    @staticmethod
    def builder() -> GetDocumentRequestBuilder:
        return GetDocumentRequestBuilder()


class GetDocumentRequestBuilder:
    """Builder for GetDocumentRequest."""

    def __init__(self) -> None:
        get_document_request = GetDocumentRequest()
        get_document_request.http_method = HttpMethod.GET
        get_document_request.uri = "/v1/datasets/:dataset_id/documents/:document_id"
        self._get_document_request = get_document_request

    def build(self) -> GetDocumentRequest:
        return self._get_document_request

    def dataset_id(self, dataset_id: str) -> GetDocumentRequestBuilder:
        self._get_document_request.dataset_id = dataset_id
        self._get_document_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> GetDocumentRequestBuilder:
        self._get_document_request.document_id = document_id
        self._get_document_request.paths["document_id"] = document_id
        return self
