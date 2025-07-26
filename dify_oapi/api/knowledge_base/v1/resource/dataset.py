from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

# New dataset models
from ..model.dataset.create_request import CreateRequest
from ..model.dataset.create_response import CreateDatasetResponse
from ..model.dataset.list_request import ListRequest
from ..model.dataset.list_response import ListDatasetsResponse
from ..model.dataset.get_request import GetRequest
from ..model.dataset.get_response import GetDatasetResponse
from ..model.dataset.update_request import UpdateRequest
from ..model.dataset.update_response import UpdateDatasetResponse
from ..model.dataset.delete_request import DeleteRequest
from ..model.dataset.delete_response import DeleteDatasetResponse
from ..model.dataset.retrieve_request import RetrieveRequest
from ..model.dataset.retrieve_response import RetrieveDatasetResponse




class Dataset:
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateRequest, option: RequestOption | None = None) -> CreateDatasetResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateDatasetResponse, option=option)

    async def acreate(
        self, request: CreateRequest, option: RequestOption | None = None
    ) -> CreateDatasetResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=CreateDatasetResponse, option=option)

    def list(self, request: ListRequest, option: RequestOption | None = None) -> ListDatasetsResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListDatasetsResponse, option=option)

    async def alist(self, request: ListRequest, option: RequestOption | None = None) -> ListDatasetsResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=ListDatasetsResponse, option=option)

    def get(self, request: GetRequest, option: RequestOption | None = None) -> GetDatasetResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetDatasetResponse, option=option)

    async def aget(self, request: GetRequest, option: RequestOption | None = None) -> GetDatasetResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetDatasetResponse, option=option)

    def update(self, request: UpdateRequest, option: RequestOption | None = None) -> UpdateDatasetResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateDatasetResponse, option=option)

    async def aupdate(self, request: UpdateRequest, option: RequestOption | None = None) -> UpdateDatasetResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UpdateDatasetResponse, option=option)

    def delete(self, request: DeleteRequest, option: RequestOption | None = None) -> DeleteDatasetResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteDatasetResponse, option=option)

    async def adelete(
        self, request: DeleteRequest, option: RequestOption | None = None
    ) -> DeleteDatasetResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=DeleteDatasetResponse, option=option)

    def retrieve(self, request: RetrieveRequest, option: RequestOption | None = None) -> RetrieveDatasetResponse:
        return Transport.execute(self.config, request, unmarshal_as=RetrieveDatasetResponse, option=option)

    async def aretrieve(self, request: RetrieveRequest, option: RequestOption | None = None) -> RetrieveDatasetResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=RetrieveDatasetResponse, option=option)

