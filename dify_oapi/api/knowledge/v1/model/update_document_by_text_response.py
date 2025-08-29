"""Update document by text response model."""

from dify_oapi.core.model.base_response import BaseResponse

from .document_info import DocumentInfo


class UpdateDocumentByTextResponse(BaseResponse):
    """Response model for update document by text API."""

    document: DocumentInfo | None = None
    batch: str | None = None
