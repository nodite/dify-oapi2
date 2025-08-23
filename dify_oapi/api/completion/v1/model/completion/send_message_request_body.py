from __future__ import annotations

from pydantic import BaseModel

from .completion_inputs import CompletionInputs
from .completion_types import FileType, ResponseMode, TransferMethod


class FileInfo(BaseModel):
    type: FileType | None = None
    transfer_method: TransferMethod | None = None
    url: str | None = None
    upload_file_id: str | None = None

    @staticmethod
    def builder() -> FileInfoBuilder:
        return FileInfoBuilder()


class FileInfoBuilder:
    def __init__(self):
        self._file_info = FileInfo()

    def build(self) -> FileInfo:
        return self._file_info

    def type(self, type_: FileType) -> FileInfoBuilder:
        self._file_info.type = type_
        return self

    def transfer_method(self, transfer_method: TransferMethod) -> FileInfoBuilder:
        self._file_info.transfer_method = transfer_method
        return self

    def url(self, url: str) -> FileInfoBuilder:
        self._file_info.url = url
        return self

    def upload_file_id(self, upload_file_id: str) -> FileInfoBuilder:
        self._file_info.upload_file_id = upload_file_id
        return self


class SendMessageRequestBody(BaseModel):
    inputs: CompletionInputs | None = None
    response_mode: ResponseMode | None = None
    user: str | None = None
    files: list[FileInfo] | None = None

    @staticmethod
    def builder() -> SendMessageRequestBodyBuilder:
        return SendMessageRequestBodyBuilder()


class SendMessageRequestBodyBuilder:
    def __init__(self):
        self._send_message_request_body = SendMessageRequestBody()

    def build(self) -> SendMessageRequestBody:
        return self._send_message_request_body

    def inputs(self, inputs: CompletionInputs) -> SendMessageRequestBodyBuilder:
        self._send_message_request_body.inputs = inputs
        return self

    def response_mode(self, response_mode: ResponseMode) -> SendMessageRequestBodyBuilder:
        self._send_message_request_body.response_mode = response_mode
        return self

    def user(self, user: str) -> SendMessageRequestBodyBuilder:
        self._send_message_request_body.user = user
        return self

    def files(self, files: list[FileInfo]) -> SendMessageRequestBodyBuilder:
        self._send_message_request_body.files = files
        return self
