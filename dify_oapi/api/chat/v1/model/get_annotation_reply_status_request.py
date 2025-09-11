from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .chat_types import AnnotationAction


class GetAnnotationReplyStatusRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def builder() -> "GetAnnotationReplyStatusRequestBuilder":
        return GetAnnotationReplyStatusRequestBuilder()


class GetAnnotationReplyStatusRequestBuilder:
    def __init__(self) -> None:
        get_annotation_reply_status_request = GetAnnotationReplyStatusRequest()
        get_annotation_reply_status_request.http_method = HttpMethod.GET
        get_annotation_reply_status_request.uri = "/v1/apps/annotation-reply/:action/status/:job_id"
        self._get_annotation_reply_status_request = get_annotation_reply_status_request

    def action(self, action: AnnotationAction) -> "GetAnnotationReplyStatusRequestBuilder":
        self._get_annotation_reply_status_request.paths["action"] = action
        return self

    def job_id(self, job_id: str) -> "GetAnnotationReplyStatusRequestBuilder":
        self._get_annotation_reply_status_request.paths["job_id"] = job_id
        return self

    def build(self) -> GetAnnotationReplyStatusRequest:
        return self._get_annotation_reply_status_request
