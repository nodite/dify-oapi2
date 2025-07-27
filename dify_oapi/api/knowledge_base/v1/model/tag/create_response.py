from __future__ import annotations

from dify_oapi.api.knowledge_base.v1.model.tag.tag_info import TagInfo
from dify_oapi.core.model.base_response import BaseResponse


class CreateResponse(BaseResponse):
    id: str | None = None
    name: str | None = None
    type: str | None = None
    binding_count: int | None = None

    def to_tag_info(self) -> TagInfo:
        return TagInfo(
            id=self.id or "", name=self.name or "", type=self.type or "", binding_count=self.binding_count or 0
        )
