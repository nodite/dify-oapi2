from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel
from dify_oapi.core.model.base_response import BaseResponse


class RetrieveResponse(BaseResponse):
    query: Optional[QueryInfo] = None
    records: Optional[List[RetrievalRecord]] = None


class QueryInfo(BaseModel):
    content: Optional[str] = None


class RetrievalRecord(BaseModel):
    segment: Optional[SegmentInfo] = None
    score: Optional[float] = None
    tsne_position: Optional[dict] = None


class SegmentInfo(BaseModel):
    id: Optional[str] = None
    position: Optional[int] = None
    document_id: Optional[str] = None
    content: Optional[str] = None
    answer: Optional[str] = None
    word_count: Optional[int] = None
    tokens: Optional[int] = None
    keywords: Optional[List[str]] = None
    index_node_id: Optional[str] = None
    index_node_hash: Optional[str] = None
    hit_count: Optional[int] = None
    enabled: Optional[bool] = None
    disabled_at: Optional[int] = None
    disabled_by: Optional[str] = None
    status: Optional[str] = None
    created_by: Optional[str] = None
    created_at: Optional[int] = None
    indexing_at: Optional[int] = None
    completed_at: Optional[int] = None
    error: Optional[str] = None
    stopped_at: Optional[int] = None
    document: Optional[DocumentInfo] = None


class DocumentInfo(BaseModel):
    id: Optional[str] = None
    data_source_type: Optional[str] = None
    name: Optional[str] = None
