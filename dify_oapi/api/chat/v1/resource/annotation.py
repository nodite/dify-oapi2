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
        self.config: Config = config

    def list(self, request: ListAnnotationsRequest, option: RequestOption | None = None) -> ListAnnotationsResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListAnnotationsResponse, option=option)

    async def alist(
        self, request: ListAnnotationsRequest, option: RequestOption | None = None
    ) -> ListAnnotationsResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=ListAnnotationsResponse, option=option)

    def create(self, request: CreateAnnotationRequest, option: RequestOption | None = None) -> CreateAnnotationResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateAnnotationResponse, option=option)

    async def acreate(
        self, request: CreateAnnotationRequest, option: RequestOption | None = None
    ) -> CreateAnnotationResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=CreateAnnotationResponse, option=option)

    def update(self, request: UpdateAnnotationRequest, option: RequestOption | None = None) -> UpdateAnnotationResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateAnnotationResponse, option=option)

    async def aupdate(
        self, request: UpdateAnnotationRequest, option: RequestOption | None = None
    ) -> UpdateAnnotationResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UpdateAnnotationResponse, option=option)

    def delete(self, request: DeleteAnnotationRequest, option: RequestOption | None = None) -> DeleteAnnotationResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteAnnotationResponse, option=option)

    async def adelete(
        self, request: DeleteAnnotationRequest, option: RequestOption | None = None
    ) -> DeleteAnnotationResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=DeleteAnnotationResponse, option=option)

    def configure(
        self, request: ConfigureAnnotationReplyRequest, option: RequestOption | None = None
    ) -> ConfigureAnnotationReplyResponse:
        return Transport.execute(self.config, request, unmarshal_as=ConfigureAnnotationReplyResponse, option=option)

    async def aconfigure(
        self, request: ConfigureAnnotationReplyRequest, option: RequestOption | None = None
    ) -> ConfigureAnnotationReplyResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=ConfigureAnnotationReplyResponse, option=option
        )

    def status(
        self, request: GetAnnotationReplyStatusRequest, option: RequestOption | None = None
    ) -> GetAnnotationReplyStatusResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetAnnotationReplyStatusResponse, option=option)

    async def astatus(
        self, request: GetAnnotationReplyStatusRequest, option: RequestOption | None = None
    ) -> GetAnnotationReplyStatusResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetAnnotationReplyStatusResponse, option=option
        )
