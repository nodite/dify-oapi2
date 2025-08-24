from __future__ import annotations

from pydantic import BaseModel

from ..workflow.workflow_types import FileType, TransferMethod


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

    def type(self, type: FileType) -> FileInfoBuilder:
        self._file_info.type = type
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
