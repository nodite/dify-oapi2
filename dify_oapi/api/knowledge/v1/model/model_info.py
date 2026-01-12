"""Model information model for Knowledge Base API."""

from pydantic import BaseModel

from .knowledge_types import ModelFeature, ModelFetchFrom, ModelStatus
from .model_parameters import ModelParameters


class ModelLabel(BaseModel):
    """Model label with localization support."""

    en_US: str | None = None  # noqa: N815
    zh_Hans: str | None = None  # noqa: N815


class ModelIcon(BaseModel):
    """Model icon with different sizes."""

    en_US: str | None = None  # noqa: N815
    zh_Hans: str | None = None  # noqa: N815


class EmbeddingModelDetails(BaseModel):
    """Individual embedding model details."""

    model: str | None = None
    label: ModelLabel | None = None
    model_type: str | None = None
    features: list[ModelFeature] | None = None
    fetch_from: ModelFetchFrom | None = None
    model_properties: ModelParameters | None = None
    deprecated: bool | None = None
    status: ModelStatus | None = None
    load_balancing_enabled: bool | None = None


class ModelInfo(BaseModel):
    """Model provider information with embedding models."""

    provider: str | None = None
    label: ModelLabel | None = None
    icon_small: ModelIcon | None = None
    icon_large: ModelIcon | None = None
    status: ModelStatus | None = None
    models: list[EmbeddingModelDetails] | None = None

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
