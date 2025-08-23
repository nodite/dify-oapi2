from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .update_annotation_request_body import UpdateAnnotationRequestBody


class UpdateAnnotationRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.annotation_id: str | None = None
        self.request_body: UpdateAnnotationRequestBody | None = None

    @staticmethod
    def builder() -> UpdateAnnotationRequestBuilder:
        return UpdateAnnotationRequestBuilder()


class UpdateAnnotationRequestBuilder:
    def __init__(self):
        update_annotation_request = UpdateAnnotationRequest()
        update_annotation_request.http_method = HttpMethod.PUT
        update_annotation_request.uri = "/v1/apps/annotations/:annotation_id"
        self._update_annotation_request = update_annotation_request

    def build(self) -> UpdateAnnotationRequest:
        return self._update_annotation_request

    def annotation_id(self, annotation_id: str) -> UpdateAnnotationRequestBuilder:
        self._update_annotation_request.annotation_id = annotation_id
        self._update_annotation_request.paths["annotation_id"] = annotation_id
        return self

    def request_body(self, request_body: UpdateAnnotationRequestBody) -> UpdateAnnotationRequestBuilder:
        self._update_annotation_request.request_body = request_body
        self._update_annotation_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
