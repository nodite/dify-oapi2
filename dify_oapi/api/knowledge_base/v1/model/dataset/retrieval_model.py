from __future__ import annotations

from pydantic import BaseModel

from .metadata_filtering_conditions import MetadataFilteringConditions
from .reranking_model import RerankingModel


class RetrievalModel(BaseModel):
    search_method: str | None = None
    reranking_enable: bool | None = None
    reranking_mode: str | None = None
    reranking_model: RerankingModel | None = None
    weights: float | None = None
    top_k: int | None = None
    score_threshold_enabled: bool | None = None
    score_threshold: float | None = None
    metadata_filtering_conditions: MetadataFilteringConditions | None = None
