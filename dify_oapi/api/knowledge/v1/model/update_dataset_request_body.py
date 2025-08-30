from pydantic import BaseModel

from .embedding_model_parameters import EmbeddingModelParameters
from .knowledge_types import IndexingTechnique, Permission
from .retrieval_model import RetrievalModel


class UpdateDatasetRequestBody(BaseModel):
    name: str | None = None
    description: str | None = None
    indexing_technique: IndexingTechnique | None = None
    permission: Permission | None = None
    provider: str | None = None
    model: str | None = None
    embedding_model_parameters: EmbeddingModelParameters | None = None
    retrieval_model: RetrievalModel | None = None

    @staticmethod
    def builder() -> "UpdateDatasetRequestBodyBuilder":
        return UpdateDatasetRequestBodyBuilder()


class UpdateDatasetRequestBodyBuilder:
    def __init__(self) -> None:
        self._update_dataset_request_body = UpdateDatasetRequestBody()

    def build(self) -> UpdateDatasetRequestBody:
        return self._update_dataset_request_body

    def name(self, name: str) -> "UpdateDatasetRequestBodyBuilder":
        self._update_dataset_request_body.name = name
        return self

    def description(self, description: str) -> "UpdateDatasetRequestBodyBuilder":
        self._update_dataset_request_body.description = description
        return self

    def indexing_technique(self, indexing_technique: IndexingTechnique) -> "UpdateDatasetRequestBodyBuilder":
        self._update_dataset_request_body.indexing_technique = indexing_technique
        return self

    def permission(self, permission: Permission) -> "UpdateDatasetRequestBodyBuilder":
        self._update_dataset_request_body.permission = permission
        return self

    def provider(self, provider: str) -> "UpdateDatasetRequestBodyBuilder":
        self._update_dataset_request_body.provider = provider
        return self

    def model(self, model: str) -> "UpdateDatasetRequestBodyBuilder":
        self._update_dataset_request_body.model = model
        return self

    def embedding_model_parameters(
        self, embedding_model_parameters: EmbeddingModelParameters
    ) -> "UpdateDatasetRequestBodyBuilder":
        self._update_dataset_request_body.embedding_model_parameters = embedding_model_parameters
        return self

    def retrieval_model(self, retrieval_model: RetrievalModel) -> "UpdateDatasetRequestBodyBuilder":
        self._update_dataset_request_body.retrieval_model = retrieval_model
        return self
