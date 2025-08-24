from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class PreviewFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.file_id: str | None = None

    @staticmethod
    def builder() -> PreviewFileRequestBuilder:
        return PreviewFileRequestBuilder()


class PreviewFileRequestBuilder:
    def __init__(self):
        preview_file_request = PreviewFileRequest()
        preview_file_request.http_method = HttpMethod.GET
        preview_file_request.uri = "/v1/files/:file_id/preview"
        self._preview_file_request = preview_file_request

    def build(self) -> PreviewFileRequest:
        return self._preview_file_request

    def file_id(self, file_id: str) -> PreviewFileRequestBuilder:
        self._preview_file_request.file_id = file_id
        self._preview_file_request.paths["file_id"] = file_id
        return self

    def as_attachment(self, as_attachment: bool) -> PreviewFileRequestBuilder:
        self._preview_file_request.add_query("as_attachment", str(as_attachment).lower())
        return self
