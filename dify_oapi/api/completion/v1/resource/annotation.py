from __future__ import annotations

from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.annotation.annotation_reply_settings_request import AnnotationReplySettingsRequest
from ..model.annotation.annotation_reply_settings_response import AnnotationReplySettingsResponse
from ..model.annotation.create_annotation_request import CreateAnnotationRequest
from ..model.annotation.create_annotation_response import CreateAnnotationResponse
from ..model.annotation.delete_annotation_request import DeleteAnnotationRequest
from ..model.annotation.delete_annotation_response import DeleteAnnotationResponse
from ..model.annotation.list_annotations_request import ListAnnotationsRequest
from ..model.annotation.list_annotations_response import ListAnnotationsResponse
from ..model.annotation.query_annotation_reply_status_request import QueryAnnotationReplyStatusRequest
from ..model.annotation.query_annotation_reply_status_response import QueryAnnotationReplyStatusResponse
from ..model.annotation.update_annotation_request import UpdateAnnotationRequest
from ..model.annotation.update_annotation_response import UpdateAnnotationResponse


class Annotation:
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def list_annotations(
        self, request: ListAnnotationsRequest, request_option: RequestOption
    ) -> ListAnnotationsResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListAnnotationsResponse, option=request_option)

    async def alist_annotations(
        self, request: ListAnnotationsRequest, request_option: RequestOption
    ) -> ListAnnotationsResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=ListAnnotationsResponse, option=request_option
        )

    def create_annotation(
        self, request: CreateAnnotationRequest, request_option: RequestOption
    ) -> CreateAnnotationResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateAnnotationResponse, option=request_option)

    async def acreate_annotation(
        self, request: CreateAnnotationRequest, request_option: RequestOption
    ) -> CreateAnnotationResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=CreateAnnotationResponse, option=request_option
        )

    def update_annotation(
        self, request: UpdateAnnotationRequest, request_option: RequestOption
    ) -> UpdateAnnotationResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateAnnotationResponse, option=request_option)

    async def aupdate_annotation(
        self, request: UpdateAnnotationRequest, request_option: RequestOption
    ) -> UpdateAnnotationResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=UpdateAnnotationResponse, option=request_option
        )

    def delete_annotation(
        self, request: DeleteAnnotationRequest, request_option: RequestOption
    ) -> DeleteAnnotationResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteAnnotationResponse, option=request_option)

    async def adelete_annotation(
        self, request: DeleteAnnotationRequest, request_option: RequestOption
    ) -> DeleteAnnotationResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=DeleteAnnotationResponse, option=request_option
        )

    def annotation_reply_settings(
        self, request: AnnotationReplySettingsRequest, request_option: RequestOption
    ) -> AnnotationReplySettingsResponse:
        return Transport.execute(
            self.config, request, unmarshal_as=AnnotationReplySettingsResponse, option=request_option
        )

    async def aannotation_reply_settings(
        self, request: AnnotationReplySettingsRequest, request_option: RequestOption
    ) -> AnnotationReplySettingsResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=AnnotationReplySettingsResponse, option=request_option
        )

    def query_annotation_reply_status(
        self, request: QueryAnnotationReplyStatusRequest, request_option: RequestOption
    ) -> QueryAnnotationReplyStatusResponse:
        return Transport.execute(
            self.config, request, unmarshal_as=QueryAnnotationReplyStatusResponse, option=request_option
        )

    async def aquery_annotation_reply_status(
        self, request: QueryAnnotationReplyStatusRequest, request_option: RequestOption
    ) -> QueryAnnotationReplyStatusResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=QueryAnnotationReplyStatusResponse, option=request_option
        )
