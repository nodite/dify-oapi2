from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .dataset_info import DatasetInfo


class GetResponse(DatasetInfo, BaseResponse):
    """Response model for get dataset details API"""

    pass
