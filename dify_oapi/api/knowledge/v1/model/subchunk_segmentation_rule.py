"""Sub-chunk segmentation rule model for Knowledge Base API."""

from pydantic import BaseModel


class SubChunkSegmentationRule(BaseModel):
    """Sub-chunk segmentation rule model with builder pattern."""

    separator: str | None = None
    max_tokens: int | None = None
    chunk_overlap: int | None = None

    @staticmethod
    def builder() -> "SubChunkSegmentationRuleBuilder":
        return SubChunkSegmentationRuleBuilder()


class SubChunkSegmentationRuleBuilder:
    """Builder for SubChunkSegmentationRule."""

    def __init__(self):
        self._subchunk_segmentation_rule = SubChunkSegmentationRule()

    def build(self) -> SubChunkSegmentationRule:
        return self._subchunk_segmentation_rule

    def separator(self, separator: str) -> "SubChunkSegmentationRuleBuilder":
        self._subchunk_segmentation_rule.separator = separator
        return self

    def max_tokens(self, max_tokens: int) -> "SubChunkSegmentationRuleBuilder":
        self._subchunk_segmentation_rule.max_tokens = max_tokens
        return self

    def chunk_overlap(self, chunk_overlap: int) -> "SubChunkSegmentationRuleBuilder":
        self._subchunk_segmentation_rule.chunk_overlap = chunk_overlap
        return self
