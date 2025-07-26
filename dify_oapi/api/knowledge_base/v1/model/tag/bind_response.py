from __future__ import annotations

from pydantic import BaseModel


class BindTagsResponse(BaseModel):
    result: str

    @staticmethod
    def builder() -> BindTagsResponseBuilder:
        return BindTagsResponseBuilder()


class BindTagsResponseBuilder:
    def __init__(self):
        self._response = BindTagsResponse(result="")

    def build(self) -> BindTagsResponse:
        return self._response

    def result(self, result: str) -> BindTagsResponseBuilder:
        self._response.result = result
        return self