from __future__ import annotations

from typing import Optional, Union

from pydantic import BaseModel


class FilterCondition(BaseModel):
    name: str
    comparison_operator: str
    value: Optional[Union[str, int, float]] = None

    @staticmethod
    def builder() -> FilterConditionBuilder:
        return FilterConditionBuilder()


class FilterConditionBuilder:
    def __init__(self):
        self._filter_condition = FilterCondition(name="", comparison_operator="")

    def build(self) -> FilterCondition:
        return self._filter_condition

    def name(self, name: str) -> FilterConditionBuilder:
        self._filter_condition.name = name
        return self

    def comparison_operator(self, comparison_operator: str) -> FilterConditionBuilder:
        self._filter_condition.comparison_operator = comparison_operator
        return self

    def value(self, value: Union[str, int, float]) -> FilterConditionBuilder:
        self._filter_condition.value = value
        return self