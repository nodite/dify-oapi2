from __future__ import annotations

from pydantic import BaseModel


class DeleteMetadataRequest(BaseModel):
    dataset_id: str
    metadata_id: str

    @staticmethod
    def builder() -> DeleteMetadataRequestBuilder:
        return DeleteMetadataRequestBuilder()


class DeleteMetadataRequestBuilder:
    def __init__(self):
        self._request = DeleteMetadataRequest(dataset_id="", metadata_id="")

    def build(self) -> DeleteMetadataRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> DeleteMetadataRequestBuilder:
        self._request.dataset_id = dataset_id
        return self

    def metadata_id(self, metadata_id: str) -> DeleteMetadataRequestBuilder:
        self._request.metadata_id = metadata_id
        return self