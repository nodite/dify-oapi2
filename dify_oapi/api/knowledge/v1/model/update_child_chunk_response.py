"""Update child chunk response model."""

from dify_oapi.core.model.base_response import BaseResponse

from .child_chunk_info import ChildChunkInfo


class UpdateChildChunkResponse(BaseResponse):
    """Response model for update child chunk API."""

    data: ChildChunkInfo | None = None
