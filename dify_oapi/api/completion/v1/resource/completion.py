from collections.abc import AsyncIterator, Iterator
from typing import Literal, overload

from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.completion.send_message_request import SendMessageRequest
from ..model.completion.send_message_response import SendMessageResponse
from ..model.completion.stop_response_request import StopResponseRequest
from ..model.completion.stop_response_response import StopResponseResponse


class Completion:
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    @overload
    def send_message(
        self,
        request: SendMessageRequest,
        request_option: RequestOption,
        stream: Literal[True],
    ) -> Iterator[str]: ...

    @overload
    def send_message(
        self,
        request: SendMessageRequest,
        request_option: RequestOption,
        stream: Literal[False] = False,
    ) -> SendMessageResponse: ...

    def send_message(
        self,
        request: SendMessageRequest,
        request_option: RequestOption,
        stream: bool = False,
    ) -> SendMessageResponse | Iterator[str]:
        if stream:
            return Transport.stream(self.config, request, option=request_option)
        return Transport.execute(self.config, request, unmarshal_as=SendMessageResponse, option=request_option)

    @overload
    async def asend_message(
        self,
        request: SendMessageRequest,
        request_option: RequestOption,
        stream: Literal[True],
    ) -> AsyncIterator[str]: ...

    @overload
    async def asend_message(
        self,
        request: SendMessageRequest,
        request_option: RequestOption,
        stream: Literal[False] = False,
    ) -> SendMessageResponse: ...

    async def asend_message(
        self,
        request: SendMessageRequest,
        request_option: RequestOption,
        stream: bool = False,
    ) -> SendMessageResponse | AsyncIterator[str]:
        if stream:
            return ATransport.astream(self.config, request, option=request_option)
        return await ATransport.aexecute(self.config, request, unmarshal_as=SendMessageResponse, option=request_option)

    def stop_response(self, request: StopResponseRequest, request_option: RequestOption) -> StopResponseResponse:
        return Transport.execute(self.config, request, unmarshal_as=StopResponseResponse, option=request_option)

    async def astop_response(self, request: StopResponseRequest, request_option: RequestOption) -> StopResponseResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=StopResponseResponse, option=request_option)
