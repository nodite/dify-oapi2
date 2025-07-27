from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class ExternalKnowledgeInfo(BaseModel):
    external_knowledge_id: Optional[str] = None
    external_knowledge_api_id: Optional[str] = None
    external_knowledge_api_name: Optional[str] = None
    external_knowledge_api_endpoint: Optional[str] = None

