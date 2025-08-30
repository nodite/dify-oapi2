"""Document metadata model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel


class DocumentMetadata(BaseModel):
    """Document metadata model with builder pattern."""

    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def builder() -> "DocumentMetadataBuilder":
        return DocumentMetadataBuilder()


class DocumentMetadataBuilder:
    """Builder for DocumentMetadata."""

    def __init__(self):
        self._document_metadata = DocumentMetadata()

    def build(self) -> DocumentMetadata:
        return self._document_metadata

    def id(self, id: str) -> "DocumentMetadataBuilder":
        self._document_metadata.id = id
        return self

    def name(self, name: str) -> "DocumentMetadataBuilder":
        self._document_metadata.name = name
        return self

    def type(self, type: str) -> "DocumentMetadataBuilder":
        self._document_metadata.type = type
        return self
