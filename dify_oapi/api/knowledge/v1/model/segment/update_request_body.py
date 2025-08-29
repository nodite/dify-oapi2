from __future__ import annotations

from pydantic import BaseModel

from .segment_data import SegmentData


class UpdateRequestBody(BaseModel):
    segment: SegmentData | None = None

    @staticmethod
    def builder() -> UpdateRequestBodyBuilder:
        return UpdateRequestBodyBuilder()


class UpdateRequestBodyBuilder:
    def __init__(self):
        self._update_request_body = UpdateRequestBody()

    def build(self) -> UpdateRequestBody:
        return self._update_request_body

    def segment(self, segment: SegmentData) -> UpdateRequestBodyBuilder:
        self._update_request_body.segment = segment
        return self
