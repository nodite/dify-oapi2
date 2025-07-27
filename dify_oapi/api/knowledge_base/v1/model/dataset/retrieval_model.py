from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from .reranking_model import RerankingModel
from .metadata_filtering_conditions import MetadataFilteringConditions


class RetrievalModel(BaseModel):
    search_method: Optional[str] = None
    reranking_enable: Optional[bool] = None
    reranking_mode: Optional[str] = None
    reranking_model: Optional[RerankingModel] = None
    weights: Optional[float] = None
    top_k: Optional[int] = None
    score_threshold_enabled: Optional[bool] = None
    score_threshold: Optional[float] = None
    metadata_filtering_conditions: Optional[MetadataFilteringConditions] = None

