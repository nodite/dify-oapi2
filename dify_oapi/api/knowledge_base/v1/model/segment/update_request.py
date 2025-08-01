from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .update_request_body import UpdateRequestBody


class UpdateRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.document_id: str | None = None
        self.segment_id: str | None = None
        self.request_body: UpdateRequestBody | None = None

    @staticmethod
    def builder() -> "UpdateRequestBuilder":
        return UpdateRequestBuilder()


class UpdateRequestBuilder:
    def __init__(self):
        update_request = UpdateRequest()
        update_request.http_method = HttpMethod.POST
        update_request.uri = "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id"
        self._update_request = update_request

    def build(self) -> UpdateRequest:
        return self._update_request

    def dataset_id(self, dataset_id: str) -> "UpdateRequestBuilder":
        self._update_request.dataset_id = dataset_id
        self._update_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> "UpdateRequestBuilder":
        self._update_request.document_id = document_id
        self._update_request.paths["document_id"] = document_id
        return self

    def segment_id(self, segment_id: str) -> "UpdateRequestBuilder":
        self._update_request.segment_id = segment_id
        self._update_request.paths["segment_id"] = segment_id
        return self

    def request_body(self, request_body: UpdateRequestBody) -> "UpdateRequestBuilder":
        self._update_request.request_body = request_body
        self._update_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
