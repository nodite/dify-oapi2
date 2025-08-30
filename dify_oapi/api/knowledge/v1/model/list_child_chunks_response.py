"""List child chunks response model."""

from dify_oapi.core.model.base_response import BaseResponse

from .child_chunk_info import ChildChunkInfo


class ListChildChunksResponse(BaseResponse):
    """Response model for list child chunks API."""

    data: list[ChildChunkInfo] | None = None
    total: int | None = None
    total_pages: int | None = None
    page: int | None = None
    limit: int | None = None
