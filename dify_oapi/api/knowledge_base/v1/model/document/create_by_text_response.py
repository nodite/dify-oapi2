from __future__ import annotations

from pydantic import BaseModel

from .document_info import DocumentInfo


class CreateByTextResponse(BaseModel):
    """Response model for create document by text API"""

    document: DocumentInfo | None = None
    batch: str | None = None
