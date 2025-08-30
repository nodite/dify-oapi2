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

    def with_variables(self, **kwargs: Any) -> CompletionInputs:
        result: CompletionInputs = self.model_copy(update=kwargs)
        return result


class CompletionInputsBuilder:
    def __init__(self):
        self._inputs: CompletionInputs | None = None

    def build(self) -> CompletionInputs:
        if self._inputs is None:
            raise ValueError("query field is required for CompletionInputs")
        return self._inputs

    def query(self, query: str) -> CompletionInputsBuilder:
        self._inputs = CompletionInputs(query=query)
        return self

    def add_variable(self, key: str, value: Any) -> CompletionInputsBuilder:
        if self._inputs is None:
            raise ValueError("Must set query first")
        self._inputs = self._inputs.with_variables(**{key: value})
        return self

    def variables(self, **kwargs: Any) -> CompletionInputsBuilder:
        if self._inputs is None:
            raise ValueError("Must set query first")
        self._inputs = self._inputs.with_variables(**kwargs)
        return self
