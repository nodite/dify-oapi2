from __future__ import annotations

from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.file.preview_file_request import PreviewFileRequest
from ..model.file.preview_file_response import PreviewFileResponse
from ..model.file.upload_file_request import UploadFileRequest
from ..model.file.upload_file_response import UploadFileResponse


class File:
    def __init__(self, config: Config) -> None:
        self.config = config

    def upload_file(self, request: UploadFileRequest, request_option: RequestOption) -> UploadFileResponse:
        """Upload file for multimodal support.

        Args:
            request: The upload file request
            request_option: Request options including API key

        Returns:
            UploadFileResponse with file information
        """
        return Transport.execute(self.config, request, unmarshal_as=UploadFileResponse, option=request_option)

    async def aupload_file(self, request: UploadFileRequest, request_option: RequestOption) -> UploadFileResponse:
        """Upload file for multimodal support asynchronously.

        Args:
            request: The upload file request
            request_option: Request options including API key

        Returns:
            UploadFileResponse with file information
        """
        return await ATransport.aexecute(self.config, request, unmarshal_as=UploadFileResponse, option=request_option)

    def preview_file(self, request: PreviewFileRequest, request_option: RequestOption) -> PreviewFileResponse:
        """Preview or download uploaded file.

        Args:
            request: The preview file request
            request_option: Request options including API key

        Returns:
            PreviewFileResponse with file content
        """
        return Transport.execute(self.config, request, unmarshal_as=PreviewFileResponse, option=request_option)

    async def apreview_file(self, request: PreviewFileRequest, request_option: RequestOption) -> PreviewFileResponse:
        """Preview or download uploaded file asynchronously.

        Args:
            request: The preview file request
            request_option: Request options including API key

        Returns:
            PreviewFileResponse with file content
        """
        return await ATransport.aexecute(self.config, request, unmarshal_as=PreviewFileResponse, option=request_option)
