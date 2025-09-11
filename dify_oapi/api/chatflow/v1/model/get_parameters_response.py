from dify_oapi.core.model.base_response import BaseResponse

from .app_parameters import AppParameters


class GetParametersResponse(AppParameters, BaseResponse):
    pass
