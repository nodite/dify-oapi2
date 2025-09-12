from collections.abc import AsyncGenerator, Generator
from typing import Literal, overload

from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.chat_request import ChatRequest
from ..model.chat_response import ChatResponse
from ..model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from ..model.get_suggested_questions_response import GetSuggestedQuestionsResponse
from ..model.stop_chat_request import StopChatRequest
from ..model.stop_chat_response import StopChatResponse


class Chat:
    def __init__(self, config: Config) -> None:
        self.config = config

    @overload
    def chat(
        self,
        request: ChatRequest,
        request_option: RequestOption,
        stream: Literal[True],
    ) -> Generator[bytes, None, None]: ...

    @overload
    def chat(
        self,
        request: ChatRequest,
        request_option: RequestOption,
        stream: Literal[False] = False,
    ) -> ChatResponse: ...

    def chat(
        self,
        request: ChatRequest,
        request_option: RequestOption,
        stream: bool = False,
    ) -> ChatResponse | Generator[bytes, None, None]:
        if stream:
            return Transport.execute(self.config, request, stream=True, option=request_option)
        return Transport.execute(self.config, request, unmarshal_as=ChatResponse, option=request_option)

    @overload
    async def achat(
        self,
        request: ChatRequest,
        request_option: RequestOption,
        stream: Literal[True],
    ) -> AsyncGenerator[bytes, None]: ...

    @overload
    async def achat(
        self,
        request: ChatRequest,
        request_option: RequestOption,
        stream: Literal[False] = False,
    ) -> ChatResponse: ...

    async def achat(
        self,
        request: ChatRequest,
        request_option: RequestOption,
        stream: bool = False,
    ) -> ChatResponse | AsyncGenerator[bytes, None]:
        if stream:
            return await ATransport.aexecute(self.config, request, stream=True, option=request_option)
        return await ATransport.aexecute(self.config, request, unmarshal_as=ChatResponse, option=request_option)

    def stop(self, request: StopChatRequest, request_option: RequestOption) -> StopChatResponse:
        return Transport.execute(self.config, request, unmarshal_as=StopChatResponse, option=request_option)

    async def astop(self, request: StopChatRequest, request_option: RequestOption) -> StopChatResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=StopChatResponse, option=request_option)

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
