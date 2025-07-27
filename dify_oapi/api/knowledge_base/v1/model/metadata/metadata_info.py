from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class MetadataInfo(BaseModel):
    id: str
    name: str
    type: str
    use_count: Optional[int] = None