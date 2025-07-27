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
