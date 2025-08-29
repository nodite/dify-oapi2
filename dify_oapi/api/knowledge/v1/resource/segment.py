from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.create_child_chunk_request import CreateChildChunkRequest
from ..model.create_child_chunk_response import CreateChildChunkResponse
from ..model.create_segment_request import CreateSegmentRequest
from ..model.create_segment_response import CreateSegmentResponse
from ..model.delete_child_chunk_request import DeleteChildChunkRequest
from ..model.delete_child_chunk_response import DeleteChildChunkResponse
from ..model.delete_segment_request import DeleteSegmentRequest
from ..model.delete_segment_response import DeleteSegmentResponse
from ..model.get_segment_request import GetSegmentRequest
from ..model.get_segment_response import GetSegmentResponse
from ..model.list_child_chunks_request import ListChildChunksRequest
from ..model.list_child_chunks_response import ListChildChunksResponse
from ..model.list_segments_request import ListSegmentsRequest
from ..model.list_segments_response import ListSegmentsResponse
from ..model.update_child_chunk_request import UpdateChildChunkRequest
from ..model.update_child_chunk_response import UpdateChildChunkResponse
from ..model.update_segment_request import UpdateSegmentRequest
from ..model.update_segment_response import UpdateSegmentResponse


class Segment:
    def __init__(self, config: Config):
        self.config = config

    def list(self, request: ListSegmentsRequest, request_option: RequestOption) -> ListSegmentsResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListSegmentsResponse, option=request_option)

    async def alist(self, request: ListSegmentsRequest, request_option: RequestOption) -> ListSegmentsResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=ListSegmentsResponse, option=request_option)

    def create(self, request: CreateSegmentRequest, request_option: RequestOption) -> CreateSegmentResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateSegmentResponse, option=request_option)

    async def acreate(self, request: CreateSegmentRequest, request_option: RequestOption) -> CreateSegmentResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=CreateSegmentResponse, option=request_option
        )

    def get(self, request: GetSegmentRequest, request_option: RequestOption) -> GetSegmentResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetSegmentResponse, option=request_option)

    async def aget(self, request: GetSegmentRequest, request_option: RequestOption) -> GetSegmentResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetSegmentResponse, option=request_option)

    def update(self, request: UpdateSegmentRequest, request_option: RequestOption) -> UpdateSegmentResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateSegmentResponse, option=request_option)

    async def aupdate(self, request: UpdateSegmentRequest, request_option: RequestOption) -> UpdateSegmentResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=UpdateSegmentResponse, option=request_option
        )

    def delete(self, request: DeleteSegmentRequest, request_option: RequestOption) -> DeleteSegmentResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteSegmentResponse, option=request_option)

    async def adelete(self, request: DeleteSegmentRequest, request_option: RequestOption) -> DeleteSegmentResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=DeleteSegmentResponse, option=request_option
        )

    def list_chunks(self, request: ListChildChunksRequest, request_option: RequestOption) -> ListChildChunksResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListChildChunksResponse, option=request_option)

    async def alist_chunks(
        self, request: ListChildChunksRequest, request_option: RequestOption
    ) -> ListChildChunksResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=ListChildChunksResponse, option=request_option
        )

    def create_chunk(self, request: CreateChildChunkRequest, request_option: RequestOption) -> CreateChildChunkResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateChildChunkResponse, option=request_option)

    async def acreate_chunk(
        self, request: CreateChildChunkRequest, request_option: RequestOption
    ) -> CreateChildChunkResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=CreateChildChunkResponse, option=request_option
        )

    def update_chunk(self, request: UpdateChildChunkRequest, request_option: RequestOption) -> UpdateChildChunkResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateChildChunkResponse, option=request_option)

    async def aupdate_chunk(
        self, request: UpdateChildChunkRequest, request_option: RequestOption
    ) -> UpdateChildChunkResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=UpdateChildChunkResponse, option=request_option
        )

    def delete_chunk(self, request: DeleteChildChunkRequest, request_option: RequestOption) -> DeleteChildChunkResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteChildChunkResponse, option=request_option)

    async def adelete_chunk(
        self, request: DeleteChildChunkRequest, request_option: RequestOption
    ) -> DeleteChildChunkResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=DeleteChildChunkResponse, option=request_option
        )
