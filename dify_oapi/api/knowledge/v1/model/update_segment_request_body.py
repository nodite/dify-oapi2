"""Update segment request body model."""

from __future__ import annotations

from pydantic import BaseModel

from .segment_content import SegmentContent


class UpdateSegmentRequestBody(BaseModel):
    """Request body model for update segment API."""

    segment: SegmentContent | None = None

    @staticmethod
    def builder() -> UpdateSegmentRequestBodyBuilder:
        return UpdateSegmentRequestBodyBuilder()


class UpdateSegmentRequestBodyBuilder:
    """Builder for UpdateSegmentRequestBody."""

    def __init__(self) -> None:
        self._update_segment_request_body = UpdateSegmentRequestBody()

    def build(self) -> UpdateSegmentRequestBody:
        return self._update_segment_request_body

    def segment(self, segment: SegmentContent) -> UpdateSegmentRequestBodyBuilder:
        self._update_segment_request_body.segment = segment
        return self
