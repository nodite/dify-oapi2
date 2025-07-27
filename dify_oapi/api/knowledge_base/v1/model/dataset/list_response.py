from __future__ import annotations

from typing import List, Optional

from dify_oapi.core.model.base_response import BaseResponse

from .dataset_info import DatasetInfo


class ListResponse(BaseResponse):
    data: Optional[List[DatasetInfo]] = None
    has_more: Optional[bool] = None
    limit: Optional[int] = None
    total: Optional[int] = None
    page: Optional[int] = None