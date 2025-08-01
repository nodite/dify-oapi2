"""Update document by text response model."""

from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .document_info import DocumentInfo


class UpdateByTextResponse(BaseResponse):
    """Response model for updating document by text."""

    document: DocumentInfo | None = None
    batch: str | None = None
