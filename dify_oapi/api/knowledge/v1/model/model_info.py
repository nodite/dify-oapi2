"""Model information model for Knowledge Base API."""

from typing import Any, Optional

from pydantic import BaseModel

from .knowledge_types import ModelType, ProviderType


class ModelInfo(BaseModel):
    """Model information model with builder pattern."""

    model_name: Optional[str] = None
    model_type: Optional[ModelType] = None
    provider: Optional[str] = None
    provider_type: Optional[ProviderType] = None
    credentials: Optional[dict[str, Any]] = None
    load_balancing: Optional[dict[str, Any]] = None

    @staticmethod
    def builder() -> "ModelInfoBuilder":
        return ModelInfoBuilder()


class ModelInfoBuilder:
    """Builder for ModelInfo."""

    def __init__(self):
        self._model_info = ModelInfo()

    def build(self) -> ModelInfo:
        return self._model_info

    def model_name(self, model_name: str) -> "ModelInfoBuilder":
        self._model_info.model_name = model_name
        return self

    def model_type(self, model_type: ModelType) -> "ModelInfoBuilder":
        self._model_info.model_type = model_type
        return self

    def provider(self, provider: str) -> "ModelInfoBuilder":
        self._model_info.provider = provider
        return self

    def provider_type(self, provider_type: ProviderType) -> "ModelInfoBuilder":
        self._model_info.provider_type = provider_type
        return self

    def credentials(self, credentials: dict[str, Any]) -> "ModelInfoBuilder":
        self._model_info.credentials = credentials
        return self

    def load_balancing(self, load_balancing: dict[str, Any]) -> "ModelInfoBuilder":
        self._model_info.load_balancing = load_balancing
        return self
