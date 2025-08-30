"""Reranking model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel

from .model_credentials import ModelCredentials
from .model_parameters import ModelParameters


class RerankingModel(BaseModel):
    """Reranking model with builder pattern."""

    model: Optional[str] = None
    provider: Optional[str] = None
    credentials: Optional[ModelCredentials] = None
    model_parameters: Optional[ModelParameters] = None

    @staticmethod
    def builder() -> "RerankingModelBuilder":
        return RerankingModelBuilder()


class RerankingModelBuilder:
    """Builder for RerankingModel."""

    def __init__(self):
        self._reranking_model = RerankingModel()

    def build(self) -> RerankingModel:
        return self._reranking_model

    def model(self, model: str) -> "RerankingModelBuilder":
        self._reranking_model.model = model
        return self

    def provider(self, provider: str) -> "RerankingModelBuilder":
        self._reranking_model.provider = provider
        return self

    def credentials(self, credentials: ModelCredentials) -> "RerankingModelBuilder":
        self._reranking_model.credentials = credentials
        return self

    def model_parameters(self, model_parameters: ModelParameters) -> "RerankingModelBuilder":
        self._reranking_model.model_parameters = model_parameters
        return self
