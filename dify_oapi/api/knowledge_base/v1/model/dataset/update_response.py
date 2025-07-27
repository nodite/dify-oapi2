from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .dataset_info import DatasetInfo


class UpdateResponse(DatasetInfo, BaseResponse):
    """Response model for update dataset API"""

    pass
