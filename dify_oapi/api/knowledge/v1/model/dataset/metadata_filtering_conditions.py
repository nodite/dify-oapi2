from __future__ import annotations

from pydantic import BaseModel

from .filter_condition import FilterCondition


class MetadataFilteringConditions(BaseModel):
    logical_operator: str
    conditions: list[FilterCondition]

    @staticmethod
    def builder() -> MetadataFilteringConditionsBuilder:
        return MetadataFilteringConditionsBuilder()


class MetadataFilteringConditionsBuilder:
    def __init__(self):
        self._metadata_filtering_conditions = MetadataFilteringConditions(logical_operator="", conditions=[])

    def build(self) -> MetadataFilteringConditions:
        return self._metadata_filtering_conditions

    def logical_operator(self, logical_operator: str) -> MetadataFilteringConditionsBuilder:
        self._metadata_filtering_conditions.logical_operator = logical_operator
        return self

    def conditions(self, conditions: list[FilterCondition]) -> MetadataFilteringConditionsBuilder:
        self._metadata_filtering_conditions.conditions = conditions
        return self
