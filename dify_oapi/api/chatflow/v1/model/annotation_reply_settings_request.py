from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .annotation_reply_settings_request_body import AnnotationReplySettingsRequestBody
from .chatflow_types import AnnotationAction


class AnnotationReplySettingsRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: AnnotationReplySettingsRequestBody | None = None
        self.action: AnnotationAction | None = None

    @staticmethod
    def builder() -> "AnnotationReplySettingsRequestBuilder":
        return AnnotationReplySettingsRequestBuilder()


class AnnotationReplySettingsRequestBuilder:
    def __init__(self):
        annotation_reply_settings_request = AnnotationReplySettingsRequest()
        annotation_reply_settings_request.http_method = HttpMethod.POST
        annotation_reply_settings_request.uri = "/v1/apps/annotation-reply/:action"
        self._annotation_reply_settings_request = annotation_reply_settings_request

    def build(self) -> AnnotationReplySettingsRequest:
        return self._annotation_reply_settings_request

    def action(self, action: AnnotationAction) -> "AnnotationReplySettingsRequestBuilder":
        self._annotation_reply_settings_request.action = action
        self._annotation_reply_settings_request.paths["action"] = action
        return self

    def request_body(self, request_body: AnnotationReplySettingsRequestBody) -> "AnnotationReplySettingsRequestBuilder":
        self._annotation_reply_settings_request.request_body = request_body
        self._annotation_reply_settings_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
