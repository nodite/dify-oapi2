from __future__ import annotations

from typing import Optional, Union

from dify_oapi.api.knowledge_base.v1.model.tag.tag_info import TagInfo
from dify_oapi.core.model.base_response import BaseResponse


class UpdateResponse(BaseResponse):
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    binding_count: Optional[Union[int, str]] = None

    def to_tag_info(self) -> TagInfo:
        return TagInfo(
            id=self.id or "",
            name=self.name or "",
            type=self.type or "",
            binding_count=self.binding_count or 0,
        )
