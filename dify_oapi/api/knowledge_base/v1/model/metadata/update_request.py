from __future__ import annotations

from pydantic import BaseModel

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class UpdateMetadataRequestBody(BaseModel):
    name: str = ""


class UpdateMetadataRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.metadata_id: str | None = None
        self.request_body: UpdateMetadataRequestBody | None = None

    @staticmethod
    def builder() -> UpdateMetadataRequestBuilder:
        return UpdateMetadataRequestBuilder()


class UpdateMetadataRequestBuilder:
    def __init__(self):
        update_metadata_request = UpdateMetadataRequest()
        update_metadata_request.http_method = HttpMethod.PATCH
        update_metadata_request.uri = "/v1/datasets/:dataset_id/metadata/:metadata_id"
        self._request = update_metadata_request

    def build(self) -> UpdateMetadataRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> UpdateMetadataRequestBuilder:
        self._request.dataset_id = dataset_id
        self._request.paths["dataset_id"] = dataset_id
        return self

    def metadata_id(self, metadata_id: str) -> UpdateMetadataRequestBuilder:
        self._request.metadata_id = metadata_id
        self._request.paths["metadata_id"] = metadata_id
        return self

    def name(self, name: str) -> UpdateMetadataRequestBuilder:
        if self._request.request_body is None:
            self._request.request_body = UpdateMetadataRequestBody()
        self._request.request_body.name = name
        self._request.body = self._request.request_body.model_dump(exclude_none=True, mode="json")
        return self