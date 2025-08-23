from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class FileInfo(BaseModel):
    type: str | None = None
    transfer_method: str | None = None
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

    def type(self, type_: str) -> FileInfoBuilder:
        self._file_info.type = type_
        return self

    def transfer_method(self, transfer_method: str) -> FileInfoBuilder:
        self._file_info.transfer_method = transfer_method
        return self

    def url(self, url: str) -> FileInfoBuilder:
        self._file_info.url = url
        return self

    def upload_file_id(self, upload_file_id: str) -> FileInfoBuilder:
        self._file_info.upload_file_id = upload_file_id
        return self


class SendMessageRequestBody(BaseModel):
    inputs: dict[str, Any] | None = None
    query: str | None = None
    response_mode: str | None = None
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

    def inputs(self, inputs: dict[str, Any]) -> SendMessageRequestBodyBuilder:
        self._send_message_request_body.inputs = inputs
        return self

    def query(self, query: str) -> SendMessageRequestBodyBuilder:
        self._send_message_request_body.query = query
        return self

    def response_mode(self, response_mode: str) -> SendMessageRequestBodyBuilder:
        self._send_message_request_body.response_mode = response_mode
        return self

    def user(self, user: str) -> SendMessageRequestBodyBuilder:
        self._send_message_request_body.user = user
        return self

    def files(self, files: list[FileInfo]) -> SendMessageRequestBodyBuilder:
        self._send_message_request_body.files = files
        return self
