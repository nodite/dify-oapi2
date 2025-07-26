from __future__ import annotations

from pydantic import BaseModel


class DeleteDatasetRequest(BaseModel):
    dataset_id: str

    @staticmethod
    def builder() -> DeleteDatasetRequestBuilder:
        return DeleteDatasetRequestBuilder()


class DeleteDatasetRequestBuilder:
    def __init__(self):
        self._request = DeleteDatasetRequest(dataset_id="")

    def build(self) -> DeleteDatasetRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> DeleteDatasetRequestBuilder:
        self._request.dataset_id = dataset_id
        return self