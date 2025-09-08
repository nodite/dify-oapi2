"""Upload file response model."""

from dify_oapi.api.chat.v1.model.file_info import FileInfo
from dify_oapi.core.model.base_response import BaseResponse


class UploadFileResponse(FileInfo, BaseResponse):
    """Response model for upload file API."""

    pass
