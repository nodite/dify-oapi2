from __future__ import annotations

from typing import List

from pydantic import BaseModel

from .filter_condition import FilterCondition


class MetadataFilteringConditions(BaseModel):
    logical_operator: str
    conditions: List[FilterCondition]

    @staticmethod
    def builder() -> MetadataFilteringConditionsBuilder:
        return MetadataFilteringConditionsBuilder()


class MetadataFilteringConditionsBuilder:
    def __init__(self):
        self._metadata_filtering_conditions = MetadataFilteringConditions(logical_operator="and", conditions=[])

    def build(self) -> MetadataFilteringConditions:
        return self._metadata_filtering_conditions

    def logical_operator(self, logical_operator: str) -> MetadataFilteringConditionsBuilder:
        self._metadata_filtering_conditions.logical_operator = logical_operator
        return self

    def conditions(self, conditions: List[FilterCondition]) -> MetadataFilteringConditionsBuilder:
        self._metadata_filtering_conditions.conditions = conditions
        return self

    def add_condition(self, condition: FilterCondition) -> MetadataFilteringConditionsBuilder:
        self._metadata_filtering_conditions.conditions.append(condition)
        return self