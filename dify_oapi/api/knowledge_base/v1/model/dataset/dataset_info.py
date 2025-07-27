from __future__ import annotations

from typing import Optional, List

from pydantic import BaseModel

from .external_knowledge_info import ExternalKnowledgeInfo
from .retrieval_model import RetrievalModel
from ..tag.tag_info import TagInfo


class DatasetInfo(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    provider: Optional[str] = None
    permission: Optional[str] = None
    data_source_type: Optional[str] = None
    indexing_technique: Optional[str] = None
    app_count: Optional[int] = None
    document_count: Optional[int] = None
    word_count: Optional[int] = None
    created_by: Optional[str] = None
    created_at: Optional[int] = None
    updated_by: Optional[str] = None
    updated_at: Optional[int] = None
    embedding_model: Optional[str] = None
    embedding_model_provider: Optional[str] = None
    embedding_available: Optional[bool] = None
    retrieval_model_dict: Optional[RetrievalModel] = None
    tags: Optional[List[TagInfo]] = None
    doc_form: Optional[str] = None
    external_knowledge_info: Optional[ExternalKnowledgeInfo] = None
    external_retrieval_model: Optional[RetrievalModel] = None
    partial_member_list: Optional[List[str]] = None


