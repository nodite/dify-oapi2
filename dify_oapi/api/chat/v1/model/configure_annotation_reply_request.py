from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .chat_types import AnnotationAction
from .configure_annotation_reply_request_body import ConfigureAnnotationReplyRequestBody


class ConfigureAnnotationReplyRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: ConfigureAnnotationReplyRequestBody | None = None

    @staticmethod
    def builder() -> "ConfigureAnnotationReplyRequestBuilder":
        return ConfigureAnnotationReplyRequestBuilder()


class ConfigureAnnotationReplyRequestBuilder:
    def __init__(self) -> None:
        configure_annotation_reply_request = ConfigureAnnotationReplyRequest()
        configure_annotation_reply_request.http_method = HttpMethod.POST
        configure_annotation_reply_request.uri = "/v1/apps/annotation-reply/:action"
        self._configure_annotation_reply_request = configure_annotation_reply_request

    def action(self, action: AnnotationAction) -> "ConfigureAnnotationReplyRequestBuilder":
        self._configure_annotation_reply_request.paths["action"] = action
        return self

    def request_body(
        self, request_body: ConfigureAnnotationReplyRequestBody
    ) -> "ConfigureAnnotationReplyRequestBuilder":
        self._configure_annotation_reply_request.request_body = request_body
        self._configure_annotation_reply_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self

    def build(self) -> ConfigureAnnotationReplyRequest:
        return self._configure_annotation_reply_request
