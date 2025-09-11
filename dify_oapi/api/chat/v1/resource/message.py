from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from ..model.get_suggested_questions_response import GetSuggestedQuestionsResponse
from ..model.message_history_request import GetMessageHistoryRequest
from ..model.message_history_response import GetMessageHistoryResponse


class Message:
    def __init__(self, config: Config) -> None:
        self.config = config

    def suggested(
        self, request: GetSuggestedQuestionsRequest, request_option: RequestOption
    ) -> GetSuggestedQuestionsResponse:
        return Transport.execute(
            self.config, request, unmarshal_as=GetSuggestedQuestionsResponse, option=request_option
        )

    async def asuggested(
        self, request: GetSuggestedQuestionsRequest, request_option: RequestOption
    ) -> GetSuggestedQuestionsResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetSuggestedQuestionsResponse, option=request_option
        )

    def history(self, request: GetMessageHistoryRequest, request_option: RequestOption) -> GetMessageHistoryResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetMessageHistoryResponse, option=request_option)

    async def ahistory(
        self, request: GetMessageHistoryRequest, request_option: RequestOption
    ) -> GetMessageHistoryResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetMessageHistoryResponse, option=request_option
        )
