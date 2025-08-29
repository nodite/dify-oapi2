"""Retrieval model for Knowledge Base API."""

from typing import Any, Optional

from pydantic import BaseModel

from .knowledge_types import SearchMethod


class RetrievalModel(BaseModel):
    """Retrieval model with builder pattern."""

    search_method: Optional[SearchMethod] = None
    reranking_enable: Optional[bool] = None
    reranking_model: Optional[dict[str, Any]] = None
    top_k: Optional[int] = None
    score_threshold_enabled: Optional[bool] = None
    score_threshold: Optional[float] = None

    @staticmethod
    def builder() -> "RetrievalModelBuilder":
        return RetrievalModelBuilder()


class RetrievalModelBuilder:
    """Builder for RetrievalModel."""

    def __init__(self):
        self._retrieval_model = RetrievalModel()

    def build(self) -> RetrievalModel:
        return self._retrieval_model

    def search_method(self, search_method: SearchMethod) -> "RetrievalModelBuilder":
        self._retrieval_model.search_method = search_method
        return self

    def reranking_enable(self, reranking_enable: bool) -> "RetrievalModelBuilder":
        self._retrieval_model.reranking_enable = reranking_enable
        return self

    def reranking_model(self, reranking_model: dict[str, Any]) -> "RetrievalModelBuilder":
        self._retrieval_model.reranking_model = reranking_model
        return self

    def top_k(self, top_k: int) -> "RetrievalModelBuilder":
        self._retrieval_model.top_k = top_k
        return self

    def score_threshold_enabled(self, score_threshold_enabled: bool) -> "RetrievalModelBuilder":
        self._retrieval_model.score_threshold_enabled = score_threshold_enabled
        return self

    def score_threshold(self, score_threshold: float) -> "RetrievalModelBuilder":
        self._retrieval_model.score_threshold = score_threshold
        return self
