"""Update document status request model."""

from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .knowledge_types import DocumentStatusAction
from .update_document_status_request_body import UpdateDocumentStatusRequestBody


class UpdateDocumentStatusRequest(BaseRequest):
    """Request model for update document status API."""

    def __init__(self) -> None:
        super().__init__()
        self.dataset_id: str | None = None
        self.action: DocumentStatusAction | None = None
        self.request_body: UpdateDocumentStatusRequestBody | None = None

    @staticmethod
    def builder() -> UpdateDocumentStatusRequestBuilder:
        return UpdateDocumentStatusRequestBuilder()


class UpdateDocumentStatusRequestBuilder:
    """Builder for UpdateDocumentStatusRequest."""

    def __init__(self) -> None:
        update_document_status_request = UpdateDocumentStatusRequest()
        update_document_status_request.http_method = HttpMethod.PATCH
        update_document_status_request.uri = "/v1/datasets/:dataset_id/documents/status/:action"
        self._update_document_status_request = update_document_status_request

    def build(self) -> UpdateDocumentStatusRequest:
        return self._update_document_status_request

    def dataset_id(self, dataset_id: str) -> UpdateDocumentStatusRequestBuilder:
        self._update_document_status_request.dataset_id = dataset_id
        self._update_document_status_request.paths["dataset_id"] = dataset_id
        return self

    def action(self, action: DocumentStatusAction) -> UpdateDocumentStatusRequestBuilder:
        self._update_document_status_request.action = action
        self._update_document_status_request.paths["action"] = action
        return self

    def request_body(self, request_body: UpdateDocumentStatusRequestBody) -> UpdateDocumentStatusRequestBuilder:
        self._update_document_status_request.request_body = request_body
        self._update_document_status_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
