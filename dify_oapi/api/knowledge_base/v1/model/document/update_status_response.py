"""Update status response model for document API."""

from dify_oapi.core.model.base_response import BaseResponse


class UpdateStatusResponse(BaseResponse):
    """Response model for updating document status."""

    result: str | None = None
