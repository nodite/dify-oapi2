from dify_oapi.core.model.base_response import BaseResponse

from .annotation_info import AnnotationInfo


class ListAnnotationsResponse(BaseResponse):
    data: list[AnnotationInfo] = []
    has_more: bool = False
    limit: int = 20
    total: int = 0
    page: int = 1
