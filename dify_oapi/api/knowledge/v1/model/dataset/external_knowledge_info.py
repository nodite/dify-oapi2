from __future__ import annotations

from pydantic import BaseModel


class ExternalKnowledgeInfo(BaseModel):
    external_knowledge_id: str | None = None
    external_knowledge_api_id: str | None = None
    external_knowledge_api_name: str | None = None
    external_knowledge_api_endpoint: str | None = None

    @staticmethod
    def builder() -> ExternalKnowledgeInfoBuilder:
        return ExternalKnowledgeInfoBuilder()


class ExternalKnowledgeInfoBuilder:
    def __init__(self):
        self._external_knowledge_info = ExternalKnowledgeInfo()

    def build(self) -> ExternalKnowledgeInfo:
        return self._external_knowledge_info

    def external_knowledge_id(self, external_knowledge_id: str) -> ExternalKnowledgeInfoBuilder:
        self._external_knowledge_info.external_knowledge_id = external_knowledge_id
        return self

    def external_knowledge_api_id(self, external_knowledge_api_id: str) -> ExternalKnowledgeInfoBuilder:
        self._external_knowledge_info.external_knowledge_api_id = external_knowledge_api_id
        return self

    def external_knowledge_api_name(self, external_knowledge_api_name: str) -> ExternalKnowledgeInfoBuilder:
        self._external_knowledge_info.external_knowledge_api_name = external_knowledge_api_name
        return self

    def external_knowledge_api_endpoint(self, external_knowledge_api_endpoint: str) -> ExternalKnowledgeInfoBuilder:
        self._external_knowledge_info.external_knowledge_api_endpoint = external_knowledge_api_endpoint
        return self
