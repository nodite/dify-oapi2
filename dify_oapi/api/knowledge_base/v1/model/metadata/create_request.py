from __future__ import annotations

from pydantic import BaseModel

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class CreateMetadataRequestBody(BaseModel):
    type: str = ""
    name: str = ""


class CreateMetadataRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.request_body: CreateMetadataRequestBody | None = None

    @staticmethod
    def builder() -> CreateMetadataRequestBuilder:
        return CreateMetadataRequestBuilder()


class CreateMetadataRequestBuilder:
    def __init__(self):
        create_metadata_request = CreateMetadataRequest()
        create_metadata_request.http_method = HttpMethod.POST
        create_metadata_request.uri = "/v1/datasets/:dataset_id/metadata"
        self._request = create_metadata_request

    def build(self) -> CreateMetadataRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> CreateMetadataRequestBuilder:
        self._request.dataset_id = dataset_id
        self._request.paths["dataset_id"] = dataset_id
        return self

    def type(self, type: str) -> CreateMetadataRequestBuilder:
        if self._request.request_body is None:
            self._request.request_body = CreateMetadataRequestBody()
        self._request.request_body.type = type
        self._request.body = self._request.request_body.model_dump(exclude_none=True, mode="json")
        return self

    def name(self, name: str) -> CreateMetadataRequestBuilder:
        if self._request.request_body is None:
            self._request.request_body = CreateMetadataRequestBody()
        self._request.request_body.name = name
        self._request.body = self._request.request_body.model_dump(exclude_none=True, mode="json")
        return self