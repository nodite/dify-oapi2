from __future__ import annotations

from pydantic import BaseModel

from .segment_info import SegmentInfo


class CreateRequestBody(BaseModel):
    segments: list[SegmentInfo] | None = None

    @staticmethod
    def builder() -> CreateRequestBodyBuilder:
        return CreateRequestBodyBuilder()


class CreateRequestBodyBuilder:
    def __init__(self):
        self._create_request_body = CreateRequestBody()

    def build(self) -> CreateRequestBody:
        return self._create_request_body

    def segments(self, segments: list[SegmentInfo]) -> CreateRequestBodyBuilder:
        self._create_request_body.segments = segments
        return self
