"""Update status response model for document API."""

from pydantic import BaseModel


class UpdateStatusResponse(BaseModel):
    """Response model for updating document status."""

    result: str | None = None
