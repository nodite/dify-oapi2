"""Update document status request body model."""

from __future__ import annotations

from pydantic import BaseModel


class UpdateDocumentStatusRequestBody(BaseModel):
    """Request body model for update document status API."""

    document_ids: list[str] | None = None

    @staticmethod
    def builder() -> UpdateDocumentStatusRequestBodyBuilder:
        return UpdateDocumentStatusRequestBodyBuilder()


class UpdateDocumentStatusRequestBodyBuilder:
    """Builder for UpdateDocumentStatusRequestBody."""

    def __init__(self) -> None:
        self._update_document_status_request_body = UpdateDocumentStatusRequestBody()

    def build(self) -> UpdateDocumentStatusRequestBody:
        return self._update_document_status_request_body

    def document_ids(self, document_ids: list[str]) -> UpdateDocumentStatusRequestBodyBuilder:
        self._update_document_status_request_body.document_ids = document_ids
        return self
