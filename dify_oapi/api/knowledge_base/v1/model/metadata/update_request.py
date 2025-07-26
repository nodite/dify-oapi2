from __future__ import annotations

from pydantic import BaseModel


class UpdateMetadataRequest(BaseModel):
    dataset_id: str
    metadata_id: str
    name: str

    @staticmethod
    def builder() -> UpdateMetadataRequestBuilder:
        return UpdateMetadataRequestBuilder()


class UpdateMetadataRequestBuilder:
    def __init__(self):
        self._request = UpdateMetadataRequest(dataset_id="", metadata_id="", name="")

    def build(self) -> UpdateMetadataRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> UpdateMetadataRequestBuilder:
        self._request.dataset_id = dataset_id
        return self

    def metadata_id(self, metadata_id: str) -> UpdateMetadataRequestBuilder:
        self._request.metadata_id = metadata_id
        return self

    def name(self, name: str) -> UpdateMetadataRequestBuilder:
        self._request.name = name
        return self