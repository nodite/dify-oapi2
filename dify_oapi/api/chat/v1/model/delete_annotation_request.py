from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class DeleteAnnotationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def builder() -> "DeleteAnnotationRequestBuilder":
        return DeleteAnnotationRequestBuilder()


class DeleteAnnotationRequestBuilder:
    def __init__(self) -> None:
        delete_annotation_request = DeleteAnnotationRequest()
        delete_annotation_request.http_method = HttpMethod.DELETE
        delete_annotation_request.uri = "/v1/apps/annotations/:annotation_id"
        self._delete_annotation_request = delete_annotation_request

    def annotation_id(self, annotation_id: str) -> "DeleteAnnotationRequestBuilder":
        self._delete_annotation_request.paths["annotation_id"] = annotation_id
        return self

    def build(self) -> DeleteAnnotationRequest:
        return self._delete_annotation_request
