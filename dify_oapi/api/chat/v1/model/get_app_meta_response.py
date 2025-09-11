from dify_oapi.core.model.base_response import BaseResponse

from .tool_icon import ToolIcon


class GetAppMetaResponse(ToolIcon, BaseResponse):
    """Response for get application meta information API."""

    pass
