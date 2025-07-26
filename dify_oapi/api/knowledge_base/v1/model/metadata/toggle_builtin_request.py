from __future__ import annotations

from pydantic import BaseModel


class ToggleBuiltinMetadataRequest(BaseModel):
    dataset_id: str
    action: str  # "enable" or "disable"

    @staticmethod
    def builder() -> ToggleBuiltinMetadataRequestBuilder:
        return ToggleBuiltinMetadataRequestBuilder()


class ToggleBuiltinMetadataRequestBuilder:
    def __init__(self):
        self._request = ToggleBuiltinMetadataRequest(dataset_id="", action="")

    def build(self) -> ToggleBuiltinMetadataRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> ToggleBuiltinMetadataRequestBuilder:
        self._request.dataset_id = dataset_id
        return self

    def action(self, action: str) -> ToggleBuiltinMetadataRequestBuilder:
        self._request.action = action
        return self