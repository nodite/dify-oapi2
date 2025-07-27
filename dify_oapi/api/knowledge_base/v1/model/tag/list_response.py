from __future__ import annotations

from typing import List

from dify_oapi.core.model.base_response import BaseResponse

from dify_oapi.api.knowledge_base.v1.model.tag.tag_info import TagInfo


class ListResponse(BaseResponse):
    # For tag list API, the response is directly an array
    # We'll handle this in the transport layer by wrapping the array
    data: List[TagInfo] = []

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)
