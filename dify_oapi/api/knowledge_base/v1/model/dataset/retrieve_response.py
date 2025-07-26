from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class RetrieveDatasetResponse(BaseModel):
    query: QueryInfo
    records: List[RetrievalRecord]

    @staticmethod
    def builder() -> RetrieveDatasetResponseBuilder:
        return RetrieveDatasetResponseBuilder()


class QueryInfo(BaseModel):
    content: str

    @staticmethod
    def builder() -> QueryInfoBuilder:
        return QueryInfoBuilder()


class RetrievalRecord(BaseModel):
    segment: SegmentInfo
    score: float
    tsne_position: Optional[dict] = None

    @staticmethod
    def builder() -> RetrievalRecordBuilder:
        return RetrievalRecordBuilder()


class SegmentInfo(BaseModel):
    id: str
    position: int
    document_id: str
    content: str
    answer: Optional[str] = None
    word_count: int
    tokens: int
    keywords: List[str]
    index_node_id: str
    index_node_hash: str
    hit_count: int
    enabled: bool
    disabled_at: Optional[int] = None
    disabled_by: Optional[str] = None
    status: str
    created_by: str
    created_at: int
    indexing_at: int
    completed_at: int
    error: Optional[str] = None
    stopped_at: Optional[int] = None
    document: DocumentInfo

    @staticmethod
    def builder() -> SegmentInfoBuilder:
        return SegmentInfoBuilder()


class DocumentInfo(BaseModel):
    id: str
    data_source_type: str
    name: str

    @staticmethod
    def builder() -> DocumentInfoBuilder:
        return DocumentInfoBuilder()


# Builder classes
class RetrieveDatasetResponseBuilder:
    def __init__(self):
        self._response = RetrieveDatasetResponse(
            query=QueryInfo(content=""),
            records=[]
        )

    def build(self) -> RetrieveDatasetResponse:
        return self._response

    def query(self, query: QueryInfo) -> RetrieveDatasetResponseBuilder:
        self._response.query = query
        return self

    def records(self, records: List[RetrievalRecord]) -> RetrieveDatasetResponseBuilder:
        self._response.records = records
        return self


class QueryInfoBuilder:
    def __init__(self):
        self._query = QueryInfo(content="")

    def build(self) -> QueryInfo:
        return self._query

    def content(self, content: str) -> QueryInfoBuilder:
        self._query.content = content
        return self


class RetrievalRecordBuilder:
    def __init__(self):
        self._record = RetrievalRecord(
            segment=SegmentInfo(
                id="", position=0, document_id="", content="", word_count=0,
                tokens=0, keywords=[], index_node_id="", index_node_hash="",
                hit_count=0, enabled=True, status="", created_by="",
                created_at=0, indexing_at=0, completed_at=0,
                document=DocumentInfo(id="", data_source_type="", name="")
            ),
            score=0.0
        )

    def build(self) -> RetrievalRecord:
        return self._record

    def segment(self, segment: SegmentInfo) -> RetrievalRecordBuilder:
        self._record.segment = segment
        return self

    def score(self, score: float) -> RetrievalRecordBuilder:
        self._record.score = score
        return self

    def tsne_position(self, tsne_position: dict) -> RetrievalRecordBuilder:
        self._record.tsne_position = tsne_position
        return self


class SegmentInfoBuilder:
    def __init__(self):
        self._segment = SegmentInfo(
            id="", position=0, document_id="", content="", word_count=0,
            tokens=0, keywords=[], index_node_id="", index_node_hash="",
            hit_count=0, enabled=True, status="", created_by="",
            created_at=0, indexing_at=0, completed_at=0,
            document=DocumentInfo(id="", data_source_type="", name="")
        )

    def build(self) -> SegmentInfo:
        return self._segment

    def id(self, id: str) -> SegmentInfoBuilder:
        self._segment.id = id
        return self

    def position(self, position: int) -> SegmentInfoBuilder:
        self._segment.position = position
        return self

    def document_id(self, document_id: str) -> SegmentInfoBuilder:
        self._segment.document_id = document_id
        return self

    def content(self, content: str) -> SegmentInfoBuilder:
        self._segment.content = content
        return self

    def answer(self, answer: str) -> SegmentInfoBuilder:
        self._segment.answer = answer
        return self

    def word_count(self, word_count: int) -> SegmentInfoBuilder:
        self._segment.word_count = word_count
        return self

    def tokens(self, tokens: int) -> SegmentInfoBuilder:
        self._segment.tokens = tokens
        return self

    def keywords(self, keywords: List[str]) -> SegmentInfoBuilder:
        self._segment.keywords = keywords
        return self

    def index_node_id(self, index_node_id: str) -> SegmentInfoBuilder:
        self._segment.index_node_id = index_node_id
        return self

    def index_node_hash(self, index_node_hash: str) -> SegmentInfoBuilder:
        self._segment.index_node_hash = index_node_hash
        return self

    def hit_count(self, hit_count: int) -> SegmentInfoBuilder:
        self._segment.hit_count = hit_count
        return self

    def enabled(self, enabled: bool) -> SegmentInfoBuilder:
        self._segment.enabled = enabled
        return self

    def disabled_at(self, disabled_at: int) -> SegmentInfoBuilder:
        self._segment.disabled_at = disabled_at
        return self

    def disabled_by(self, disabled_by: str) -> SegmentInfoBuilder:
        self._segment.disabled_by = disabled_by
        return self

    def status(self, status: str) -> SegmentInfoBuilder:
        self._segment.status = status
        return self

    def created_by(self, created_by: str) -> SegmentInfoBuilder:
        self._segment.created_by = created_by
        return self

    def created_at(self, created_at: int) -> SegmentInfoBuilder:
        self._segment.created_at = created_at
        return self

    def indexing_at(self, indexing_at: int) -> SegmentInfoBuilder:
        self._segment.indexing_at = indexing_at
        return self

    def completed_at(self, completed_at: int) -> SegmentInfoBuilder:
        self._segment.completed_at = completed_at
        return self

    def error(self, error: str) -> SegmentInfoBuilder:
        self._segment.error = error
        return self

    def stopped_at(self, stopped_at: int) -> SegmentInfoBuilder:
        self._segment.stopped_at = stopped_at
        return self

    def document(self, document: DocumentInfo) -> SegmentInfoBuilder:
        self._segment.document = document
        return self


class DocumentInfoBuilder:
    def __init__(self):
        self._document = DocumentInfo(id="", data_source_type="", name="")

    def build(self) -> DocumentInfo:
        return self._document

    def id(self, id: str) -> DocumentInfoBuilder:
        self._document.id = id
        return self

    def data_source_type(self, data_source_type: str) -> DocumentInfoBuilder:
        self._document.data_source_type = data_source_type
        return self

    def name(self, name: str) -> DocumentInfoBuilder:
        self._document.name = name
        return self