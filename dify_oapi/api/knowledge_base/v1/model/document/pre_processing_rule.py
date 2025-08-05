from __future__ import annotations

from typing import Literal

from pydantic import BaseModel


class PreProcessingRule(BaseModel):
    """Pre-processing rule model for document preprocessing configuration."""

    id: str | None = None
    enabled: bool | None = None

    @staticmethod
    def builder() -> PreProcessingRuleBuilder:
        return PreProcessingRuleBuilder()


class PreProcessingRuleBuilder:
    def __init__(self):
        self._pre_processing_rule = PreProcessingRule()

    def build(self) -> PreProcessingRule:
        return self._pre_processing_rule

    def id(self, id: Literal["remove_extra_spaces", "remove_urls_emails"]) -> PreProcessingRuleBuilder:
        self._pre_processing_rule.id = id
        return self

    def enabled(self, enabled: bool) -> PreProcessingRuleBuilder:
        self._pre_processing_rule.enabled = enabled
        return self
