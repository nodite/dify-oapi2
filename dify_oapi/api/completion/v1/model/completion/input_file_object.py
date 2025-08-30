from __future__ import annotations

from pydantic import BaseModel, field_validator

from .completion_types import FileType, TransferMethod


class InputFileObject(BaseModel):
    """File input object for multimodal understanding."""

    type: FileType
    transfer_method: TransferMethod
    url: str | None = None
    upload_file_id: str | None = None

    @field_validator("url", "upload_file_id")
    @classmethod
    def validate_transfer_method_fields(cls, v, info):
        """Validate that the correct field is provided based on transfer_method."""
        if info.data.get("transfer_method") == "remote_url":
            if info.field_name == "url" and v is None:
                raise ValueError("url is required when transfer_method is remote_url")
            if info.field_name == "upload_file_id" and v is not None:
                raise ValueError("upload_file_id must not be provided when transfer_method is remote_url")
        elif info.data.get("transfer_method") == "local_file":
            if info.field_name == "upload_file_id" and v is None:
                raise ValueError("upload_file_id is required when transfer_method is local_file")
            if info.field_name == "url" and v is not None:
                raise ValueError("url must not be provided when transfer_method is local_file")
        return v

    @staticmethod
    def builder() -> InputFileObjectBuilder:
        return InputFileObjectBuilder()


class InputFileObjectBuilder:
    def __init__(self):
        self._file_object = InputFileObject(type="image", transfer_method="remote_url")

    def build(self) -> InputFileObject:
        return self._file_object

    def type(self, type_: FileType) -> InputFileObjectBuilder:
        self._file_object.type = type_
        return self

    def transfer_method(self, transfer_method: TransferMethod) -> InputFileObjectBuilder:
        self._file_object.transfer_method = transfer_method
        return self

    def url(self, url: str) -> InputFileObjectBuilder:
        self._file_object.url = url
        return self

    def upload_file_id(self, upload_file_id: str) -> InputFileObjectBuilder:
        self._file_object.upload_file_id = upload_file_id
        return self
