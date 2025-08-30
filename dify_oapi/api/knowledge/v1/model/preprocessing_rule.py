"""Preprocessing rule model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel

from .knowledge_types import PreprocessingRuleId


class PreprocessingRule(BaseModel):
    """Preprocessing rule model with builder pattern."""

    id: Optional[PreprocessingRuleId] = None
    enabled: Optional[bool] = None

    @staticmethod
    def builder() -> "PreprocessingRuleBuilder":
        return PreprocessingRuleBuilder()


class PreprocessingRuleBuilder:
    """Builder for PreprocessingRule."""

    def __init__(self):
        self._preprocessing_rule = PreprocessingRule()

    def build(self) -> PreprocessingRule:
        return self._preprocessing_rule

    def id(self, id: PreprocessingRuleId) -> "PreprocessingRuleBuilder":
        self._preprocessing_rule.id = id
        return self

    def enabled(self, enabled: bool) -> "PreprocessingRuleBuilder":
        self._preprocessing_rule.enabled = enabled
        return self
