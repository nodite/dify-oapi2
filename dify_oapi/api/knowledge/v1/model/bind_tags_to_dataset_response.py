from dify_oapi.core.model.base_response import BaseResponse


class BindTagsToDatasetResponse(BaseResponse):
    result: str | None = None
