from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class ToggleBuiltinMetadataRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.action: str | None = None  # "enable" or "disable"

    @staticmethod
    def builder() -> ToggleBuiltinMetadataRequestBuilder:
        return ToggleBuiltinMetadataRequestBuilder()


class ToggleBuiltinMetadataRequestBuilder:
    def __init__(self):
        toggle_builtin_metadata_request = ToggleBuiltinMetadataRequest()
        toggle_builtin_metadata_request.http_method = HttpMethod.POST
        toggle_builtin_metadata_request.uri = "/v1/datasets/:dataset_id/metadata/built-in/:action"
        self._request = toggle_builtin_metadata_request

    def build(self) -> ToggleBuiltinMetadataRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> ToggleBuiltinMetadataRequestBuilder:
        self._request.dataset_id = dataset_id
        self._request.paths["dataset_id"] = dataset_id
        return self

    def action(self, action: str) -> ToggleBuiltinMetadataRequestBuilder:
        self._request.action = action
        self._request.paths["action"] = action
        return self