"""Dataset metadata model."""

from pydantic import BaseModel


class DatasetMetadata(BaseModel):
    """Dataset metadata information."""

    # Based on API response, this is typically an empty array
    # Can be extended when actual metadata structure is known
    key: str | None = None
    value: str | None = None
