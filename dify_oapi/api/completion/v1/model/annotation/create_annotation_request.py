from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .create_annotation_request_body import CreateAnnotationRequestBody


class CreateAnnotationRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: CreateAnnotationRequestBody | None = None

    @staticmethod
    def builder() -> CreateAnnotationRequestBuilder:
        return CreateAnnotationRequestBuilder()


class CreateAnnotationRequestBuilder:
    def __init__(self):
        create_annotation_request = CreateAnnotationRequest()
        create_annotation_request.http_method = HttpMethod.POST
        create_annotation_request.uri = "/v1/apps/annotations"
        self._create_annotation_request = create_annotation_request

    def build(self) -> CreateAnnotationRequest:
        return self._create_annotation_request

    def request_body(self, request_body: CreateAnnotationRequestBody) -> CreateAnnotationRequestBuilder:
        self._create_annotation_request.request_body = request_body
        self._create_annotation_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
