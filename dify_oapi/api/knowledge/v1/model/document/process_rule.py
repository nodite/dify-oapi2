from __future__ import annotations

from typing import Literal

from pydantic import BaseModel

from .rules import Rules


class ProcessRule(BaseModel):
    """Processing rule model for document processing configuration."""

    mode: str | None = None
    rules: Rules | None = None

    @staticmethod
    def builder() -> ProcessRuleBuilder:
        return ProcessRuleBuilder()


class ProcessRuleBuilder:
    def __init__(self):
        self._process_rule = ProcessRule()

    def build(self) -> ProcessRule:
        return self._process_rule

    def mode(self, mode: Literal["automatic", "custom"]) -> ProcessRuleBuilder:
        self._process_rule.mode = mode
        return self

    def rules(self, rules: Rules) -> ProcessRuleBuilder:
        self._process_rule.rules = rules
        return self
