from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .dataset_info import DatasetInfo


class CreateResponse(DatasetInfo, BaseResponse):
    """Response model for dataset creation API"""

    pass
