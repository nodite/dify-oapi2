from __future__ import annotations

from typing import Literal

from pydantic import BaseModel


class FilterCondition(BaseModel):
    name: str
    comparison_operator: Literal[
        "contains",
        "not contains",
        "start with",
        "end with",
        "is",
        "is not",
        "empty",
        "not empty",
        "=",
        "≠",
        ">",
        "<",
        "≥",
        "≤",
        "before",
        "after",
    ]
    value: str | int | float | None = None

    @staticmethod
    def builder() -> FilterConditionBuilder:
        return FilterConditionBuilder()


class FilterConditionBuilder:
    def __init__(self):
        self._filter_condition = FilterCondition(name="", comparison_operator="contains")

    def build(self) -> FilterCondition:
        return self._filter_condition

    def name(self, name: str) -> FilterConditionBuilder:
        self._filter_condition.name = name
        return self

    def comparison_operator(
        self,
        comparison_operator: Literal[
            "contains",
            "not contains",
            "start with",
            "end with",
            "is",
            "is not",
            "empty",
            "not empty",
            "=",
            "≠",
            ">",
            "<",
            "≥",
            "≤",
            "before",
            "after",
        ],
    ) -> FilterConditionBuilder:
        self._filter_condition.comparison_operator = comparison_operator
        return self

    def value(self, value: str | int | float | None) -> FilterConditionBuilder:
        self._filter_condition.value = value
        return self
