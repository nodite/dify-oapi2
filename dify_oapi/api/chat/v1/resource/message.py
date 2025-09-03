from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from ..model.get_suggested_questions_response import GetSuggestedQuestionsResponse
from ..model.message_history_request import GetMessageHistoryRequest
from ..model.message_history_response import GetMessageHistoryResponse


class Message:
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def suggested(
        self, request: GetSuggestedQuestionsRequest, option: RequestOption | None = None
    ) -> GetSuggestedQuestionsResponse:
        # Send request
        return Transport.execute(self.config, request, unmarshal_as=GetSuggestedQuestionsResponse, option=option)

    async def asuggested(
        self, request: GetSuggestedQuestionsRequest, option: RequestOption | None = None
    ) -> GetSuggestedQuestionsResponse:
        # Send request
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetSuggestedQuestionsResponse, option=option
        )

    def history(
        self, request: GetMessageHistoryRequest, option: RequestOption | None = None
    ) -> GetMessageHistoryResponse:
        # Send request
        return Transport.execute(self.config, request, unmarshal_as=GetMessageHistoryResponse, option=option)

    async def ahistory(
        self, request: GetMessageHistoryRequest, option: RequestOption | None = None
    ) -> GetMessageHistoryResponse:
        # Send request
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetMessageHistoryResponse, option=option)
