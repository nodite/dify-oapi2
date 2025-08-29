"""Get document response model."""

from dify_oapi.core.model.base_response import BaseResponse

from .document_info import DocumentInfo


class GetDocumentResponse(DocumentInfo, BaseResponse):
    """Response model for get document API."""

    pass
