from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .file_upload_info import FileUploadInfo


class UploadFileResponse(FileUploadInfo, BaseResponse):
    pass
