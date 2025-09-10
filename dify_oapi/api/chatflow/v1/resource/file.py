from __future__ import annotations

from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.upload_file_request import UploadFileRequest
from ..model.upload_file_response import UploadFileResponse


class File:
    """File resource for chatflow API operations."""

    def __init__(self, config: Config):
        self.config = config

    def upload(self, request: UploadFileRequest, request_option: RequestOption) -> UploadFileResponse:
        """Upload file for multimodal support.

        Args:
            request: Upload file request
            request_option: Request options including API key

        Returns:
            Upload file response with file information
        """
        return Transport.execute(self.config, request, unmarshal_as=UploadFileResponse, option=request_option)

    async def aupload(self, request: UploadFileRequest, request_option: RequestOption) -> UploadFileResponse:
        """Upload file for multimodal support (async).

        Args:
            request: Upload file request
            request_option: Request options including API key

        Returns:
            Upload file response with file information
        """
        return await ATransport.aexecute(self.config, request, unmarshal_as=UploadFileResponse, option=request_option)
