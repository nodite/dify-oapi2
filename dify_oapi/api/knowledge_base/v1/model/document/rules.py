from __future__ import annotations

from pydantic import BaseModel

from .pre_processing_rule import PreProcessingRule
from .segmentation import Segmentation


class Rules(BaseModel):
    pre_processing_rules: list[PreProcessingRule] | None = None
    segmentation: Segmentation | None = None

    @staticmethod
    def builder() -> RulesBuilder:
        return RulesBuilder()


class RulesBuilder:
    def __init__(self):
        self._rules = Rules()

    def build(self) -> Rules:
        return self._rules

    def pre_processing_rules(self, pre_processing_rules: list[PreProcessingRule]) -> RulesBuilder:
        self._rules.pre_processing_rules = pre_processing_rules
        return self

    def segmentation(self, segmentation: Segmentation) -> RulesBuilder:
        self._rules.segmentation = segmentation
        return self
