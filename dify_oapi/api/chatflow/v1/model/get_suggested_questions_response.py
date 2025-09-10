from dify_oapi.core.model.base_response import BaseResponse


class GetSuggestedQuestionsResponse(BaseResponse):
    result: str | None = None
    data: list[str] | None = None
