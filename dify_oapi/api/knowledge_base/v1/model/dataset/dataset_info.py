from __future__ import annotations

from pydantic import BaseModel

from ..tag.tag_info import TagInfo
from .external_knowledge_info import ExternalKnowledgeInfo
from .retrieval_model import RetrievalModel


class DatasetInfo(BaseModel):
    id: str | None = None
    name: str | None = None
    description: str | None = None
    provider: str | None = None
    permission: str | None = None
    data_source_type: str | None = None
    indexing_technique: str | None = None
    app_count: int | None = None
    document_count: int | None = None
    word_count: int | None = None
    created_by: str | None = None
    created_at: int | None = None
    updated_by: str | None = None
    updated_at: int | None = None
    embedding_model: str | None = None
    embedding_model_provider: str | None = None
    embedding_available: bool | None = None
    retrieval_model_dict: RetrievalModel | None = None
    tags: list[TagInfo] | None = None
    doc_form: str | None = None
    external_knowledge_info: ExternalKnowledgeInfo | None = None
    external_retrieval_model: RetrievalModel | None = None
    partial_member_list: list[str] | None = None
