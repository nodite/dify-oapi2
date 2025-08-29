from __future__ import annotations

from pydantic import BaseModel


class DataSourceInfo(BaseModel):
    """Data source information model for document uploads."""

    upload_file_id: str | None = None
    upload_file: dict | None = None

    @staticmethod
    def builder() -> DataSourceInfoBuilder:
        return DataSourceInfoBuilder()


class DataSourceInfoBuilder:
    def __init__(self):
        self._data_source_info = DataSourceInfo()

    def build(self) -> DataSourceInfo:
        return self._data_source_info

    def upload_file_id(self, upload_file_id: str) -> DataSourceInfoBuilder:
        self._data_source_info.upload_file_id = upload_file_id
        return self

    def upload_file(self, upload_file: dict) -> DataSourceInfoBuilder:
        self._data_source_info.upload_file = upload_file
        return self
