from __future__ import annotations

from pydantic import BaseModel

from .document_info import DocumentInfo


class ListResponse(BaseModel):
    """Response model for list documents API"""

    data: list[DocumentInfo] | None = None
    has_more: bool | None = None
    limit: int | None = None
    total: int | None = None
    page: int | None = None
