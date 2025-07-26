from __future__ import annotations

from pydantic import BaseModel


class DeleteResponse(BaseModel):
    """Response model for delete dataset API (204 No Content)"""
    pass