from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetAnnotationsRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> "GetAnnotationsRequestBuilder":
        return GetAnnotationsRequestBuilder()


class GetAnnotationsRequestBuilder:
    def __init__(self):
        get_annotations_request = GetAnnotationsRequest()
        get_annotations_request.http_method = HttpMethod.GET
        get_annotations_request.uri = "/v1/apps/annotations"
        self._get_annotations_request = get_annotations_request

    def build(self) -> GetAnnotationsRequest:
        return self._get_annotations_request

    def page(self, page: int) -> "GetAnnotationsRequestBuilder":
        self._get_annotations_request.add_query("page", page)
        return self

    def limit(self, limit: int) -> "GetAnnotationsRequestBuilder":
        self._get_annotations_request.add_query("limit", limit)
        return self
