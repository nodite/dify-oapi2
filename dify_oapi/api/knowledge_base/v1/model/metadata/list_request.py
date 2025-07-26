from __future__ import annotations

from pydantic import BaseModel


class ListMetadataRequest(BaseModel):
    dataset_id: str

    @staticmethod
    def builder() -> ListMetadataRequestBuilder:
        return ListMetadataRequestBuilder()


class ListMetadataRequestBuilder:
    def __init__(self):
        self._request = ListMetadataRequest(dataset_id="")

    def build(self) -> ListMetadataRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> ListMetadataRequestBuilder:
        self._request.dataset_id = dataset_id
        return self