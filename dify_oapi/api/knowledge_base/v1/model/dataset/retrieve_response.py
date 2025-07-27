from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from dify_oapi.core.model.base_response import BaseResponse


class RetrieveResponse(BaseResponse):
    query: QueryInfo | None = None
    records: list[RetrievalRecord] | None = None


class QueryInfo(BaseModel):
    content: str | None = None


class RetrievalRecord(BaseModel):
    segment: SegmentInfo | None = None
    score: float | None = None
    tsne_position: dict[str, Any] | None = None


class SegmentInfo(BaseModel):
    id: str | None = None
    position: int | None = None
    document_id: str | None = None
    content: str | None = None
    answer: str | None = None
    word_count: int | None = None
    tokens: int | None = None
    keywords: list[str] | None = None
    index_node_id: str | None = None
    index_node_hash: str | None = None
    hit_count: int | None = None
    enabled: bool | None = None
    disabled_at: int | None = None
    disabled_by: str | None = None
    status: str | None = None
    created_by: str | None = None
    created_at: int | None = None
    indexing_at: int | None = None
    completed_at: int | None = None
    error: str | None = None
    stopped_at: int | None = None
    document: DocumentInfo | None = None


class DocumentInfo(BaseModel):
    id: str | None = None
    data_source_type: str | None = None
    name: str | None = None
