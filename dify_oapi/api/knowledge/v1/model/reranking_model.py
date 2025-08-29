"""Reranking model for Knowledge Base API."""

from typing import Any, Optional

from pydantic import BaseModel


class RerankingModel(BaseModel):
    """Reranking model with builder pattern."""

    model: Optional[str] = None
    provider: Optional[str] = None
    credentials: Optional[dict[str, Any]] = None
    model_parameters: Optional[dict[str, Any]] = None

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

    def credentials(self, credentials: dict[str, Any]) -> "RerankingModelBuilder":
        self._reranking_model.credentials = credentials
        return self

    def model_parameters(self, model_parameters: dict[str, Any]) -> "RerankingModelBuilder":
        self._reranking_model.model_parameters = model_parameters
        return self
