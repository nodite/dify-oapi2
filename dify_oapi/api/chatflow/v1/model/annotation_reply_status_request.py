from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .chatflow_types import AnnotationAction


class AnnotationReplyStatusRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.action: AnnotationAction | None = None
        self.job_id: str | None = None

    @staticmethod
    def builder() -> "AnnotationReplyStatusRequestBuilder":
        return AnnotationReplyStatusRequestBuilder()


class AnnotationReplyStatusRequestBuilder:
    def __init__(self):
        annotation_reply_status_request = AnnotationReplyStatusRequest()
        annotation_reply_status_request.http_method = HttpMethod.GET
        annotation_reply_status_request.uri = "/v1/apps/annotation-reply/:action/status/:job_id"
        self._annotation_reply_status_request = annotation_reply_status_request

    def build(self) -> AnnotationReplyStatusRequest:
        return self._annotation_reply_status_request

    def action(self, action: AnnotationAction) -> "AnnotationReplyStatusRequestBuilder":
        self._annotation_reply_status_request.action = action
        self._annotation_reply_status_request.paths["action"] = action
        return self

    def job_id(self, job_id: str) -> "AnnotationReplyStatusRequestBuilder":
        self._annotation_reply_status_request.job_id = job_id
        self._annotation_reply_status_request.paths["job_id"] = job_id
        return self
