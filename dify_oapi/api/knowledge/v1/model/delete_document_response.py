"""Delete document response model."""

from dify_oapi.core.model.base_response import BaseResponse


class DeleteDocumentResponse(BaseResponse):
    """Response model for delete document API."""

    result: str | None = None
