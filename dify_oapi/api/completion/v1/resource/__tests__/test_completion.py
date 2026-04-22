import httpx
import pytest
import respx

from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody
from dify_oapi.api.completion.v1.model.completion.stop_response_request import StopResponseRequest
from dify_oapi.api.completion.v1.model.completion.stop_response_request_body import StopResponseRequestBody
from dify_oapi.api.completion.v1.resource.completion import Completion


class TestCompletion:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Completion(config)
        self.option = request_option

    @respx.mock
    def test_send_message(self):
        route = respx.post("https://api.dify.ai/v1/completion-messages").mock(
            return_value=httpx.Response(200, json={
                "answer": "The answer is 42.",
                "task_id": "task-123",
                "id": "msg-123",
            })
        )
        body = SendMessageRequestBody.builder().inputs({"query": "What is 42?"}).user("u1").build()
        result = self.resource.send_message(
            SendMessageRequest.builder().request_body(body).build(), self.option
        )
        assert result.answer == "The answer is 42."
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_send_message_stream(self):
        chunks = b"data: hello\n\ndata: world\n\n"
        route = respx.post("https://api.dify.ai/v1/completion-messages").mock(
            return_value=httpx.Response(200, content=chunks)
        )
        body = SendMessageRequestBody.builder().inputs({"query": "Hello"}).user("u1").build()
        gen = self.resource.send_message(
            SendMessageRequest.builder().request_body(body).build(), self.option, stream=True
        )
        collected = b"".join(gen)
        assert b"hello" in collected
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_stop_response(self):
        route = respx.post(
            url__regex=r"https://api\.dify\.ai/v1/completion-messages/[^/]+/stop"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        body = StopResponseRequestBody.builder().user("u1").build()
        result = self.resource.stop_response(
            StopResponseRequest.builder().task_id("task-123").request_body(body).build(),
            self.option,
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
