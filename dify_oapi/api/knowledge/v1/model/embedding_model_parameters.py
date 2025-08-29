"""Embedding model parameters for Knowledge Base API."""

from typing import Any, Optional

from pydantic import BaseModel


class EmbeddingModelParameters(BaseModel):
    """Embedding model parameters with builder pattern."""

    model: Optional[str] = None
    provider: Optional[str] = None
    credentials: Optional[dict[str, Any]] = None
    model_parameters: Optional[dict[str, Any]] = None

    @staticmethod
    def builder() -> "EmbeddingModelParametersBuilder":
        return EmbeddingModelParametersBuilder()


class EmbeddingModelParametersBuilder:
    """Builder for EmbeddingModelParameters."""

    def __init__(self):
        self._embedding_model_parameters = EmbeddingModelParameters()

    def build(self) -> EmbeddingModelParameters:
        return self._embedding_model_parameters

    def model(self, model: str) -> "EmbeddingModelParametersBuilder":
        self._embedding_model_parameters.model = model
        return self

    def provider(self, provider: str) -> "EmbeddingModelParametersBuilder":
        self._embedding_model_parameters.provider = provider
        return self

    def credentials(self, credentials: dict[str, Any]) -> "EmbeddingModelParametersBuilder":
        self._embedding_model_parameters.credentials = credentials
        return self

    def model_parameters(self, model_parameters: dict[str, Any]) -> "EmbeddingModelParametersBuilder":
        self._embedding_model_parameters.model_parameters = model_parameters
        return self
