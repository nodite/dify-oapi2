from __future__ import annotations

from pydantic import BaseModel


class MetadataInfo(BaseModel):
    id: str
    name: str
    type: str
    use_count: int | None = None

    @staticmethod
    def builder() -> MetadataInfoBuilder:
        return MetadataInfoBuilder()


class MetadataInfoBuilder:
    def __init__(self):
        self._metadata_info = MetadataInfo(id="", name="", type="")

    def build(self) -> MetadataInfo:
        return self._metadata_info

    def id(self, id: str) -> MetadataInfoBuilder:
        self._metadata_info.id = id
        return self

    def name(self, name: str) -> MetadataInfoBuilder:
        self._metadata_info.name = name
        return self

    def type(self, type: str) -> MetadataInfoBuilder:
        self._metadata_info.type = type
        return self

    def use_count(self, use_count: int) -> MetadataInfoBuilder:
        self._metadata_info.use_count = use_count
        return self
