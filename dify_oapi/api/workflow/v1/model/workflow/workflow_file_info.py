from __future__ import annotations

from pydantic import BaseModel

from .workflow_types import FileType, TransferMethod


class WorkflowFileInfo(BaseModel):
    type: FileType | None = None
    transfer_method: TransferMethod | None = None
    url: str | None = None
    upload_file_id: str | None = None

    @staticmethod
    def builder() -> WorkflowFileInfoBuilder:
        return WorkflowFileInfoBuilder()


class WorkflowFileInfoBuilder:
    def __init__(self):
        self._workflow_file_info = WorkflowFileInfo()

    def build(self) -> WorkflowFileInfo:
        return self._workflow_file_info

    def type(self, type: FileType) -> WorkflowFileInfoBuilder:
        self._workflow_file_info.type = type
        return self

    def transfer_method(self, transfer_method: TransferMethod) -> WorkflowFileInfoBuilder:
        self._workflow_file_info.transfer_method = transfer_method
        return self

    def url(self, url: str) -> WorkflowFileInfoBuilder:
        self._workflow_file_info.url = url
        return self

    def upload_file_id(self, upload_file_id: str) -> WorkflowFileInfoBuilder:
        self._workflow_file_info.upload_file_id = upload_file_id
        return self
