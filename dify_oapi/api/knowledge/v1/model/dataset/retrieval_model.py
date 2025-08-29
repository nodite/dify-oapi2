from __future__ import annotations

from pydantic import BaseModel

from .dataset_types import SearchMethod
from .metadata_filtering_conditions import MetadataFilteringConditions
from .reranking_model import RerankingModel


class KeywordSetting(BaseModel):
    keyword_weight: float | None = None

    @staticmethod
    def builder() -> KeywordSettingBuilder:
        return KeywordSettingBuilder()


class KeywordSettingBuilder:
    def __init__(self):
        self._keyword_setting = KeywordSetting()

    def build(self) -> KeywordSetting:
        return self._keyword_setting

    def keyword_weight(self, keyword_weight: float) -> KeywordSettingBuilder:
        self._keyword_setting.keyword_weight = keyword_weight
        return self


class VectorSetting(BaseModel):
    vector_weight: float | None = None
    embedding_model_name: str | None = None
    embedding_provider_name: str | None = None

    @staticmethod
    def builder() -> VectorSettingBuilder:
        return VectorSettingBuilder()


class VectorSettingBuilder:
    def __init__(self):
        self._vector_setting = VectorSetting()

    def build(self) -> VectorSetting:
        return self._vector_setting

    def vector_weight(self, vector_weight: float) -> VectorSettingBuilder:
        self._vector_setting.vector_weight = vector_weight
        return self

    def embedding_model_name(self, embedding_model_name: str) -> VectorSettingBuilder:
        self._vector_setting.embedding_model_name = embedding_model_name
        return self

    def embedding_provider_name(self, embedding_provider_name: str) -> VectorSettingBuilder:
        self._vector_setting.embedding_provider_name = embedding_provider_name
        return self


class Weights(BaseModel):
    keyword_setting: KeywordSetting | None = None
    vector_setting: VectorSetting | None = None

    @staticmethod
    def builder() -> WeightsBuilder:
        return WeightsBuilder()


class WeightsBuilder:
    def __init__(self):
        self._weights = Weights()

    def build(self) -> Weights:
        return self._weights

    def keyword_setting(self, keyword_setting: KeywordSetting) -> WeightsBuilder:
        self._weights.keyword_setting = keyword_setting
        return self

    def vector_setting(self, vector_setting: VectorSetting) -> WeightsBuilder:
        self._weights.vector_setting = vector_setting
        return self


class RetrievalModel(BaseModel):
    search_method: SearchMethod | None = None
    reranking_enable: bool | None = None
    reranking_mode: str | None = None
    reranking_model: RerankingModel | None = None
    weights: Weights | None = None
    top_k: int | None = None
    score_threshold_enabled: bool | None = None
    score_threshold: float | None = None
    metadata_filtering_conditions: MetadataFilteringConditions | None = None

    @staticmethod
    def builder() -> RetrievalModelBuilder:
        return RetrievalModelBuilder()


class RetrievalModelBuilder:
    def __init__(self):
        self._retrieval_model = RetrievalModel()

    def build(self) -> RetrievalModel:
        return self._retrieval_model

    def search_method(self, search_method: SearchMethod) -> RetrievalModelBuilder:
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

    def weights(self, weights: Weights) -> RetrievalModelBuilder:
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

    def metadata_filtering_conditions(
        self, metadata_filtering_conditions: MetadataFilteringConditions
    ) -> RetrievalModelBuilder:
        self._retrieval_model.metadata_filtering_conditions = metadata_filtering_conditions
        return self
