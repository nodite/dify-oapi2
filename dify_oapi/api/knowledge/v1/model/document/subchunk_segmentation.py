from __future__ import annotations

from pydantic import BaseModel


class SubchunkSegmentation(BaseModel):
    """Sub-chunk segmentation rule model for hierarchical document segmentation."""

    separator: str | None = None
    max_tokens: int | None = None
    chunk_overlap: int | None = None

    @staticmethod
    def builder() -> SubchunkSegmentationBuilder:
        return SubchunkSegmentationBuilder()


class SubchunkSegmentationBuilder:
    def __init__(self):
        self._subchunk_segmentation = SubchunkSegmentation()

    def build(self) -> SubchunkSegmentation:
        return self._subchunk_segmentation

    def separator(self, separator: str) -> SubchunkSegmentationBuilder:
        self._subchunk_segmentation.separator = separator
        return self

    def max_tokens(self, max_tokens: int) -> SubchunkSegmentationBuilder:
        self._subchunk_segmentation.max_tokens = max_tokens
        return self

    def chunk_overlap(self, chunk_overlap: int) -> SubchunkSegmentationBuilder:
        self._subchunk_segmentation.chunk_overlap = chunk_overlap
        return self
