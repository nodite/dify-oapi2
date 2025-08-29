from dify_oapi.core.model.base_response import BaseResponse

from .document_info import DocumentInfo


class GetResponse(DocumentInfo, BaseResponse):
    """Response model for get document API"""

    pass
