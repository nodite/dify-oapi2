from __future__ import annotations

from pydantic import BaseModel

from .indexing_status_info import IndexingStatusInfo


class IndexingStatusResponse(BaseModel):
    """Response model for indexing status API"""

    data: list[IndexingStatusInfo] | None = None
