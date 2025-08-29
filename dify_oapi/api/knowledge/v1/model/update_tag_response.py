from dify_oapi.core.model.base_response import BaseResponse

from .tag_info import TagInfo


class UpdateTagResponse(TagInfo, BaseResponse):
    pass
