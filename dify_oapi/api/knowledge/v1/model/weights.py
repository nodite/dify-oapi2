"""Weights model for retrieval configuration."""

from typing import Optional

from pydantic import BaseModel


class KeywordSetting(BaseModel):
    """Keyword search weight settings."""

    keyword_weight: Optional[float] = None


class VectorSetting(BaseModel):
    """Vector search weight settings."""

    vector_weight: Optional[float] = None
    embedding_model_name: Optional[str] = None
    embedding_provider_name: Optional[str] = None


class Weights(BaseModel):
    """Weights configuration for hybrid search."""

    weight_type: Optional[str] = None
    keyword_setting: Optional[KeywordSetting] = None
    vector_setting: Optional[VectorSetting] = None
