from __future__ import annotations

from pydantic import BaseModel

from .metadata_filtering_conditions import MetadataFilteringConditions
from .reranking_model import RerankingModel


class KeywordSetting(BaseModel):
    keyword_weight: float | None = None


class VectorSetting(BaseModel):
    vector_weight: float | None = None
    embedding_model_name: str | None = None
    embedding_provider_name: str | None = None


class Weights(BaseModel):
    keyword_setting: KeywordSetting | None = None

    vector_setting: VectorSetting | None = None


class RetrievalModel(BaseModel):
    search_method: str | None = None
    reranking_enable: bool | None = None
    reranking_mode: str | None = None
    reranking_model: RerankingModel | None = None
    weights: Weights | None = None
    top_k: int | None = None
    score_threshold_enabled: bool | None = None
    score_threshold: float | None = None
    metadata_filtering_conditions: MetadataFilteringConditions | None = None
