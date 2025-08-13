from __future__ import annotations

from pydantic import BaseModel

from .update_by_file_request_body_data import UpdateByFileRequestBodyData


class UpdateByFileRequestBody(BaseModel):
    data: str | None = None

    @staticmethod
    def builder() -> UpdateByFileRequestBodyBuilder:
        return UpdateByFileRequestBodyBuilder()


class UpdateByFileRequestBodyBuilder:
    def __init__(self):
        update_by_file_request_body = UpdateByFileRequestBody()
        self._update_by_file_request_body = update_by_file_request_body

    def build(self) -> UpdateByFileRequestBody:
        return self._update_by_file_request_body

    def data(self, data: UpdateByFileRequestBodyData) -> UpdateByFileRequestBodyBuilder:
        self._update_by_file_request_body.data = data.model_dump_json(exclude_none=True)
        return self
