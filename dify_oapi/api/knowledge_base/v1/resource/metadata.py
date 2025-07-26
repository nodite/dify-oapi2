from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.metadata.create_request import CreateMetadataRequest
from ..model.metadata.create_response import CreateMetadataResponse
from ..model.metadata.list_request import ListMetadataRequest
from ..model.metadata.list_response import ListMetadataResponse
from ..model.metadata.update_request import UpdateMetadataRequest
from ..model.metadata.update_response import UpdateMetadataResponse
from ..model.metadata.delete_request import DeleteMetadataRequest
from ..model.metadata.delete_response import DeleteMetadataResponse
from ..model.metadata.toggle_builtin_request import ToggleBuiltinMetadataRequest
from ..model.metadata.toggle_builtin_response import ToggleBuiltinMetadataResponse
from ..model.metadata.update_document_request import UpdateDocumentMetadataRequest
from ..model.metadata.update_document_response import UpdateDocumentMetadataResponse


class Metadata:
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateMetadataRequest, option: RequestOption | None = None) -> CreateMetadataResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateMetadataResponse, option=option)

    async def acreate(
        self, request: CreateMetadataRequest, option: RequestOption | None = None
    ) -> CreateMetadataResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=CreateMetadataResponse, option=option)

    def list(self, request: ListMetadataRequest, option: RequestOption | None = None) -> ListMetadataResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListMetadataResponse, option=option)

    async def alist(self, request: ListMetadataRequest, option: RequestOption | None = None) -> ListMetadataResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=ListMetadataResponse, option=option)

    def update(self, request: UpdateMetadataRequest, option: RequestOption | None = None) -> UpdateMetadataResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateMetadataResponse, option=option)

    async def aupdate(self, request: UpdateMetadataRequest, option: RequestOption | None = None) -> UpdateMetadataResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UpdateMetadataResponse, option=option)

    def delete(self, request: DeleteMetadataRequest, option: RequestOption | None = None) -> DeleteMetadataResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteMetadataResponse, option=option)

    async def adelete(
        self, request: DeleteMetadataRequest, option: RequestOption | None = None
    ) -> DeleteMetadataResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=DeleteMetadataResponse, option=option)

    def toggle_builtin(self, request: ToggleBuiltinMetadataRequest, option: RequestOption | None = None) -> ToggleBuiltinMetadataResponse:
        return Transport.execute(self.config, request, unmarshal_as=ToggleBuiltinMetadataResponse, option=option)

    async def atoggle_builtin(self, request: ToggleBuiltinMetadataRequest, option: RequestOption | None = None) -> ToggleBuiltinMetadataResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=ToggleBuiltinMetadataResponse, option=option)

    def update_document(self, request: UpdateDocumentMetadataRequest, option: RequestOption | None = None) -> UpdateDocumentMetadataResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateDocumentMetadataResponse, option=option)

    async def aupdate_document(self, request: UpdateDocumentMetadataRequest, option: RequestOption | None = None) -> UpdateDocumentMetadataResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UpdateDocumentMetadataResponse, option=option)