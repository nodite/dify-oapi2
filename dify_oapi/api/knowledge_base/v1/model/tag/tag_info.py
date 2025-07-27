from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class TagInfo(BaseModel):
    id: str
    name: str
    type: Optional[str] = None
    binding_count: Optional[int] = None