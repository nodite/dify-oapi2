from __future__ import annotations

from pydantic import BaseModel


class CreateMetadataRequest(BaseModel):
    dataset_id: str
    type: str
    name: str

    @staticmethod
    def builder() -> CreateMetadataRequestBuilder:
        return CreateMetadataRequestBuilder()


class CreateMetadataRequestBuilder:
    def __init__(self):
        self._request = CreateMetadataRequest(dataset_id="", type="", name="")

    def build(self) -> CreateMetadataRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> CreateMetadataRequestBuilder:
        self._request.dataset_id = dataset_id
        return self

    def type(self, type: str) -> CreateMetadataRequestBuilder:
        self._request.type = type
        return self

    def name(self, name: str) -> CreateMetadataRequestBuilder:
        self._request.name = name
        return self