from dify_oapi.core.model.base_response import BaseResponse


class UnbindTagsFromDatasetResponse(BaseResponse):
    result: str | None = None
