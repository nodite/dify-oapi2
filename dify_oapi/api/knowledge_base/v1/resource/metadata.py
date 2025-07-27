from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.metadata.create_request import CreateRequest
from ..model.metadata.create_response import CreateResponse
from ..model.metadata.delete_request import DeleteRequest
from ..model.metadata.delete_response import DeleteResponse
from ..model.metadata.list_request import ListRequest
from ..model.metadata.list_response import ListResponse
from ..model.metadata.toggle_builtin_request import ToggleBuiltinRequest
from ..model.metadata.toggle_builtin_response import ToggleBuiltinResponse
from ..model.metadata.update_document_request import UpdateDocumentRequest
from ..model.metadata.update_document_response import UpdateDocumentResponse
from ..model.metadata.update_request import UpdateRequest
from ..model.metadata.update_response import UpdateResponse


class Metadata:
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

    def toggle_builtin(
        self, request: ToggleBuiltinRequest, option: RequestOption | None = None
    ) -> ToggleBuiltinResponse:
        return Transport.execute(self.config, request, unmarshal_as=ToggleBuiltinResponse, option=option)

    async def atoggle_builtin(
        self, request: ToggleBuiltinRequest, option: RequestOption | None = None
    ) -> ToggleBuiltinResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=ToggleBuiltinResponse, option=option)

    def update_document(
        self, request: UpdateDocumentRequest, option: RequestOption | None = None
    ) -> UpdateDocumentResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateDocumentResponse, option=option)

    async def aupdate_document(
        self, request: UpdateDocumentRequest, option: RequestOption | None = None
    ) -> UpdateDocumentResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UpdateDocumentResponse, option=option)
