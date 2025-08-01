from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .indexing_status_info import IndexingStatusInfo


class IndexingStatusResponse(BaseResponse):
    """Response model for indexing status API"""

    data: list[IndexingStatusInfo] | None = None
