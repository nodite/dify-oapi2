from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .stop_response_request_body import StopResponseRequestBody


class StopResponseRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: StopResponseRequestBody | None = None
        self.task_id: str | None = None

    @staticmethod
    def builder() -> StopResponseRequestBuilder:
        return StopResponseRequestBuilder()


class StopResponseRequestBuilder:
    def __init__(self):
        stop_response_request = StopResponseRequest()
        stop_response_request.http_method = HttpMethod.POST
        stop_response_request.uri = "/v1/completion-messages/:task_id/stop"
        self._stop_response_request = stop_response_request

    def build(self) -> StopResponseRequest:
        return self._stop_response_request

    def request_body(self, request_body: StopResponseRequestBody) -> StopResponseRequestBuilder:
        self._stop_response_request.request_body = request_body
        self._stop_response_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self

    def task_id(self, task_id: str) -> StopResponseRequestBuilder:
        self._stop_response_request.task_id = task_id
        self._stop_response_request.paths["task_id"] = task_id
        return self
