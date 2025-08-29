from pydantic import BaseModel

from .segment_info import SegmentInfo


class RetrievalRecord(BaseModel):
    segment: SegmentInfo | None = None
    score: float | None = None

    @staticmethod
    def builder() -> "RetrievalRecordBuilder":
        return RetrievalRecordBuilder()


class RetrievalRecordBuilder:
    def __init__(self) -> None:
        self._retrieval_record = RetrievalRecord()

    def build(self) -> RetrievalRecord:
        return self._retrieval_record

    def segment(self, segment: SegmentInfo) -> "RetrievalRecordBuilder":
        self._retrieval_record.segment = segment
        return self

    def score(self, score: float) -> "RetrievalRecordBuilder":
        self._retrieval_record.score = score
        return self
