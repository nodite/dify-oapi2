"""Get segment response model."""

from dify_oapi.core.model.base_response import BaseResponse

from .segment_info import SegmentInfo


class GetSegmentResponse(BaseResponse):
    """Response model for get segment API."""

    data: SegmentInfo | None = None
    doc_form: str | None = None
