from __future__ import annotations

from pydantic import BaseModel


class GetDatasetRequest(BaseModel):
    dataset_id: str

    @staticmethod
    def builder() -> GetDatasetRequestBuilder:
        return GetDatasetRequestBuilder()


class GetDatasetRequestBuilder:
    def __init__(self):
        self._request = GetDatasetRequest(dataset_id="")

    def build(self) -> GetDatasetRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> GetDatasetRequestBuilder:
        self._request.dataset_id = dataset_id
        return self