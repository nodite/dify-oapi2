from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .document_info import DocumentInfo


class UpdateByFileResponse(BaseResponse):
    """Response model for update document by file API"""

    document: DocumentInfo | None = None
    batch: str | None = None
