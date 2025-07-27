from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.tag.bind_request import BindRequest
from ..model.tag.bind_response import BindResponse
from ..model.tag.create_request import CreateRequest
from ..model.tag.create_response import CreateResponse
from ..model.tag.delete_request import DeleteRequest
from ..model.tag.delete_response import DeleteResponse
from ..model.tag.list_request import ListRequest
from ..model.tag.list_response import ListResponse
from ..model.tag.query_bound_request import QueryBoundRequest
from ..model.tag.query_bound_response import QueryBoundResponse
from ..model.tag.unbind_request import UnbindRequest
from ..model.tag.unbind_response import UnbindResponse
from ..model.tag.update_request import UpdateRequest
from ..model.tag.update_response import UpdateResponse


class Tag:
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateRequest, option: RequestOption | None = None) -> CreateResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateResponse, option=option)

    async def acreate(self, request: CreateRequest, option: RequestOption | None = None) -> CreateResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=CreateResponse, option=option)

    def list(self, request: ListRequest, option: RequestOption | None = None) -> ListResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListResponse, option=option)

    async def alist(self, request: ListRequest, option: RequestOption | None = None) -> ListResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=ListResponse, option=option)

    def update(self, request: UpdateRequest, option: RequestOption | None = None) -> UpdateResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateResponse, option=option)

    async def aupdate(self, request: UpdateRequest, option: RequestOption | None = None) -> UpdateResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UpdateResponse, option=option)

    def delete(self, request: DeleteRequest, option: RequestOption | None = None) -> DeleteResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteResponse, option=option)

    async def adelete(self, request: DeleteRequest, option: RequestOption | None = None) -> DeleteResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=DeleteResponse, option=option)

    def bind_tags(self, request: BindRequest, option: RequestOption | None = None) -> BindResponse:
        return Transport.execute(self.config, request, unmarshal_as=BindResponse, option=option)

    async def abind_tags(self, request: BindRequest, option: RequestOption | None = None) -> BindResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=BindResponse, option=option)

    def unbind_tag(self, request: UnbindRequest, option: RequestOption | None = None) -> UnbindResponse:
        return Transport.execute(self.config, request, unmarshal_as=UnbindResponse, option=option)

    async def aunbind_tag(self, request: UnbindRequest, option: RequestOption | None = None) -> UnbindResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UnbindResponse, option=option)

    def query_bound(self, request: QueryBoundRequest, option: RequestOption | None = None) -> QueryBoundResponse:
        return Transport.execute(self.config, request, unmarshal_as=QueryBoundResponse, option=option)

    async def aquery_bound(self, request: QueryBoundRequest, option: RequestOption | None = None) -> QueryBoundResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=QueryBoundResponse, option=option)
