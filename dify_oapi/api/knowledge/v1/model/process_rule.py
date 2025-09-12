"""Process rule model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel

from .knowledge_types import ProcessingMode
from .process_rules import ProcessRules


class ProcessRule(BaseModel):
    """Process rule model with builder pattern."""

    mode: Optional[ProcessingMode] = None
    rules: Optional[ProcessRules] = None

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

    def rules(self, rules: ProcessRules) -> "ProcessRuleBuilder":
        self._process_rule.rules = rules
        return self
