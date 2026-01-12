"""Data source detail models."""

from pydantic import BaseModel


class UploadFileDetail(BaseModel):
    """Upload file detail information."""

    id: str | None = None
    name: str | None = None
    size: int | None = None
    extension: str | None = None
    mime_type: str | None = None
    created_by: str | None = None
    created_at: float | None = None


class DataSourceDetailDict(BaseModel):
    """Data source detail dictionary."""

    upload_file: UploadFileDetail | None = None
