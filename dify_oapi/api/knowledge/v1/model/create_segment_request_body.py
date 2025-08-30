"""Create segment request body model."""

from __future__ import annotations

from pydantic import BaseModel

from .segment_content import SegmentContent


class CreateSegmentRequestBody(BaseModel):
    """Request body model for create segment API."""

    segments: list[SegmentContent] | None = None

    @staticmethod
    def builder() -> CreateSegmentRequestBodyBuilder:
        return CreateSegmentRequestBodyBuilder()


class CreateSegmentRequestBodyBuilder:
    """Builder for CreateSegmentRequestBody."""

    def __init__(self) -> None:
        self._create_segment_request_body = CreateSegmentRequestBody()

    def build(self) -> CreateSegmentRequestBody:
        return self._create_segment_request_body

    def segments(self, segments: list[SegmentContent]) -> CreateSegmentRequestBodyBuilder:
        self._create_segment_request_body.segments = segments
        return self
