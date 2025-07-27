from __future__ import annotations

from pydantic import BaseModel


class MetadataInfo(BaseModel):
    id: str
    name: str
    type: str
    use_count: int | None = None
