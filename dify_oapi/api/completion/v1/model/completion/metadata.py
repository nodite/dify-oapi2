from __future__ import annotations

from pydantic import BaseModel

from .retriever_resource import RetrieverResource
from .usage import Usage


class Metadata(BaseModel):
    usage: Usage | None = None
    retriever_resources: list[RetrieverResource] | None = None

    @staticmethod
    def builder() -> MetadataBuilder:
        return MetadataBuilder()


class MetadataBuilder:
    def __init__(self):
        self._metadata = Metadata()

    def build(self) -> Metadata:
        return self._metadata

    def usage(self, usage: Usage) -> MetadataBuilder:
        self._metadata.usage = usage
        return self

    def retriever_resources(self, retriever_resources: list[RetrieverResource]) -> MetadataBuilder:
        self._metadata.retriever_resources = retriever_resources
        return self
