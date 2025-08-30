"""Embedding model parameters for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel

from .model_credentials import ModelCredentials
from .model_parameters import ModelParameters


class EmbeddingModelParameters(BaseModel):
    """Embedding model parameters with builder pattern."""

    model: Optional[str] = None
    provider: Optional[str] = None
    credentials: Optional[ModelCredentials] = None
    model_parameters: Optional[ModelParameters] = None

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

    def credentials(self, credentials: ModelCredentials) -> "EmbeddingModelParametersBuilder":
        self._embedding_model_parameters.credentials = credentials
        return self

    def model_parameters(self, model_parameters: ModelParameters) -> "EmbeddingModelParametersBuilder":
        self._embedding_model_parameters.model_parameters = model_parameters
        return self
