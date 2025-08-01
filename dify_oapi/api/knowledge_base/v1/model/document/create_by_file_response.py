"""Create document by file response model."""

from dify_oapi.core.model.base_response import BaseResponse

from .document_info import DocumentInfo


class CreateByFileResponse(BaseResponse):
    """Response model for create document by file API."""

    document: DocumentInfo | None = None
    batch: str | None = None
