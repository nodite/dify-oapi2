from dify_oapi.core.model.base_response import BaseResponse

from .app_parameters import AppParameters


class GetAppParametersResponse(AppParameters, BaseResponse):
    """Response for get application parameters API."""

    pass
