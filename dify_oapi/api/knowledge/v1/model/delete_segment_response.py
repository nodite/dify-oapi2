"""Delete segment response model."""

from dify_oapi.core.model.base_response import BaseResponse


class DeleteSegmentResponse(BaseResponse):
    """Response model for delete segment API."""

    result: str | None = None
