from __future__ import annotations

from pydantic import BaseModel


class DeleteResponse(BaseModel):
    """Response model for delete document API (204 No Content)"""

    pass
