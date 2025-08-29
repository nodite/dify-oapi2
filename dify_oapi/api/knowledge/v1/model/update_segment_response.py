"""Update segment response model."""

from dify_oapi.core.model.base_response import BaseResponse

from .segment_info import SegmentInfo


class UpdateSegmentResponse(SegmentInfo, BaseResponse):
    """Response model for update segment API."""

    pass
