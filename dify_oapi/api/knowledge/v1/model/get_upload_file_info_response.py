"""Get upload file info response model."""

from dify_oapi.core.model.base_response import BaseResponse

from .file_info import FileInfo


class GetUploadFileInfoResponse(FileInfo, BaseResponse):
    """Response model for get upload file info API."""

    pass
