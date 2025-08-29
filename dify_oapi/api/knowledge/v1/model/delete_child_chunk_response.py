"""Delete child chunk response model."""

from dify_oapi.core.model.base_response import BaseResponse


class DeleteChildChunkResponse(BaseResponse):
    """Response model for delete child chunk API."""

    result: str | None = None
