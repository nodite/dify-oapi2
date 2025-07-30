"""Create document by file response model."""

from pydantic import BaseModel

from .document_info import DocumentInfo


class CreateByFileResponse(BaseModel):
    """Response model for create document by file API."""

    document: DocumentInfo | None = None
    batch: str | None = None
