from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.configure_annotation_reply_request import ConfigureAnnotationReplyRequest
from ..model.configure_annotation_reply_response import ConfigureAnnotationReplyResponse
from ..model.create_annotation_request import CreateAnnotationRequest
from ..model.create_annotation_response import CreateAnnotationResponse
from ..model.delete_annotation_request import DeleteAnnotationRequest
from ..model.delete_annotation_response import DeleteAnnotationResponse
from ..model.get_annotation_reply_status_request import GetAnnotationReplyStatusRequest
from ..model.get_annotation_reply_status_response import GetAnnotationReplyStatusResponse
from ..model.list_annotations_request import ListAnnotationsRequest
from ..model.list_annotations_response import ListAnnotationsResponse
from ..model.update_annotation_request import UpdateAnnotationRequest
from ..model.update_annotation_response import UpdateAnnotationResponse


class Annotation:
    def __init__(self, config: Config) -> None:
        self.config = config

    def list(self, request: ListAnnotationsRequest, request_option: RequestOption) -> ListAnnotationsResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListAnnotationsResponse, option=request_option)

    async def alist(self, request: ListAnnotationsRequest, request_option: RequestOption) -> ListAnnotationsResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=ListAnnotationsResponse, option=request_option
        )

    def create(self, request: CreateAnnotationRequest, request_option: RequestOption) -> CreateAnnotationResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateAnnotationResponse, option=request_option)

    async def acreate(
        self, request: CreateAnnotationRequest, request_option: RequestOption
    ) -> CreateAnnotationResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=CreateAnnotationResponse, option=request_option
        )

    def update(self, request: UpdateAnnotationRequest, request_option: RequestOption) -> UpdateAnnotationResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateAnnotationResponse, option=request_option)

    async def aupdate(
        self, request: UpdateAnnotationRequest, request_option: RequestOption
    ) -> UpdateAnnotationResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=UpdateAnnotationResponse, option=request_option
        )

    def delete(self, request: DeleteAnnotationRequest, request_option: RequestOption) -> DeleteAnnotationResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteAnnotationResponse, option=request_option)

    async def adelete(
        self, request: DeleteAnnotationRequest, request_option: RequestOption
    ) -> DeleteAnnotationResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=DeleteAnnotationResponse, option=request_option
        )

    def configure(
        self, request: ConfigureAnnotationReplyRequest, request_option: RequestOption
    ) -> ConfigureAnnotationReplyResponse:
        return Transport.execute(
            self.config, request, unmarshal_as=ConfigureAnnotationReplyResponse, option=request_option
        )

    async def aconfigure(
        self, request: ConfigureAnnotationReplyRequest, request_option: RequestOption
    ) -> ConfigureAnnotationReplyResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=ConfigureAnnotationReplyResponse, option=request_option
        )

    def status(
        self, request: GetAnnotationReplyStatusRequest, request_option: RequestOption
    ) -> GetAnnotationReplyStatusResponse:
        return Transport.execute(
            self.config, request, unmarshal_as=GetAnnotationReplyStatusResponse, option=request_option
        )

    async def astatus(
        self, request: GetAnnotationReplyStatusRequest, request_option: RequestOption
    ) -> GetAnnotationReplyStatusResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetAnnotationReplyStatusResponse, option=request_option
        )
