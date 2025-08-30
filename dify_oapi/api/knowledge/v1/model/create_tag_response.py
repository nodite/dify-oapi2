from dify_oapi.core.model.base_response import BaseResponse

from .tag_info import TagInfo


class CreateTagResponse(TagInfo, BaseResponse):
    pass
