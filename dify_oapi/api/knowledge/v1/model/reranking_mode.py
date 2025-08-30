"""Reranking mode model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel

from .knowledge_types import RerankingModelName, RerankingProviderName


class RerankingMode(BaseModel):
    """Reranking mode model with builder pattern."""

    reranking_provider_name: Optional[RerankingProviderName] = None
    reranking_model_name: Optional[RerankingModelName] = None

    @staticmethod
    def builder() -> "RerankingModeBuilder":
        return RerankingModeBuilder()


class RerankingModeBuilder:
    """Builder for RerankingMode."""

    def __init__(self):
        self._reranking_mode = RerankingMode()

    def build(self) -> RerankingMode:
        return self._reranking_mode

    def reranking_provider_name(self, reranking_provider_name: RerankingProviderName) -> "RerankingModeBuilder":
        self._reranking_mode.reranking_provider_name = reranking_provider_name
        return self

    def reranking_model_name(self, reranking_model_name: RerankingModelName) -> "RerankingModeBuilder":
        self._reranking_mode.reranking_model_name = reranking_model_name
        return self
