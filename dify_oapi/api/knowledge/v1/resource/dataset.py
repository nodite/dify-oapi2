from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.create_dataset_request import CreateDatasetRequest
from ..model.create_dataset_response import CreateDatasetResponse
from ..model.delete_dataset_request import DeleteDatasetRequest
from ..model.delete_dataset_response import DeleteDatasetResponse
from ..model.get_dataset_request import GetDatasetRequest
from ..model.get_dataset_response import GetDatasetResponse
from ..model.list_datasets_request import ListDatasetsRequest
from ..model.list_datasets_response import ListDatasetsResponse
from ..model.retrieve_from_dataset_request import RetrieveFromDatasetRequest
from ..model.retrieve_from_dataset_response import RetrieveFromDatasetResponse
from ..model.update_dataset_request import UpdateDatasetRequest
from ..model.update_dataset_response import UpdateDatasetResponse


class Dataset:
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateDatasetRequest, request_option: RequestOption) -> CreateDatasetResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateDatasetResponse, option=request_option)

    async def acreate(self, request: CreateDatasetRequest, request_option: RequestOption) -> CreateDatasetResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=CreateDatasetResponse, option=request_option
        )

    def list(self, request: ListDatasetsRequest, request_option: RequestOption) -> ListDatasetsResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListDatasetsResponse, option=request_option)

    async def alist(self, request: ListDatasetsRequest, request_option: RequestOption) -> ListDatasetsResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=ListDatasetsResponse, option=request_option)

    def get(self, request: GetDatasetRequest, request_option: RequestOption) -> GetDatasetResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetDatasetResponse, option=request_option)

    async def aget(self, request: GetDatasetRequest, request_option: RequestOption) -> GetDatasetResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetDatasetResponse, option=request_option)

    def update(self, request: UpdateDatasetRequest, request_option: RequestOption) -> UpdateDatasetResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateDatasetResponse, option=request_option)

    async def aupdate(self, request: UpdateDatasetRequest, request_option: RequestOption) -> UpdateDatasetResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=UpdateDatasetResponse, option=request_option
        )

    def delete(self, request: DeleteDatasetRequest, request_option: RequestOption) -> DeleteDatasetResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteDatasetResponse, option=request_option)

    async def adelete(self, request: DeleteDatasetRequest, request_option: RequestOption) -> DeleteDatasetResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=DeleteDatasetResponse, option=request_option
        )

    def retrieve(
        self, request: RetrieveFromDatasetRequest, request_option: RequestOption
    ) -> RetrieveFromDatasetResponse:
        return Transport.execute(self.config, request, unmarshal_as=RetrieveFromDatasetResponse, option=request_option)

    async def aretrieve(
        self, request: RetrieveFromDatasetRequest, request_option: RequestOption
    ) -> RetrieveFromDatasetResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=RetrieveFromDatasetResponse, option=request_option
        )
