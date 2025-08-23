from __future__ import annotations

from pydantic import BaseModel


class CompletionInputs(BaseModel):
    """
    Inputs for completion application containing variables defined in the App.
    Text generation applications require at least the query field.
    """

    query: str | None = None  # User input text content (required for completion apps)

    @staticmethod
    def builder() -> CompletionInputsBuilder:
        return CompletionInputsBuilder()


class CompletionInputsBuilder:
    def __init__(self):
        self._completion_inputs = CompletionInputs()

    def build(self) -> CompletionInputs:
        return self._completion_inputs

    def query(self, query: str) -> CompletionInputsBuilder:
        self._completion_inputs.query = query
        return self
