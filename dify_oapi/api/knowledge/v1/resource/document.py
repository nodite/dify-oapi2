from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.document.create_by_file_request import CreateByFileRequest
from ..model.document.create_by_file_response import CreateByFileResponse
from ..model.document.create_by_text_request import CreateByTextRequest
from ..model.document.create_by_text_response import CreateByTextResponse
from ..model.document.delete_request import DeleteRequest
from ..model.document.delete_response import DeleteResponse
from ..model.document.get_request import GetRequest
from ..model.document.get_response import GetResponse
from ..model.document.get_upload_file_request import GetUploadFileRequest
from ..model.document.get_upload_file_response import GetUploadFileResponse
from ..model.document.indexing_status_request import IndexingStatusRequest
from ..model.document.indexing_status_response import IndexingStatusResponse
from ..model.document.list_request import ListRequest
from ..model.document.list_response import ListResponse
from ..model.document.update_by_file_request import UpdateByFileRequest
from ..model.document.update_by_file_response import UpdateByFileResponse
from ..model.document.update_by_text_request import UpdateByTextRequest
from ..model.document.update_by_text_response import UpdateByTextResponse
from ..model.document.update_status_request import UpdateStatusRequest
from ..model.document.update_status_response import UpdateStatusResponse


class Document:
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create_by_text(self, request: CreateByTextRequest, option: RequestOption | None = None) -> CreateByTextResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateByTextResponse, option=option)

    async def acreate_by_text(
        self, request: CreateByTextRequest, option: RequestOption | None = None
    ) -> CreateByTextResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=CreateByTextResponse, option=option)

    def update_by_text(self, request: UpdateByTextRequest, option: RequestOption | None = None) -> UpdateByTextResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateByTextResponse, option=option)

    async def aupdate_by_text(
        self, request: UpdateByTextRequest, option: RequestOption | None = None
    ) -> UpdateByTextResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UpdateByTextResponse, option=option)

    def create_by_file(self, request: CreateByFileRequest, option: RequestOption | None = None) -> CreateByFileResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateByFileResponse, option=option)

    async def acreate_by_file(
        self, request: CreateByFileRequest, option: RequestOption | None = None
    ) -> CreateByFileResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=CreateByFileResponse, option=option)

    def update_by_file(self, request: UpdateByFileRequest, option: RequestOption | None = None) -> UpdateByFileResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateByFileResponse, option=option)

    async def aupdate_by_file(
        self, request: UpdateByFileRequest, option: RequestOption | None = None
    ) -> UpdateByFileResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UpdateByFileResponse, option=option)

    def list(self, request: ListRequest, option: RequestOption | None = None) -> ListResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListResponse, option=option)

    async def alist(self, request: ListRequest, option: RequestOption | None = None) -> ListResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=ListResponse, option=option)

    def delete(self, request: DeleteRequest, option: RequestOption | None = None) -> DeleteResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteResponse, option=option)

    async def adelete(self, request: DeleteRequest, option: RequestOption | None = None) -> DeleteResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=DeleteResponse, option=option)

    def indexing_status(
        self, request: IndexingStatusRequest, option: RequestOption | None = None
    ) -> IndexingStatusResponse:
        return Transport.execute(self.config, request, unmarshal_as=IndexingStatusResponse, option=option)

    async def aindexing_status(
        self, request: IndexingStatusRequest, option: RequestOption | None = None
    ) -> IndexingStatusResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=IndexingStatusResponse, option=option)

    def get(self, request: GetRequest, option: RequestOption | None = None) -> GetResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetResponse, option=option)

    async def aget(self, request: GetRequest, option: RequestOption | None = None) -> GetResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetResponse, option=option)

    def update_status(self, request: UpdateStatusRequest, option: RequestOption | None = None) -> UpdateStatusResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateStatusResponse, option=option)

    async def aupdate_status(
        self, request: UpdateStatusRequest, option: RequestOption | None = None
    ) -> UpdateStatusResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UpdateStatusResponse, option=option)

    def get_upload_file(
        self, request: GetUploadFileRequest, option: RequestOption | None = None
    ) -> GetUploadFileResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetUploadFileResponse, option=option)

    async def aget_upload_file(
        self, request: GetUploadFileRequest, option: RequestOption | None = None
    ) -> GetUploadFileResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetUploadFileResponse, option=option)
