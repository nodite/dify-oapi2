from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody


class TestChatflowModels:
    def test_send_chat_message_request_builder(self):
        body = SendChatMessageRequestBody.builder().query("test query").user("u1").build()
        request = SendChatMessageRequest.builder().request_body(body).build()
        assert request is not None
        assert request.request_body is not None
        assert request.request_body.query == "test query"

    def test_send_chat_message_request_body_builder_fields(self):
        body = (
            SendChatMessageRequestBody.builder()
            .query("hello")
            .user("user-1")
            .conversation_id("conv-1")
            .build()
        )
        assert body.query == "hello"
        assert body.user == "user-1"
        assert body.conversation_id == "conv-1"
