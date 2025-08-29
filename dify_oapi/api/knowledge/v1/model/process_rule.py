"""Process rule model for Knowledge Base API."""

from typing import Any, Optional

from pydantic import BaseModel

from .knowledge_types import ProcessingMode


class ProcessRule(BaseModel):
    """Process rule model with builder pattern."""

    mode: Optional[ProcessingMode] = None
    rules: Optional[dict[str, Any]] = None

    @staticmethod
    def builder() -> "ProcessRuleBuilder":
        return ProcessRuleBuilder()


class ProcessRuleBuilder:
    """Builder for ProcessRule."""

    def __init__(self):
        self._process_rule = ProcessRule()

    def build(self) -> ProcessRule:
        return self._process_rule

    def mode(self, mode: ProcessingMode) -> "ProcessRuleBuilder":
        self._process_rule.mode = mode
        return self

    def rules(self, rules: dict[str, Any]) -> "ProcessRuleBuilder":
        self._process_rule.rules = rules
        return self
