from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from .reranking_model import RerankingModel
from .metadata_filtering_conditions import MetadataFilteringConditions


class RetrievalModel(BaseModel):
    search_method: str
    reranking_enable: Optional[bool] = None
    reranking_mode: Optional[str] = None
    reranking_model: Optional[RerankingModel] = None
    weights: Optional[float] = None
    top_k: Optional[int] = None
    score_threshold_enabled: Optional[bool] = None
    score_threshold: Optional[float] = None
    metadata_filtering_conditions: Optional[MetadataFilteringConditions] = None

    @staticmethod
    def builder() -> RetrievalModelBuilder:
        return RetrievalModelBuilder()


class RetrievalModelBuilder:
    def __init__(self):
        self._retrieval_model = RetrievalModel(search_method="semantic_search")

    def build(self) -> RetrievalModel:
        return self._retrieval_model

    def search_method(self, search_method: str) -> RetrievalModelBuilder:
        self._retrieval_model.search_method = search_method
        return self

    def reranking_enable(self, reranking_enable: bool) -> RetrievalModelBuilder:
        self._retrieval_model.reranking_enable = reranking_enable
        return self

    def reranking_mode(self, reranking_mode: str) -> RetrievalModelBuilder:
        self._retrieval_model.reranking_mode = reranking_mode
        return self

    def reranking_model(self, reranking_model: RerankingModel) -> RetrievalModelBuilder:
        self._retrieval_model.reranking_model = reranking_model
        return self

    def weights(self, weights: float) -> RetrievalModelBuilder:
        self._retrieval_model.weights = weights
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

    def metadata_filtering_conditions(self, metadata_filtering_conditions: MetadataFilteringConditions) -> RetrievalModelBuilder:
        self._retrieval_model.metadata_filtering_conditions = metadata_filtering_conditions
        return self