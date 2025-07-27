from __future__ import annotations

from typing import List

from pydantic import BaseModel

from .filter_condition import FilterCondition


class MetadataFilteringConditions(BaseModel):
    logical_operator: str
    conditions: List[FilterCondition]

