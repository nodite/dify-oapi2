"""File resource for chat API."""

from __future__ import annotations

from dify_oapi.api.chat.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.api.chat.v1.model.upload_file_response import UploadFileResponse
from dify_oapi.core.http.transport import Transport
from dify_oapi.core.http.transport.async_transport import ATransport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class File:
    """File resource for handling file upload operations."""

    def __init__(self, config: Config) -> None:
        self.config = config

    def upload(self, request: UploadFileRequest, option: RequestOption | None = None) -> UploadFileResponse:
        """Upload a file for use in chat messages."""
        return Transport.execute(self.config, request, unmarshal_as=UploadFileResponse, option=option)

    async def aupload(self, request: UploadFileRequest, option: RequestOption | None = None) -> UploadFileResponse:
        """Upload a file for use in chat messages (async)."""
        return await ATransport.aexecute(self.config, request, unmarshal_as=UploadFileResponse, option=option)
