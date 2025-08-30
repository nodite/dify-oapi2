from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .parameters_info import ParametersInfo


class GetParametersResponse(ParametersInfo, BaseResponse):
    pass
