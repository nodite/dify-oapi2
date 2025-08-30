from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.create_child_chunk_request import CreateChildChunkRequest
from ..model.create_child_chunk_response import CreateChildChunkResponse
from ..model.delete_child_chunk_request import DeleteChildChunkRequest
from ..model.delete_child_chunk_response import DeleteChildChunkResponse
from ..model.list_child_chunks_request import ListChildChunksRequest
from ..model.list_child_chunks_response import ListChildChunksResponse
from ..model.update_child_chunk_request import UpdateChildChunkRequest
from ..model.update_child_chunk_response import UpdateChildChunkResponse


class Chunk:
    def __init__(self, config: Config):
        self.config = config

    def list(self, request: ListChildChunksRequest, request_option: RequestOption) -> ListChildChunksResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListChildChunksResponse, option=request_option)

    async def alist(self, request: ListChildChunksRequest, request_option: RequestOption) -> ListChildChunksResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=ListChildChunksResponse, option=request_option
        )

    def create(self, request: CreateChildChunkRequest, request_option: RequestOption) -> CreateChildChunkResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateChildChunkResponse, option=request_option)

    async def acreate(
        self, request: CreateChildChunkRequest, request_option: RequestOption
    ) -> CreateChildChunkResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=CreateChildChunkResponse, option=request_option
        )

    def update(self, request: UpdateChildChunkRequest, request_option: RequestOption) -> UpdateChildChunkResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateChildChunkResponse, option=request_option)

    async def aupdate(
        self, request: UpdateChildChunkRequest, request_option: RequestOption
    ) -> UpdateChildChunkResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=UpdateChildChunkResponse, option=request_option
        )

    def delete(self, request: DeleteChildChunkRequest, request_option: RequestOption) -> DeleteChildChunkResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteChildChunkResponse, option=request_option)

    async def adelete(
        self, request: DeleteChildChunkRequest, request_option: RequestOption
    ) -> DeleteChildChunkResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=DeleteChildChunkResponse, option=request_option
        )
