from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .upload_file_info import UploadFileInfo


class GetUploadFileResponse(UploadFileInfo, BaseResponse):
    """Response model for get upload file API."""

    pass
