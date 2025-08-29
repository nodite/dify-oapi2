from __future__ import annotations

from typing import Literal

from pydantic import BaseModel


class RetrievalModel(BaseModel):
    """Document-specific retrieval model for search and retrieval configuration."""

    search_method: str | None = None
    reranking_enable: bool | None = None
    reranking_model: dict | None = None
    top_k: int | None = None
    score_threshold_enabled: bool | None = None
    score_threshold: float | None = None

    @staticmethod
    def builder() -> RetrievalModelBuilder:
        return RetrievalModelBuilder()


class RetrievalModelBuilder:
    def __init__(self):
        self._retrieval_model = RetrievalModel()

    def build(self) -> RetrievalModel:
        return self._retrieval_model

    def search_method(
        self, search_method: Literal["keyword_search", "semantic_search", "full_text_search", "hybrid_search"]
    ) -> RetrievalModelBuilder:
        self._retrieval_model.search_method = search_method
        return self

    def reranking_enable(self, reranking_enable: bool) -> RetrievalModelBuilder:
        self._retrieval_model.reranking_enable = reranking_enable
        return self

    def reranking_model(self, reranking_model: dict) -> RetrievalModelBuilder:
        self._retrieval_model.reranking_model = reranking_model
        return self

    def top_k(self, top_k: int) -> RetrievalModelBuilder:
        self._retrieval_model.top_k = top_k
        return self

    def score_threshold_enabled(self, score_threshold_enabled: bool) -> RetrievalModelBuilder:
        self._retrieval_model.score_threshold_enabled = score_threshold_enabled
        return self

    def score_threshold(self, score_threshold: float) -> RetrievalModelBuilder:
        self._retrieval_model.score_threshold = score_threshold
        return self
