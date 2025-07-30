from __future__ import annotations

from pydantic import BaseModel

from .process_rule import ProcessRule


class UpdateByFileRequestBody(BaseModel):
    """Request body for updating document by file"""

    name: str | None = None
    file: str | None = None
    process_rule: ProcessRule | None = None

    @staticmethod
    def builder() -> UpdateByFileRequestBodyBuilder:
        return UpdateByFileRequestBodyBuilder()


class UpdateByFileRequestBodyBuilder:
    def __init__(self) -> None:
        self._update_by_file_request_body = UpdateByFileRequestBody()

    def build(self) -> UpdateByFileRequestBody:
        return self._update_by_file_request_body

    def name(self, name: str) -> UpdateByFileRequestBodyBuilder:
        self._update_by_file_request_body.name = name
        return self

    def file(self, file: str) -> UpdateByFileRequestBodyBuilder:
        self._update_by_file_request_body.file = file
        return self

    def process_rule(self, process_rule: ProcessRule) -> UpdateByFileRequestBodyBuilder:
        self._update_by_file_request_body.process_rule = process_rule
        return self
