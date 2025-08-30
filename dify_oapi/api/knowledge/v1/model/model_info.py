"""Model information model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel

from .knowledge_types import ModelFeature, ModelFetchFrom, ModelStatus
from .model_parameters import ModelParameters


class ModelLabel(BaseModel):
    """Model label with localization support."""

    en_US: Optional[str] = None  # noqa: N815
    zh_Hans: Optional[str] = None  # noqa: N815


class ModelIcon(BaseModel):
    """Model icon with different sizes."""

    en_US: Optional[str] = None  # noqa: N815
    zh_Hans: Optional[str] = None  # noqa: N815


class EmbeddingModelDetails(BaseModel):
    """Individual embedding model details."""

    model: Optional[str] = None
    label: Optional[ModelLabel] = None
    model_type: Optional[str] = None
    features: Optional[list[ModelFeature]] = None
    fetch_from: Optional[ModelFetchFrom] = None
    model_properties: Optional[ModelParameters] = None
    deprecated: Optional[bool] = None
    status: Optional[ModelStatus] = None
    load_balancing_enabled: Optional[bool] = None


class ModelInfo(BaseModel):
    """Model provider information with embedding models."""

    provider: Optional[str] = None
    label: Optional[ModelLabel] = None
    icon_small: Optional[ModelIcon] = None
    icon_large: Optional[ModelIcon] = None
    status: Optional[ModelStatus] = None
    models: Optional[list[EmbeddingModelDetails]] = None

    @staticmethod
    def builder() -> "ModelInfoBuilder":
        return ModelInfoBuilder()


class ModelInfoBuilder:
    """Builder for ModelInfo."""

    def __init__(self):
        self._model_info = ModelInfo()

    def build(self) -> ModelInfo:
        return self._model_info

    def provider(self, provider: str) -> "ModelInfoBuilder":
        self._model_info.provider = provider
        return self

    def label(self, label: ModelLabel) -> "ModelInfoBuilder":
        self._model_info.label = label
        return self

    def icon_small(self, icon_small: ModelIcon) -> "ModelInfoBuilder":
        self._model_info.icon_small = icon_small
        return self

    def icon_large(self, icon_large: ModelIcon) -> "ModelInfoBuilder":
        self._model_info.icon_large = icon_large
        return self

    def status(self, status: ModelStatus) -> "ModelInfoBuilder":
        self._model_info.status = status
        return self

    def models(self, models: list[EmbeddingModelDetails]) -> "ModelInfoBuilder":
        self._model_info.models = models
        return self
