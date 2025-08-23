from __future__ import annotations

from pydantic import BaseModel


class RetrieverResource(BaseModel):
    position: int | None = None
    dataset_id: str | None = None
    dataset_name: str | None = None
    document_id: str | None = None
    document_name: str | None = None
    segment_id: str | None = None
    score: float | None = None
    content: str | None = None

    @staticmethod
    def builder() -> RetrieverResourceBuilder:
        return RetrieverResourceBuilder()


class RetrieverResourceBuilder:
    def __init__(self):
        self._retriever_resource = RetrieverResource()

    def build(self) -> RetrieverResource:
        return self._retriever_resource

    def position(self, position: int) -> RetrieverResourceBuilder:
        self._retriever_resource.position = position
        return self

    def dataset_id(self, dataset_id: str) -> RetrieverResourceBuilder:
        self._retriever_resource.dataset_id = dataset_id
        return self

    def dataset_name(self, dataset_name: str) -> RetrieverResourceBuilder:
        self._retriever_resource.dataset_name = dataset_name
        return self

    def document_id(self, document_id: str) -> RetrieverResourceBuilder:
        self._retriever_resource.document_id = document_id
        return self

    def document_name(self, document_name: str) -> RetrieverResourceBuilder:
        self._retriever_resource.document_name = document_name
        return self

    def segment_id(self, segment_id: str) -> RetrieverResourceBuilder:
        self._retriever_resource.segment_id = segment_id
        return self

    def score(self, score: float) -> RetrieverResourceBuilder:
        self._retriever_resource.score = score
        return self

    def content(self, content: str) -> RetrieverResourceBuilder:
        self._retriever_resource.content = content
        return self
