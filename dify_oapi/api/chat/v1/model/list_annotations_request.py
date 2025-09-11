from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class ListAnnotationsRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def builder() -> "ListAnnotationsRequestBuilder":
        return ListAnnotationsRequestBuilder()


class ListAnnotationsRequestBuilder:
    def __init__(self) -> None:
        list_annotations_request = ListAnnotationsRequest()
        list_annotations_request.http_method = HttpMethod.GET
        list_annotations_request.uri = "/v1/apps/annotations"
        self._list_annotations_request = list_annotations_request

    def page(self, page: int | None) -> "ListAnnotationsRequestBuilder":
        if page is not None:
            self._list_annotations_request.add_query("page", str(page))
        return self

    def limit(self, limit: int | None) -> "ListAnnotationsRequestBuilder":
        if limit is not None:
            self._list_annotations_request.add_query("limit", str(limit))
        return self

    def build(self) -> ListAnnotationsRequest:
        return self._list_annotations_request
