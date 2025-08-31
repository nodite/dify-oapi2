"""External knowledge info model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel


class ExternalKnowledgeInfo(BaseModel):
    """External knowledge info model with builder pattern."""

    external_knowledge_id: Optional[str] = None
    external_knowledge_api_id: Optional[str] = None
    external_knowledge_api_name: Optional[str] = None
    external_knowledge_api_endpoint: Optional[str] = None

    @staticmethod
    def builder() -> "ExternalKnowledgeInfoBuilder":
        return ExternalKnowledgeInfoBuilder()


class ExternalKnowledgeInfoBuilder:
    """Builder for ExternalKnowledgeInfo."""

    def __init__(self):
        self._external_knowledge_info = ExternalKnowledgeInfo()

    def build(self) -> ExternalKnowledgeInfo:
        return self._external_knowledge_info

    def external_knowledge_api_id(self, external_knowledge_api_id: str) -> "ExternalKnowledgeInfoBuilder":
        self._external_knowledge_info.external_knowledge_api_id = external_knowledge_api_id
        return self

    def external_knowledge_id(self, external_knowledge_id: str) -> "ExternalKnowledgeInfoBuilder":
        self._external_knowledge_info.external_knowledge_id = external_knowledge_id
        return self

    def external_knowledge_api_name(self, external_knowledge_api_name: str) -> "ExternalKnowledgeInfoBuilder":
        self._external_knowledge_info.external_knowledge_api_name = external_knowledge_api_name
        return self

    def external_knowledge_api_endpoint(self, external_knowledge_api_endpoint: str) -> "ExternalKnowledgeInfoBuilder":
        self._external_knowledge_info.external_knowledge_api_endpoint = external_knowledge_api_endpoint
        return self
