"""Create document by file request body model."""

from __future__ import annotations

from pydantic import BaseModel

from .create_document_by_file_request_body_data import CreateDocumentByFileRequestBodyData


class CreateDocumentByFileRequestBody(BaseModel):
    """Request body model for create document by file API."""

    data: str | None = None

    @staticmethod
    def builder() -> CreateDocumentByFileRequestBodyBuilder:
        return CreateDocumentByFileRequestBodyBuilder()


class CreateDocumentByFileRequestBodyBuilder:
    """Builder for CreateDocumentByFileRequestBody."""

    def __init__(self) -> None:
        self._create_document_by_file_request_body = CreateDocumentByFileRequestBody()

    def build(self) -> CreateDocumentByFileRequestBody:
        return self._create_document_by_file_request_body

    def data(self, data: CreateDocumentByFileRequestBodyData) -> CreateDocumentByFileRequestBodyBuilder:
        self._create_document_by_file_request_body.data = data.model_dump_json(exclude_none=True)
        return self
