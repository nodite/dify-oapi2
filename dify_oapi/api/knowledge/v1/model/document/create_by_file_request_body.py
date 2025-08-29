"""Create document by file request body model."""

from __future__ import annotations

from pydantic import BaseModel

from .create_by_file_request_body_data import CreateByFileRequestBodyData


class CreateByFileRequestBody(BaseModel):
    """Request body model for create document by file API."""

    data: str | None = None

    @staticmethod
    def builder() -> CreateByFileRequestBodyBuilder:
        return CreateByFileRequestBodyBuilder()


class CreateByFileRequestBodyBuilder:
    """Builder for CreateByFileRequestBody."""

    def __init__(self) -> None:
        self._create_by_file_request_body = CreateByFileRequestBody()

    def build(self) -> CreateByFileRequestBody:
        return self._create_by_file_request_body

    def data(self, data: CreateByFileRequestBodyData) -> CreateByFileRequestBodyBuilder:
        self._create_by_file_request_body.data = data.model_dump_json(exclude_none=True)
        return self
