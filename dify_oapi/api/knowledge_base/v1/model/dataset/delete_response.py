from __future__ import annotations

from pydantic import BaseModel
from dify_oapi.core.model.base_response import BaseResponse


class DeleteResponse(BaseResponse):
    """Response model for delete dataset API (204 No Content)"""
    pass