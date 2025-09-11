from __future__ import annotations

from pydantic import BaseModel, HttpUrl

from .chat_types import FileType, TransferMethod


class ChatFile(BaseModel):
    """Chat file model for file upload support."""

    type: FileType | None = None
    transfer_method: TransferMethod | None = None
    url: HttpUrl | None = None
    upload_file_id: str | None = None

    @classmethod
    def builder(cls) -> ChatFileBuilder:
        return ChatFileBuilder()


class ChatFileBuilder:
    """Builder for ChatFile."""

    def __init__(self) -> None:
        self._chat_file = ChatFile()

    def type(self, type_: FileType) -> ChatFileBuilder:
        """Set file type."""
        self._chat_file.type = type_
        return self

    def transfer_method(self, transfer_method: TransferMethod) -> ChatFileBuilder:
        """Set transfer method."""
        self._chat_file.transfer_method = transfer_method
        return self

    def url(self, url: str) -> ChatFileBuilder:
        """Set remote URL."""
        self._chat_file.url = HttpUrl(url=url)
        return self

    def upload_file_id(self, upload_file_id: str) -> ChatFileBuilder:
        """Set upload file ID."""
        self._chat_file.upload_file_id = upload_file_id
        return self

    def build(self) -> ChatFile:
        """Build the ChatFile instance."""
        if self._chat_file.transfer_method == "remote_url" and self._chat_file.url is None:
            raise ValueError("URL is required when transfer_method is 'remote_url'")
        if self._chat_file.transfer_method == "local_file" and self._chat_file.upload_file_id is None:
            raise ValueError("upload_file_id is required when transfer_method is 'local_file'")
        return self._chat_file
