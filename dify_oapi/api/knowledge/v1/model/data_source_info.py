"""Data source info model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel


class DataSourceInfo(BaseModel):
    """Data source info model with builder pattern."""

    upload_file_id: Optional[str] = None
    original_document_id: Optional[str] = None

    @staticmethod
    def builder() -> "DataSourceInfoBuilder":
        return DataSourceInfoBuilder()


class DataSourceInfoBuilder:
    """Builder for DataSourceInfo."""

    def __init__(self):
        self._data_source_info = DataSourceInfo()

    def build(self) -> DataSourceInfo:
        return self._data_source_info

    def upload_file_id(self, upload_file_id: str) -> "DataSourceInfoBuilder":
        self._data_source_info.upload_file_id = upload_file_id
        return self

    def original_document_id(self, original_document_id: str) -> "DataSourceInfoBuilder":
        self._data_source_info.original_document_id = original_document_id
        return self
