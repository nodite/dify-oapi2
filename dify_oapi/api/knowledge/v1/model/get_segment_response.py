"""Get segment response model."""

from dify_oapi.core.model.base_response import BaseResponse

from .segment_info import SegmentInfo


class GetSegmentResponse(SegmentInfo, BaseResponse):
    """Response model for get segment API."""

    pass
