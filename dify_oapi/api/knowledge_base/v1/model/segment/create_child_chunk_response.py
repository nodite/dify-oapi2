from dify_oapi.core.model.base_response import BaseResponse

from .child_chunk_info import ChildChunkInfo


class CreateChildChunkResponse(BaseResponse):
    data: ChildChunkInfo | None = None
