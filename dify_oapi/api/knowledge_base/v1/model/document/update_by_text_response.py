"""Update document by text response model."""

from __future__ import annotations

from pydantic import BaseModel

from .document_info import DocumentInfo


class UpdateByTextResponse(BaseModel):
    """Response model for updating document by text."""

    document: DocumentInfo | None = None
    batch: str | None = None
