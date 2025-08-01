"""Update document by text request body model."""

from __future__ import annotations

from pydantic import BaseModel

from .process_rule import ProcessRule


class UpdateByTextRequestBody(BaseModel):
    """Request body model for updating document by text."""

    name: str | None = None
    text: str | None = None
    process_rule: ProcessRule | None = None

    @staticmethod
    def builder() -> UpdateByTextRequestBodyBuilder:
        """Create a new UpdateByTextRequestBodyBuilder instance."""
        return UpdateByTextRequestBodyBuilder()


class UpdateByTextRequestBodyBuilder:
    """Builder for UpdateByTextRequestBody."""

    def __init__(self) -> None:
        self._update_by_text_request_body = UpdateByTextRequestBody()

    def build(self) -> UpdateByTextRequestBody:
        """Build the UpdateByTextRequestBody instance."""
        return self._update_by_text_request_body

    def name(self, name: str) -> UpdateByTextRequestBodyBuilder:
        """Set the document name."""
        self._update_by_text_request_body.name = name
        return self

    def text(self, text: str) -> UpdateByTextRequestBodyBuilder:
        """Set the document text content."""
        self._update_by_text_request_body.text = text
        return self

    def process_rule(self, process_rule: ProcessRule) -> UpdateByTextRequestBodyBuilder:
        """Set the processing rule."""
        self._update_by_text_request_body.process_rule = process_rule
        return self
