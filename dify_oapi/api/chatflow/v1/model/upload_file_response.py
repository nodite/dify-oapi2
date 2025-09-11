from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .file_info import FileInfo


class UploadFileResponse(FileInfo, BaseResponse):
    """Upload file response model."""

    pass
