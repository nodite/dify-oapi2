from __future__ import annotations

from pydantic import BaseModel


class StopResponseRequestBody(BaseModel):
    user: str | None = None

    @staticmethod
    def builder() -> StopResponseRequestBodyBuilder:
        return StopResponseRequestBodyBuilder()


class StopResponseRequestBodyBuilder:
    def __init__(self):
        self._stop_response_request_body = StopResponseRequestBody()

    def build(self) -> StopResponseRequestBody:
        return self._stop_response_request_body

    def user(self, user: str) -> StopResponseRequestBodyBuilder:
        self._stop_response_request_body.user = user
        return self
