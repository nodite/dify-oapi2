from __future__ import annotations

from pydantic import BaseModel


class TagInfo(BaseModel):
    id: str
    name: str
    type: str | None = None
    binding_count: int | None = None
