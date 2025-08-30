from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class CompletionInputs(BaseModel):
    """
    Inputs for completion application containing variables defined in the App.
    Text generation applications require at least the query field.
    Additional custom variables can be added as needed.
    """

    query: str  # Required: User input text content

    # Allow additional fields for custom variables
    model_config = {"extra": "allow"}

    @staticmethod
    def builder() -> CompletionInputsBuilder:
        return CompletionInputsBuilder()

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary format expected by API."""
        result: dict[str, Any] = self.model_dump()
        return result


class CompletionInputsBuilder:
    def __init__(self):
        self._data: dict[str, Any] = {}

    def build(self) -> CompletionInputs:
        if "query" not in self._data:
            raise ValueError("query field is required for CompletionInputs")
        return CompletionInputs(**self._data)

    def query(self, query: str) -> CompletionInputsBuilder:
        """Set the required query field."""
        self._data["query"] = query
        return self

    def add_variable(self, key: str, value: str) -> CompletionInputsBuilder:
        """Add a custom variable to the inputs."""
        self._data[key] = value
        return self

    def variables(self, variables: dict[str, str]) -> CompletionInputsBuilder:
        """Add multiple custom variables to the inputs."""
        self._data.update(variables)
        return self
