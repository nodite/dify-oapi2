from __future__ import annotations

from typing import List

from dify_oapi.core.model.base_response import BaseResponse

from dify_oapi.api.knowledge_base.v1.model.tag.tag_info import TagInfo


class QueryBoundResponse(BaseResponse):
    data: List[TagInfo] = []
    total: int = 0
