from dify_oapi.core.model.base_response import BaseResponse


class DeleteTagResponse(BaseResponse):
    result: str | None = None
