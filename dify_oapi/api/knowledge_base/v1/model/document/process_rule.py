from __future__ import annotations

from pydantic import BaseModel


class ProcessRule(BaseModel):
    """Processing rule model for document processing configuration."""

    mode: str | None = None
    rules: dict | None = None

    @staticmethod
    def builder() -> ProcessRuleBuilder:
        return ProcessRuleBuilder()


class ProcessRuleBuilder:
    def __init__(self):
        self._process_rule = ProcessRule()

    def build(self) -> ProcessRule:
        return self._process_rule

    def mode(self, mode: str) -> ProcessRuleBuilder:
        self._process_rule.mode = mode
        return self

    def rules(self, rules: dict) -> ProcessRuleBuilder:
        self._process_rule.rules = rules
        return self
