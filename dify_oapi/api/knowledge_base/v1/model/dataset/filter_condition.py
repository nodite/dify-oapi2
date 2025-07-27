from __future__ import annotations

from typing import Literal, Optional, Union

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
    value: Optional[Union[str, int, float]] = None
