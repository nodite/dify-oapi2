from __future__ import annotations

from dify_oapi.api.knowledge_base.v1.model.tag.tag_info import TagInfo
from dify_oapi.core.model.base_response import BaseResponse


class UpdateResponse(BaseResponse):
    id: str | None = None
    name: str | None = None
    type: str | None = None
    binding_count: int | str | None = None

    def to_tag_info(self) -> TagInfo:
        binding_count = None
        if self.binding_count is not None:
            binding_count = int(self.binding_count) if isinstance(self.binding_count, str) else self.binding_count

        return TagInfo(
            id=self.id or "",
            name=self.name or "",
            type=self.type or "",
            binding_count=binding_count or 0,
        )
