from dify_oapi.core.model.base_response import BaseResponse

from .annotation_info import AnnotationInfo


class CreateAnnotationResponse(AnnotationInfo, BaseResponse):
    """Response for creating annotation."""

    pass
