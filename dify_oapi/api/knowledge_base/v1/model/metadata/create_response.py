from __future__ import annotations

from dify_oapi.api.knowledge_base.v1.model.metadata.metadata_info import MetadataInfo
from dify_oapi.core.model.base_response import BaseResponse


class CreateResponse(BaseResponse):
    id: str | None = None
    type: str | None = None
    name: str | None = None

    def to_metadata_info(self) -> MetadataInfo:
        return MetadataInfo(id=self.id or "", type=self.type or "", name=self.name or "")
