from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.tag.create_request import CreateTagRequest
from ..model.tag.create_response import CreateTagResponse
from ..model.tag.list_request import ListTagsRequest
from ..model.tag.list_response import ListTagsResponse
from ..model.tag.update_request import UpdateTagRequest
from ..model.tag.update_response import UpdateTagResponse
from ..model.tag.delete_request import DeleteTagRequest
from ..model.tag.delete_response import DeleteTagResponse
from ..model.tag.bind_request import BindTagsRequest
from ..model.tag.bind_response import BindTagsResponse
from ..model.tag.unbind_request import UnbindTagRequest
from ..model.tag.unbind_response import UnbindTagResponse
from ..model.tag.query_bound_request import QueryBoundTagsRequest
from ..model.tag.query_bound_response import QueryBoundTagsResponse


class Tag:
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateTagRequest, option: RequestOption | None = None) -> CreateTagResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateTagResponse, option=option)

    async def acreate(self, request: CreateTagRequest, option: RequestOption | None = None) -> CreateTagResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=CreateTagResponse, option=option)

    def list(self, request: ListTagsRequest, option: RequestOption | None = None) -> ListTagsResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListTagsResponse, option=option)

    async def alist(self, request: ListTagsRequest, option: RequestOption | None = None) -> ListTagsResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=ListTagsResponse, option=option)

    def update(self, request: UpdateTagRequest, option: RequestOption | None = None) -> UpdateTagResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateTagResponse, option=option)

    async def aupdate(self, request: UpdateTagRequest, option: RequestOption | None = None) -> UpdateTagResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UpdateTagResponse, option=option)

    def delete(self, request: DeleteTagRequest, option: RequestOption | None = None) -> DeleteTagResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteTagResponse, option=option)

    async def adelete(self, request: DeleteTagRequest, option: RequestOption | None = None) -> DeleteTagResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=DeleteTagResponse, option=option)

    def bind_tags(self, request: BindTagsRequest, option: RequestOption | None = None) -> BindTagsResponse:
        return Transport.execute(self.config, request, unmarshal_as=BindTagsResponse, option=option)

    async def abind_tags(self, request: BindTagsRequest, option: RequestOption | None = None) -> BindTagsResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=BindTagsResponse, option=option)

    def unbind_tag(self, request: UnbindTagRequest, option: RequestOption | None = None) -> UnbindTagResponse:
        return Transport.execute(self.config, request, unmarshal_as=UnbindTagResponse, option=option)

    async def aunbind_tag(self, request: UnbindTagRequest, option: RequestOption | None = None) -> UnbindTagResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UnbindTagResponse, option=option)

    def query_bound(self, request: QueryBoundTagsRequest, option: RequestOption | None = None) -> QueryBoundTagsResponse:
        return Transport.execute(self.config, request, unmarshal_as=QueryBoundTagsResponse, option=option)

    async def aquery_bound(self, request: QueryBoundTagsRequest, option: RequestOption | None = None) -> QueryBoundTagsResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=QueryBoundTagsResponse, option=option)