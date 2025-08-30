"""Create segment response model."""

from dify_oapi.core.model.base_response import BaseResponse

from .segment_info import SegmentInfo


class CreateSegmentResponse(BaseResponse):
    """Response model for create segment API."""

    data: list[SegmentInfo] | None = None
