from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.annotation_reply_settings_request import AnnotationReplySettingsRequest
from ..model.annotation_reply_settings_response import AnnotationReplySettingsResponse
from ..model.annotation_reply_status_request import AnnotationReplyStatusRequest
from ..model.annotation_reply_status_response import AnnotationReplyStatusResponse
from ..model.create_annotation_request import CreateAnnotationRequest
from ..model.create_annotation_response import CreateAnnotationResponse
from ..model.delete_annotation_request import DeleteAnnotationRequest
from ..model.delete_annotation_response import DeleteAnnotationResponse
from ..model.get_annotations_request import GetAnnotationsRequest
from ..model.get_annotations_response import GetAnnotationsResponse
from ..model.update_annotation_request import UpdateAnnotationRequest
from ..model.update_annotation_response import UpdateAnnotationResponse


class Annotation:
    def __init__(self, config: Config) -> None:
        self.config = config

    def list(self, request: GetAnnotationsRequest, request_option: RequestOption) -> GetAnnotationsResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetAnnotationsResponse, option=request_option)

    async def alist(self, request: GetAnnotationsRequest, request_option: RequestOption) -> GetAnnotationsResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetAnnotationsResponse, option=request_option
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

    def reply_settings(
        self, request: AnnotationReplySettingsRequest, request_option: RequestOption
    ) -> AnnotationReplySettingsResponse:
        return Transport.execute(
            self.config, request, unmarshal_as=AnnotationReplySettingsResponse, option=request_option
        )

    async def areply_settings(
        self, request: AnnotationReplySettingsRequest, request_option: RequestOption
    ) -> AnnotationReplySettingsResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=AnnotationReplySettingsResponse, option=request_option
        )

    def reply_status(
        self, request: AnnotationReplyStatusRequest, request_option: RequestOption
    ) -> AnnotationReplyStatusResponse:
        return Transport.execute(
            self.config, request, unmarshal_as=AnnotationReplyStatusResponse, option=request_option
        )

    async def areply_status(
        self, request: AnnotationReplyStatusRequest, request_option: RequestOption
    ) -> AnnotationReplyStatusResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=AnnotationReplyStatusResponse, option=request_option
        )
