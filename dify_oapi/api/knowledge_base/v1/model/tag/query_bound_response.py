from __future__ import annotations

from dify_oapi.api.knowledge_base.v1.model.tag.tag_info import TagInfo
from dify_oapi.core.model.base_response import BaseResponse


class QueryBoundResponse(BaseResponse):
    data: list[TagInfo] = []
    total: int = 0
