from __future__ import annotations

from typing import Literal

from pydantic import BaseModel

from .process_rule import ProcessRule


class UpdateByFileRequestBodyData(BaseModel):
    name: str | None = None
    indexing_technique: str | None = None
    process_rule: ProcessRule | None = None

    @staticmethod
    def builder() -> UpdateByFileRequestBodyDataBuilder:
        return UpdateByFileRequestBodyDataBuilder()


class UpdateByFileRequestBodyDataBuilder:
    def __init__(self):
        update_by_file_request_body_data = UpdateByFileRequestBodyData()
        self._update_by_file_request_body_data = update_by_file_request_body_data

    def build(self) -> UpdateByFileRequestBodyData:
        return self._update_by_file_request_body_data

    def name(self, name: str) -> UpdateByFileRequestBodyDataBuilder:
        self._update_by_file_request_body_data.name = name
        return self

    def indexing_technique(
        self, indexing_technique: Literal["high_quality", "economy"]
    ) -> UpdateByFileRequestBodyDataBuilder:
        self._update_by_file_request_body_data.indexing_technique = indexing_technique
        return self

    def process_rule(self, process_rule: ProcessRule) -> UpdateByFileRequestBodyDataBuilder:
        self._update_by_file_request_body_data.process_rule = process_rule
        return self
