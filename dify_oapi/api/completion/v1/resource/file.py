from __future__ import annotations

from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.file.upload_file_request import UploadFileRequest
from ..model.file.upload_file_response import UploadFileResponse


class File:
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def upload_file(self, request: UploadFileRequest, request_option: RequestOption) -> UploadFileResponse:
        return Transport.execute(self.config, request, unmarshal_as=UploadFileResponse, option=request_option)

    async def aupload_file(self, request: UploadFileRequest, request_option: RequestOption) -> UploadFileResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UploadFileResponse, option=request_option)
