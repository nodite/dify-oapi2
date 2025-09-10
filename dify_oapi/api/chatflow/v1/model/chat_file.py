from pydantic import BaseModel

from .chatflow_types import FileType, TransferMethod


class ChatFile(BaseModel):
    """File attachment model for chat messages."""

    type: FileType | None = None
    transfer_method: TransferMethod | None = None
    url: str | None = None
    upload_file_id: str | None = None

    @staticmethod
    def builder() -> "ChatFileBuilder":
        return ChatFileBuilder()


class ChatFileBuilder:
    def __init__(self):
        self._chat_file = ChatFile()

    def build(self) -> ChatFile:
        return self._chat_file

    def type(self, type: FileType) -> "ChatFileBuilder":
        self._chat_file.type = type
        return self

    def transfer_method(self, transfer_method: TransferMethod) -> "ChatFileBuilder":
        self._chat_file.transfer_method = transfer_method
        return self

    def url(self, url: str) -> "ChatFileBuilder":
        self._chat_file.url = url
        return self

    def upload_file_id(self, upload_file_id: str) -> "ChatFileBuilder":
        self._chat_file.upload_file_id = upload_file_id
        return self
