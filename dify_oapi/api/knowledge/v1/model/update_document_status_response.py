"""Update document status response model."""

from dify_oapi.core.model.base_response import BaseResponse


class UpdateDocumentStatusResponse(BaseResponse):
    """Response model for update document status API."""

    result: str | None = None
