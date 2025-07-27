from __future__ import annotations

from pydantic import BaseModel


class ExternalKnowledgeInfo(BaseModel):
    external_knowledge_id: str | None = None
    external_knowledge_api_id: str | None = None
    external_knowledge_api_name: str | None = None
    external_knowledge_api_endpoint: str | None = None
