"""Update status request body model for document API."""

from __future__ import annotations

from pydantic import BaseModel


class UpdateStatusRequestBody(BaseModel):
    """Request body model for updating document status."""

    document_ids: list[str] | None = None

    @staticmethod
    def builder() -> UpdateStatusRequestBodyBuilder:
        """Create a new UpdateStatusRequestBodyBuilder instance."""
        return UpdateStatusRequestBodyBuilder()


class UpdateStatusRequestBodyBuilder:
    """Builder for UpdateStatusRequestBody."""

    def __init__(self) -> None:
        self._update_status_request_body = UpdateStatusRequestBody()

    def build(self) -> UpdateStatusRequestBody:
        """Build the UpdateStatusRequestBody instance."""
        return self._update_status_request_body

    def document_ids(self, document_ids: list[str]) -> UpdateStatusRequestBodyBuilder:
        """Set the document IDs."""
        self._update_status_request_body.document_ids = document_ids
        return self
