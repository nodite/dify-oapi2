"""Process rules model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel

from .knowledge_types import ParentMode
from .preprocessing_rule import PreprocessingRule
from .segmentation_rule import SegmentationRule
from .subchunk_segmentation_rule import SubChunkSegmentationRule


class ProcessRules(BaseModel):
    """Process rules model with builder pattern."""

    pre_processing_rules: Optional[list[PreprocessingRule]] = None
    segmentation: Optional[SegmentationRule] = None
    parent_mode: Optional[ParentMode] = None
    subchunk_segmentation: Optional[SubChunkSegmentationRule] = None

    @staticmethod
    def builder() -> "ProcessRulesBuilder":
        return ProcessRulesBuilder()


class ProcessRulesBuilder:
    """Builder for ProcessRules."""

    def __init__(self):
        self._process_rules = ProcessRules()

    def build(self) -> ProcessRules:
        return self._process_rules

    def pre_processing_rules(self, pre_processing_rules: list[PreprocessingRule]) -> "ProcessRulesBuilder":
        self._process_rules.pre_processing_rules = pre_processing_rules
        return self

    def segmentation(self, segmentation: SegmentationRule) -> "ProcessRulesBuilder":
        self._process_rules.segmentation = segmentation
        return self

    def parent_mode(self, parent_mode: ParentMode) -> "ProcessRulesBuilder":
        self._process_rules.parent_mode = parent_mode
        return self

    def subchunk_segmentation(self, subchunk_segmentation: SubChunkSegmentationRule) -> "ProcessRulesBuilder":
        self._process_rules.subchunk_segmentation = subchunk_segmentation
        return self
