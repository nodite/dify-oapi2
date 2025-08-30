from dify_oapi.core.model.base_response import BaseResponse

from .tag_info import TagInfo


class GetDatasetTagsResponse(BaseResponse):
    data: list[TagInfo] | None = None
    total: int | None = None
