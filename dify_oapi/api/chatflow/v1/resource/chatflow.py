from collections.abc import AsyncGenerator, Generator
from typing import Literal, overload

from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from ..model.get_suggested_questions_response import GetSuggestedQuestionsResponse
from ..model.send_chat_message_request import SendChatMessageRequest
from ..model.send_chat_message_response import SendChatMessageResponse
from ..model.stop_chat_message_request import StopChatMessageRequest
from ..model.stop_chat_message_response import StopChatMessageResponse


class Chatflow:
    def __init__(self, config: Config) -> None:
        self.config = config

    @overload
    def send(
        self,
        request: SendChatMessageRequest,
        request_option: RequestOption,
        stream: Literal[True],
    ) -> Generator[bytes, None, None]: ...

    @overload
    def send(
        self,
        request: SendChatMessageRequest,
        request_option: RequestOption,
        stream: Literal[False] = False,
    ) -> SendChatMessageResponse: ...

    def send(
        self,
        request: SendChatMessageRequest,
        request_option: RequestOption,
        stream: bool = False,
    ) -> SendChatMessageResponse | Generator[bytes, None, None]:
        if stream:
            return Transport.execute(self.config, request, stream=True, option=request_option)
        return Transport.execute(self.config, request, unmarshal_as=SendChatMessageResponse, option=request_option)

    async def asend(
        self,
        request: SendChatMessageRequest,
        request_option: RequestOption,
        stream: bool = False,
    ) -> SendChatMessageResponse | AsyncGenerator[bytes, None]:
        if stream:
            return await ATransport.aexecute(self.config, request, stream=True, option=request_option)
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=SendChatMessageResponse, option=request_option
        )

    def stop(self, request: StopChatMessageRequest, request_option: RequestOption) -> StopChatMessageResponse:
        return Transport.execute(self.config, request, unmarshal_as=StopChatMessageResponse, option=request_option)

    async def astop(self, request: StopChatMessageRequest, request_option: RequestOption) -> StopChatMessageResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=StopChatMessageResponse, option=request_option
        )

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
