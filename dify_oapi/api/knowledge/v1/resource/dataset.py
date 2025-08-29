from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

# New dataset models
from ..model.dataset.create_request import CreateRequest
from ..model.dataset.create_response import CreateResponse
from ..model.dataset.delete_request import DeleteRequest
from ..model.dataset.delete_response import DeleteResponse
from ..model.dataset.get_request import GetRequest
from ..model.dataset.get_response import GetResponse
from ..model.dataset.list_request import ListRequest
from ..model.dataset.list_response import ListResponse
from ..model.dataset.retrieve_request import RetrieveRequest
from ..model.dataset.retrieve_response import RetrieveResponse
from ..model.dataset.update_request import UpdateRequest
from ..model.dataset.update_response import UpdateResponse


class Dataset:
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

    def get(self, request: GetRequest, option: RequestOption | None = None) -> GetResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetResponse, option=option)

    async def aget(self, request: GetRequest, option: RequestOption | None = None) -> GetResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetResponse, option=option)

    def update(self, request: UpdateRequest, option: RequestOption | None = None) -> UpdateResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateResponse, option=option)

    async def aupdate(self, request: UpdateRequest, option: RequestOption | None = None) -> UpdateResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UpdateResponse, option=option)

    def delete(self, request: DeleteRequest, option: RequestOption | None = None) -> DeleteResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteResponse, option=option)

    async def adelete(self, request: DeleteRequest, option: RequestOption | None = None) -> DeleteResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=DeleteResponse, option=option)

    def retrieve(self, request: RetrieveRequest, option: RequestOption | None = None) -> RetrieveResponse:
        return Transport.execute(self.config, request, unmarshal_as=RetrieveResponse, option=option)

    async def aretrieve(self, request: RetrieveRequest, option: RequestOption | None = None) -> RetrieveResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=RetrieveResponse, option=option)
