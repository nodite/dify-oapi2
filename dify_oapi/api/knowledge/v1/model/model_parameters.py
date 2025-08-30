"""Model parameters for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel


class ModelParameters(BaseModel):
    """Model parameters with builder pattern."""

    context_size: Optional[int] = None
    max_chunks: Optional[int] = None

    @staticmethod
    def builder() -> "ModelParametersBuilder":
        return ModelParametersBuilder()


class ModelParametersBuilder:
    """Builder for ModelParameters."""

    def __init__(self):
        self._model_parameters = ModelParameters()

    def build(self) -> ModelParameters:
        return self._model_parameters

    def context_size(self, context_size: int) -> "ModelParametersBuilder":
        self._model_parameters.context_size = context_size
        return self

    def max_chunks(self, max_chunks: int) -> "ModelParametersBuilder":
        self._model_parameters.max_chunks = max_chunks
        return self
