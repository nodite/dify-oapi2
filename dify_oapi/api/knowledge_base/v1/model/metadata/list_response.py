from __future__ import annotations

from typing import List

from pydantic import BaseModel

from dify_oapi.api.knowledge_base.v1.model.dataset.metadata_info import MetadataInfo


class ListResponse(BaseModel):
    doc_metadata: List[MetadataInfo]
    built_in_field_enabled: bool

    @staticmethod
    def builder() -> ListResponseBuilder:
        return ListResponseBuilder()


class ListResponseBuilder:
    def __init__(self):
        self._response = ListResponse(doc_metadata=[], built_in_field_enabled=False)

    def build(self) -> ListResponse:
        return self._response

    def doc_metadata(self, doc_metadata: List[MetadataInfo]) -> ListResponseBuilder:
        self._response.doc_metadata = doc_metadata
        return self

    def built_in_field_enabled(self, built_in_field_enabled: bool) -> ListResponseBuilder:
        self._response.built_in_field_enabled = built_in_field_enabled
        return self