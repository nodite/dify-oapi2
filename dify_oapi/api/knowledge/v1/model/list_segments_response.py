"""List segments response model."""

from dify_oapi.core.model.base_response import BaseResponse

from .segment_info import SegmentInfo


class ListSegmentsResponse(BaseResponse):
    """Response model for list segments API."""

    data: list[SegmentInfo] | None = None
    has_more: bool | None = None
    limit: int | None = None
    total: int | None = None
    page: int | None = None
