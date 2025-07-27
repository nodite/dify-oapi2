from __future__ import annotations

from typing import Optional
from dify_oapi.core.model.base_response import BaseResponse

from dify_oapi.api.knowledge_base.v1.model.metadata.metadata_info import MetadataInfo


class UpdateResponse(BaseResponse):
    id: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None

    def to_metadata_info(self) -> MetadataInfo:
        return MetadataInfo(id=self.id or "", type=self.type or "", name=self.name or "")
