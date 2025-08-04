from dify_oapi.core.model.base_response import BaseResponse

from .child_chunk_info import ChildChunkInfo


class ListChildChunksResponse(BaseResponse):
    data: list[ChildChunkInfo] | None = None
    total: int | None = None
    total_pages: int | None = None
    page: int | None = None
    limit: int | None = None
