from dify_oapi.api.chatflow.v1.model.chat_file import ChatFile
from dify_oapi.api.chatflow.v1.model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from dify_oapi.api.chatflow.v1.model.get_suggested_questions_response import GetSuggestedQuestionsResponse
from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody
from dify_oapi.api.chatflow.v1.model.send_chat_message_response import SendChatMessageResponse
from dify_oapi.api.chatflow.v1.model.stop_chat_message_request import StopChatMessageRequest
from dify_oapi.api.chatflow.v1.model.stop_chat_message_request_body import StopChatMessageRequestBody
from dify_oapi.api.chatflow.v1.model.stop_chat_message_response import StopChatMessageResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestSendChatMessageModels:
    def test_request_builder(self):
        request = (
            SendChatMessageRequest.builder()
            .request_body(
                SendChatMessageRequestBody.builder()
                .query("Test message")
                .user("test_user")
                .response_mode("streaming")
                .build()
            )
            .build()
        )

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/chat-messages"
        assert request.request_body is not None
        assert request.request_body.query == "Test message"
        assert request.request_body.user == "test_user"
        assert request.request_body.response_mode == "streaming"

    def test_request_validation(self):
        request_body = SendChatMessageRequestBody()
        assert request_body.query is None
        assert request_body.user is None
        assert request_body.response_mode is None

    def test_request_body_builder(self):
        files = [
            ChatFile.builder().type("document").transfer_method("remote_url").url("https://example.com/doc.pdf").build()
        ]

        request_body = (
            SendChatMessageRequestBody.builder()
            .query("Analyze this document")
            .inputs({"user_name": "Alice"})
            .response_mode("blocking")
            .user("user_123")
            .conversation_id("conv_456")
            .files(files)
            .auto_generate_name(True)
            .build()
        )

        assert request_body.query == "Analyze this document"
        assert request_body.inputs == {"user_name": "Alice"}
        assert request_body.response_mode == "blocking"
        assert request_body.user == "user_123"
        assert request_body.conversation_id == "conv_456"
        assert request_body.files == files
        assert request_body.auto_generate_name is True

    def test_request_body_validation(self):
        request_body = SendChatMessageRequestBody()
        assert request_body.query is None
        assert request_body.inputs is None
        assert request_body.response_mode is None
        assert request_body.user is None
        assert request_body.conversation_id is None
        assert request_body.files is None
        assert request_body.auto_generate_name is None

    def test_response_inheritance(self):
        response = SendChatMessageResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")

    def test_response_data_access(self):
        response = SendChatMessageResponse(
            id="msg_123", conversation_id="conv_456", query="Test query", answer="Test answer"
        )
        assert response.id == "msg_123"
        assert response.conversation_id == "conv_456"
        assert response.query == "Test query"
        assert response.answer == "Test answer"


class TestStopChatMessageModels:
    def test_request_builder(self):
        request = (
            StopChatMessageRequest.builder()
            .task_id("task_123")
            .request_body(StopChatMessageRequestBody.builder().user("test_user").build())
            .build()
        )

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/chat-messages/:task_id/stop"
        assert request.task_id == "task_123"
        assert request.paths["task_id"] == "task_123"
        assert request.request_body is not None
        assert request.request_body.user == "test_user"

    def test_request_body_builder(self):
        request_body = StopChatMessageRequestBody.builder().user("user_123").build()

        assert request_body.user == "user_123"

    def test_response_inheritance(self):
        response = StopChatMessageResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "result")


class TestGetSuggestedQuestionsModels:
    def test_request_builder(self):
        request = GetSuggestedQuestionsRequest.builder().message_id("msg_123").user("test_user").build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/messages/:message_id/suggested"
        assert request.message_id == "msg_123"
        assert request.paths["message_id"] == "msg_123"

    def test_request_query_parameters(self):
        request = GetSuggestedQuestionsRequest.builder().message_id("msg_123").user("user_456").build()

        # Check that query parameter was added
        assert ("user", "user_456") in request.queries
        # Verify the query parameter is correctly stored
        user_queries = [q for q in request.queries if q[0] == "user"]
        assert len(user_queries) == 1
        assert user_queries[0][1] == "user_456"

    def test_response_inheritance(self):
        response = GetSuggestedQuestionsResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "result")
        assert hasattr(response, "data")

    def test_response_data_access(self):
        response = GetSuggestedQuestionsResponse(
            result="success", data=["What is AI?", "How does machine learning work?"]
        )
        assert response.result == "success"
        assert response.data == ["What is AI?", "How does machine learning work?"]
