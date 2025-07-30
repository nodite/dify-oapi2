from __future__ import annotations

from pydantic import BaseModel

from .document_info import DocumentInfo


class UpdateByFileResponse(BaseModel):
    """Response model for update document by file API"""

    document: DocumentInfo | None = None
    batch: str | None = None
