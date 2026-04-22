import httpx
import pytest
import respx

from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.api.chat.v1.resource.chat import Chat


class TestStreaming:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Chat(config)
        self.option = request_option

    @respx.mock
    def test_stream_returns_generator(self):
        chunks = b"data: hello\n\ndata: world\n\n"
        respx.post("https://api.dify.ai/v1/chat-messages").mock(
            return_value=httpx.Response(200, content=chunks)
        )
        body = ChatRequestBody.builder().query("hi").user("u1").build()
        gen = self.resource.chat(
            ChatRequest.builder().request_body(body).build(), self.option, stream=True
        )
        collected = b"".join(gen)
        assert b"hello" in collected
        assert b"world" in collected

    @respx.mock
    async def test_async_stream_returns_async_generator(self):
        chunks = b"data: hello\n\ndata: world\n\n"
        respx.post("https://api.dify.ai/v1/chat-messages").mock(
            return_value=httpx.Response(200, content=chunks)
        )
        body = ChatRequestBody.builder().query("hi").user("u1").build()
        gen = await self.resource.achat(
            ChatRequest.builder().request_body(body).build(), self.option, stream=True
        )
        collected = b""
        async for chunk in gen:
            collected += chunk
        assert b"hello" in collected
