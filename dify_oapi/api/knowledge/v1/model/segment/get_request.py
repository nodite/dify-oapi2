from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.document_id: str | None = None
        self.segment_id: str | None = None

    @staticmethod
    def builder() -> "GetRequestBuilder":
        return GetRequestBuilder()


class GetRequestBuilder:
    def __init__(self):
        get_request = GetRequest()
        get_request.http_method = HttpMethod.GET
        get_request.uri = "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id"
        self._get_request = get_request

    def build(self) -> GetRequest:
        return self._get_request

    def dataset_id(self, dataset_id: str) -> "GetRequestBuilder":
        self._get_request.dataset_id = dataset_id
        self._get_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> "GetRequestBuilder":
        self._get_request.document_id = document_id
        self._get_request.paths["document_id"] = document_id
        return self

    def segment_id(self, segment_id: str) -> "GetRequestBuilder":
        self._get_request.segment_id = segment_id
        self._get_request.paths["segment_id"] = segment_id
        return self
