"""Create child chunk response model."""

from dify_oapi.core.model.base_response import BaseResponse

from .child_chunk_info import ChildChunkInfo


class CreateChildChunkResponse(BaseResponse):
    """Response model for create child chunk API."""

    data: list[ChildChunkInfo] | None = None
