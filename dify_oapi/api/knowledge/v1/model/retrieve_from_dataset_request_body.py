from pydantic import BaseModel

from .retrieval_model import RetrievalModel


class RetrieveFromDatasetRequestBody(BaseModel):
    query: str | None = None
    retrieval_model: RetrievalModel | None = None
    top_k: int | None = None
    score_threshold: float | None = None

    @staticmethod
    def builder() -> "RetrieveFromDatasetRequestBodyBuilder":
        return RetrieveFromDatasetRequestBodyBuilder()


class RetrieveFromDatasetRequestBodyBuilder:
    def __init__(self) -> None:
        self._retrieve_from_dataset_request_body = RetrieveFromDatasetRequestBody()

    def build(self) -> RetrieveFromDatasetRequestBody:
        return self._retrieve_from_dataset_request_body

    def query(self, query: str) -> "RetrieveFromDatasetRequestBodyBuilder":
        self._retrieve_from_dataset_request_body.query = query
        return self

    def retrieval_model(self, retrieval_model: RetrievalModel) -> "RetrieveFromDatasetRequestBodyBuilder":
        self._retrieve_from_dataset_request_body.retrieval_model = retrieval_model
        return self

    def top_k(self, top_k: int) -> "RetrieveFromDatasetRequestBodyBuilder":
        self._retrieve_from_dataset_request_body.top_k = top_k
        return self

    def score_threshold(self, score_threshold: float) -> "RetrieveFromDatasetRequestBodyBuilder":
        self._retrieve_from_dataset_request_body.score_threshold = score_threshold
        return self
