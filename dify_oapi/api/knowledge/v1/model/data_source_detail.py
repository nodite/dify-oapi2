"""Data source detail models."""

from typing import Optional

from pydantic import BaseModel


class UploadFileDetail(BaseModel):
    """Upload file detail information."""

    id: Optional[str] = None
    name: Optional[str] = None
    size: Optional[int] = None
    extension: Optional[str] = None
    mime_type: Optional[str] = None
    created_by: Optional[str] = None
    created_at: Optional[float] = None


class DataSourceDetailDict(BaseModel):
    """Data source detail dictionary."""

    upload_file: Optional[UploadFileDetail] = None
