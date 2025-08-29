from __future__ import annotations

from pydantic import BaseModel


class Segmentation(BaseModel):
    """Segmentation rule model for document text segmentation configuration."""

    separator: str | None = None
    max_tokens: int | None = None
    chunk_overlap: int | None = None

    @staticmethod
    def builder() -> SegmentationBuilder:
        return SegmentationBuilder()


class SegmentationBuilder:
    def __init__(self):
        self._segmentation = Segmentation()

    def build(self) -> Segmentation:
        return self._segmentation

    def separator(self, separator: str) -> SegmentationBuilder:
        self._segmentation.separator = separator
        return self

    def max_tokens(self, max_tokens: int) -> SegmentationBuilder:
        self._segmentation.max_tokens = max_tokens
        return self

    def chunk_overlap(self, chunk_overlap: int) -> SegmentationBuilder:
        self._segmentation.chunk_overlap = chunk_overlap
        return self
