from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.create_document_by_file_request import CreateDocumentByFileRequest
from ..model.create_document_by_file_response import CreateDocumentByFileResponse
from ..model.create_document_by_text_request import CreateDocumentByTextRequest
from ..model.create_document_by_text_response import CreateDocumentByTextResponse
from ..model.delete_document_request import DeleteDocumentRequest
from ..model.delete_document_response import DeleteDocumentResponse
from ..model.get_batch_indexing_status_request import GetBatchIndexingStatusRequest
from ..model.get_batch_indexing_status_response import GetBatchIndexingStatusResponse
from ..model.get_document_request import GetDocumentRequest
from ..model.get_document_response import GetDocumentResponse
from ..model.get_upload_file_info_request import GetUploadFileInfoRequest
from ..model.get_upload_file_info_response import GetUploadFileInfoResponse
from ..model.list_documents_request import ListDocumentsRequest
from ..model.list_documents_response import ListDocumentsResponse
from ..model.update_document_by_file_request import UpdateDocumentByFileRequest
from ..model.update_document_by_file_response import UpdateDocumentByFileResponse
from ..model.update_document_by_text_request import UpdateDocumentByTextRequest
from ..model.update_document_by_text_response import UpdateDocumentByTextResponse
from ..model.update_document_status_request import UpdateDocumentStatusRequest
from ..model.update_document_status_response import UpdateDocumentStatusResponse


class Document:
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create_by_file(
        self, request: CreateDocumentByFileRequest, request_option: RequestOption
    ) -> CreateDocumentByFileResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateDocumentByFileResponse, option=request_option)

    async def acreate_by_file(
        self, request: CreateDocumentByFileRequest, request_option: RequestOption
    ) -> CreateDocumentByFileResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=CreateDocumentByFileResponse, option=request_option
        )

    def create_by_text(
        self, request: CreateDocumentByTextRequest, request_option: RequestOption
    ) -> CreateDocumentByTextResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateDocumentByTextResponse, option=request_option)

    async def acreate_by_text(
        self, request: CreateDocumentByTextRequest, request_option: RequestOption
    ) -> CreateDocumentByTextResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=CreateDocumentByTextResponse, option=request_option
        )

    def list(self, request: ListDocumentsRequest, request_option: RequestOption) -> ListDocumentsResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListDocumentsResponse, option=request_option)

    async def alist(self, request: ListDocumentsRequest, request_option: RequestOption) -> ListDocumentsResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=ListDocumentsResponse, option=request_option
        )

    def get(self, request: GetDocumentRequest, request_option: RequestOption) -> GetDocumentResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetDocumentResponse, option=request_option)

    async def aget(self, request: GetDocumentRequest, request_option: RequestOption) -> GetDocumentResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetDocumentResponse, option=request_option)

    def update_by_file(
        self, request: UpdateDocumentByFileRequest, request_option: RequestOption
    ) -> UpdateDocumentByFileResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateDocumentByFileResponse, option=request_option)

    async def aupdate_by_file(
        self, request: UpdateDocumentByFileRequest, request_option: RequestOption
    ) -> UpdateDocumentByFileResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=UpdateDocumentByFileResponse, option=request_option
        )

    def update_by_text(
        self, request: UpdateDocumentByTextRequest, request_option: RequestOption
    ) -> UpdateDocumentByTextResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateDocumentByTextResponse, option=request_option)

    async def aupdate_by_text(
        self, request: UpdateDocumentByTextRequest, request_option: RequestOption
    ) -> UpdateDocumentByTextResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=UpdateDocumentByTextResponse, option=request_option
        )

    def delete(self, request: DeleteDocumentRequest, request_option: RequestOption) -> DeleteDocumentResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteDocumentResponse, option=request_option)

    async def adelete(self, request: DeleteDocumentRequest, request_option: RequestOption) -> DeleteDocumentResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=DeleteDocumentResponse, option=request_option
        )

    def file_info(self, request: GetUploadFileInfoRequest, request_option: RequestOption) -> GetUploadFileInfoResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetUploadFileInfoResponse, option=request_option)

    async def afile_info(
        self, request: GetUploadFileInfoRequest, request_option: RequestOption
    ) -> GetUploadFileInfoResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetUploadFileInfoResponse, option=request_option
        )

    def update_status(
        self, request: UpdateDocumentStatusRequest, request_option: RequestOption
    ) -> UpdateDocumentStatusResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateDocumentStatusResponse, option=request_option)

    async def aupdate_status(
        self, request: UpdateDocumentStatusRequest, request_option: RequestOption
    ) -> UpdateDocumentStatusResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=UpdateDocumentStatusResponse, option=request_option
        )

    def get_batch_status(
        self, request: GetBatchIndexingStatusRequest, request_option: RequestOption
    ) -> GetBatchIndexingStatusResponse:
        return Transport.execute(
            self.config, request, unmarshal_as=GetBatchIndexingStatusResponse, option=request_option
        )

    async def aget_batch_status(
        self, request: GetBatchIndexingStatusRequest, request_option: RequestOption
    ) -> GetBatchIndexingStatusResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetBatchIndexingStatusResponse, option=request_option
        )
