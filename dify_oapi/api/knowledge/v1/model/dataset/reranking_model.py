from __future__ import annotations

from pydantic import BaseModel


class RerankingModel(BaseModel):
    reranking_provider_name: str | None = None
    reranking_model_name: str | None = None

    @staticmethod
    def builder() -> RerankingModelBuilder:
        return RerankingModelBuilder()


class RerankingModelBuilder:
    def __init__(self):
        self._reranking_model = RerankingModel()

    def build(self) -> RerankingModel:
        return self._reranking_model

    def reranking_provider_name(self, reranking_provider_name: str) -> RerankingModelBuilder:
        self._reranking_model.reranking_provider_name = reranking_provider_name
        return self

    def reranking_model_name(self, reranking_model_name: str) -> RerankingModelBuilder:
        self._reranking_model.reranking_model_name = reranking_model_name
        return self
