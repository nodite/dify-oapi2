from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

# Child chunk operations
from ..model.segment.create_child_chunk_request import CreateChildChunkRequest
from ..model.segment.create_child_chunk_response import CreateChildChunkResponse

# Core segment operations
from ..model.segment.create_request import CreateRequest
from ..model.segment.create_response import CreateResponse
from ..model.segment.delete_child_chunk_request import DeleteChildChunkRequest
from ..model.segment.delete_child_chunk_response import DeleteChildChunkResponse
from ..model.segment.delete_request import DeleteRequest
from ..model.segment.delete_response import DeleteResponse
from ..model.segment.get_request import GetRequest
from ..model.segment.get_response import GetResponse
from ..model.segment.list_child_chunks_request import ListChildChunksRequest
from ..model.segment.list_child_chunks_response import ListChildChunksResponse
from ..model.segment.list_request import ListRequest
from ..model.segment.list_response import ListResponse
from ..model.segment.update_child_chunk_request import UpdateChildChunkRequest
from ..model.segment.update_child_chunk_response import UpdateChildChunkResponse
from ..model.segment.update_request import UpdateRequest
from ..model.segment.update_response import UpdateResponse


class Segment:
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    # Core segment operations
    def create(self, request: CreateRequest, request_option: RequestOption) -> CreateResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateResponse, option=request_option)

    async def acreate(self, request: CreateRequest, request_option: RequestOption) -> CreateResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=CreateResponse, option=request_option)

    def list(self, request: ListRequest, request_option: RequestOption) -> ListResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListResponse, option=request_option)

    async def alist(self, request: ListRequest, request_option: RequestOption) -> ListResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=ListResponse, option=request_option)

    def get(self, request: GetRequest, request_option: RequestOption) -> GetResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetResponse, option=request_option)

    async def aget(self, request: GetRequest, request_option: RequestOption) -> GetResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetResponse, option=request_option)

    def update(self, request: UpdateRequest, request_option: RequestOption) -> UpdateResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateResponse, option=request_option)

    async def aupdate(self, request: UpdateRequest, request_option: RequestOption) -> UpdateResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UpdateResponse, option=request_option)

    def delete(self, request: DeleteRequest, request_option: RequestOption) -> DeleteResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteResponse, option=request_option)

    async def adelete(self, request: DeleteRequest, request_option: RequestOption) -> DeleteResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=DeleteResponse, option=request_option)

    # Child chunk operations
    def create_child_chunk(
        self, request: CreateChildChunkRequest, request_option: RequestOption
    ) -> CreateChildChunkResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateChildChunkResponse, option=request_option)

    async def acreate_child_chunk(
        self, request: CreateChildChunkRequest, request_option: RequestOption
    ) -> CreateChildChunkResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=CreateChildChunkResponse, option=request_option
        )

    def list_child_chunks(
        self, request: ListChildChunksRequest, request_option: RequestOption
    ) -> ListChildChunksResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListChildChunksResponse, option=request_option)

    async def alist_child_chunks(
        self, request: ListChildChunksRequest, request_option: RequestOption
    ) -> ListChildChunksResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=ListChildChunksResponse, option=request_option
        )

    def update_child_chunk(
        self, request: UpdateChildChunkRequest, request_option: RequestOption
    ) -> UpdateChildChunkResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateChildChunkResponse, option=request_option)

    async def aupdate_child_chunk(
        self, request: UpdateChildChunkRequest, request_option: RequestOption
    ) -> UpdateChildChunkResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=UpdateChildChunkResponse, option=request_option
        )

    def delete_child_chunk(
        self, request: DeleteChildChunkRequest, request_option: RequestOption
    ) -> DeleteChildChunkResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteChildChunkResponse, option=request_option)

    async def adelete_child_chunk(
        self, request: DeleteChildChunkRequest, request_option: RequestOption
    ) -> DeleteChildChunkResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=DeleteChildChunkResponse, option=request_option
        )
