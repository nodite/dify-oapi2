"""Segmentation rule model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel


class SegmentationRule(BaseModel):
    """Segmentation rule model with builder pattern."""

    separator: Optional[str] = None
    max_tokens: Optional[int] = None
    chunk_overlap: Optional[int] = None
    rules: Optional[dict] = None

    @staticmethod
    def builder() -> "SegmentationRuleBuilder":
        return SegmentationRuleBuilder()


class SegmentationRuleBuilder:
    """Builder for SegmentationRule."""

    def __init__(self):
        self._segmentation_rule = SegmentationRule()

    def build(self) -> SegmentationRule:
        return self._segmentation_rule

    def separator(self, separator: str) -> "SegmentationRuleBuilder":
        self._segmentation_rule.separator = separator
        return self

    def max_tokens(self, max_tokens: int) -> "SegmentationRuleBuilder":
        self._segmentation_rule.max_tokens = max_tokens
        return self

    def chunk_overlap(self, chunk_overlap: int) -> "SegmentationRuleBuilder":
        self._segmentation_rule.chunk_overlap = chunk_overlap
        return self

    def rules(self, rules: dict) -> "SegmentationRuleBuilder":
        self._segmentation_rule.rules = rules
        return self
