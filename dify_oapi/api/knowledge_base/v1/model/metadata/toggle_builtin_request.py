from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class ToggleBuiltinRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.action: str | None = None  # "enable" or "disable"

    @staticmethod
    def builder() -> ToggleBuiltinRequestBuilder:
        return ToggleBuiltinRequestBuilder()


class ToggleBuiltinRequestBuilder:
    def __init__(self):
        toggle_builtin_request = ToggleBuiltinRequest()
        toggle_builtin_request.http_method = HttpMethod.POST
        toggle_builtin_request.uri = "/v1/datasets/:dataset_id/metadata/built-in/:action"
        self._toggle_builtin_request = toggle_builtin_request

    def build(self) -> ToggleBuiltinRequest:
        return self._toggle_builtin_request

    def dataset_id(self, dataset_id: str) -> ToggleBuiltinRequestBuilder:
        self._toggle_builtin_request.dataset_id = dataset_id
        self._toggle_builtin_request.paths["dataset_id"] = dataset_id
        return self

    def action(self, action: str) -> ToggleBuiltinRequestBuilder:
        self._toggle_builtin_request.action = action
        self._toggle_builtin_request.paths["action"] = action
        return self
