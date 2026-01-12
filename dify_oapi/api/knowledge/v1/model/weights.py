"""Weights model for retrieval configuration."""

from pydantic import BaseModel


class KeywordSetting(BaseModel):
    """Keyword search weight settings."""

    keyword_weight: float | None = None


class VectorSetting(BaseModel):
    """Vector search weight settings."""

    vector_weight: float | None = None
    embedding_model_name: str | None = None
    embedding_provider_name: str | None = None


class Weights(BaseModel):
    """Weights configuration for hybrid search."""

    weight_type: str | None = None
    keyword_setting: KeywordSetting | None = None
    vector_setting: VectorSetting | None = None
