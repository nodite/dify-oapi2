"""Update document by file request body model."""

from __future__ import annotations

from pydantic import BaseModel

from .update_document_by_file_request_body_data import UpdateDocumentByFileRequestBodyData


class UpdateDocumentByFileRequestBody(BaseModel):
    """Request body model for update document by file API."""

    data: str | None = None

    @staticmethod
    def builder() -> UpdateDocumentByFileRequestBodyBuilder:
        return UpdateDocumentByFileRequestBodyBuilder()


class UpdateDocumentByFileRequestBodyBuilder:
    """Builder for UpdateDocumentByFileRequestBody."""

    def __init__(self) -> None:
        self._update_document_by_file_request_body = UpdateDocumentByFileRequestBody()

    def build(self) -> UpdateDocumentByFileRequestBody:
        return self._update_document_by_file_request_body

    def data(self, data: UpdateDocumentByFileRequestBodyData) -> UpdateDocumentByFileRequestBodyBuilder:
        self._update_document_by_file_request_body.data = data.model_dump_json(exclude_none=True)
        return self
