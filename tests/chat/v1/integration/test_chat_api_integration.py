"""
Comprehensive integration tests for Chat API to verify end-to-end functionality of all 22 APIs.

This module tests complete API flows and ensures all chat functionality works properly.
"""

from io import BytesIO
from unittest.mock import patch

import pytest

# Audio Processing API Models
from dify_oapi.api.chat.v1.model.audio_to_text_request import AudioToTextRequest
from dify_oapi.api.chat.v1.model.audio_to_text_response import AudioToTextResponse

# Public Models
from dify_oapi.api.chat.v1.model.chat_file import ChatFile

# Chat Messages API Models
from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.api.chat.v1.model.chat_response import ChatResponse
from dify_oapi.api.chat.v1.model.configure_annotation_reply_request import ConfigureAnnotationReplyRequest
from dify_oapi.api.chat.v1.model.configure_annotation_reply_request_body import ConfigureAnnotationReplyRequestBody
from dify_oapi.api.chat.v1.model.configure_annotation_reply_response import ConfigureAnnotationReplyResponse
from dify_oapi.api.chat.v1.model.create_annotation_request import CreateAnnotationRequest
from dify_oapi.api.chat.v1.model.create_annotation_request_body import CreateAnnotationRequestBody
from dify_oapi.api.chat.v1.model.create_annotation_response import CreateAnnotationResponse
from dify_oapi.api.chat.v1.model.delete_annotation_request import DeleteAnnotationRequest
from dify_oapi.api.chat.v1.model.delete_annotation_response import DeleteAnnotationResponse
from dify_oapi.api.chat.v1.model.delete_conversation_request import DeleteConversationRequest
from dify_oapi.api.chat.v1.model.delete_conversation_request_body import DeleteConversationRequestBody
from dify_oapi.api.chat.v1.model.delete_conversation_response import DeleteConversationResponse
from dify_oapi.api.chat.v1.model.get_annotation_reply_status_request import GetAnnotationReplyStatusRequest
from dify_oapi.api.chat.v1.model.get_annotation_reply_status_response import GetAnnotationReplyStatusResponse

# Application Information API Models
from dify_oapi.api.chat.v1.model.get_app_info_request import GetAppInfoRequest
from dify_oapi.api.chat.v1.model.get_app_info_response import GetAppInfoResponse
from dify_oapi.api.chat.v1.model.get_app_meta_request import GetAppMetaRequest
from dify_oapi.api.chat.v1.model.get_app_meta_response import GetAppMetaResponse
from dify_oapi.api.chat.v1.model.get_app_parameters_request import GetAppParametersRequest
from dify_oapi.api.chat.v1.model.get_app_parameters_response import GetAppParametersResponse
from dify_oapi.api.chat.v1.model.get_conversation_list_request import GetConversationListRequest
from dify_oapi.api.chat.v1.model.get_conversation_list_response import GetConversationListResponse
from dify_oapi.api.chat.v1.model.get_conversation_variables_request import GetConversationVariablesRequest
from dify_oapi.api.chat.v1.model.get_conversation_variables_response import GetConversationVariablesResponse
from dify_oapi.api.chat.v1.model.get_feedbacks_request import GetFeedbacksRequest
from dify_oapi.api.chat.v1.model.get_feedbacks_response import GetFeedbacksResponse
from dify_oapi.api.chat.v1.model.get_site_settings_request import GetSiteSettingsRequest
from dify_oapi.api.chat.v1.model.get_site_settings_response import GetSiteSettingsResponse
from dify_oapi.api.chat.v1.model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from dify_oapi.api.chat.v1.model.get_suggested_questions_response import GetSuggestedQuestionsResponse

# Annotation Management API Models
from dify_oapi.api.chat.v1.model.list_annotations_request import ListAnnotationsRequest
from dify_oapi.api.chat.v1.model.list_annotations_response import ListAnnotationsResponse

# Conversation Management API Models
from dify_oapi.api.chat.v1.model.message_history_request import MessageHistoryRequest
from dify_oapi.api.chat.v1.model.message_history_response import MessageHistoryResponse
from dify_oapi.api.chat.v1.model.rename_conversation_request import RenameConversationRequest
from dify_oapi.api.chat.v1.model.rename_conversation_request_body import RenameConversationRequestBody
from dify_oapi.api.chat.v1.model.rename_conversation_response import RenameConversationResponse
from dify_oapi.api.chat.v1.model.stop_chat_request import StopChatRequest
from dify_oapi.api.chat.v1.model.stop_chat_request_body import StopChatRequestBody
from dify_oapi.api.chat.v1.model.stop_chat_response import StopChatResponse

# Feedback Management API Models
from dify_oapi.api.chat.v1.model.submit_feedback_request import SubmitFeedbackRequest
from dify_oapi.api.chat.v1.model.submit_feedback_request_body import SubmitFeedbackRequestBody
from dify_oapi.api.chat.v1.model.submit_feedback_response import SubmitFeedbackResponse
from dify_oapi.api.chat.v1.model.text_to_audio_request import TextToAudioRequest
from dify_oapi.api.chat.v1.model.update_annotation_request import UpdateAnnotationRequest
from dify_oapi.api.chat.v1.model.update_annotation_request_body import UpdateAnnotationRequestBody
from dify_oapi.api.chat.v1.model.update_annotation_response import UpdateAnnotationResponse

# File Management API Models
from dify_oapi.api.chat.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.api.chat.v1.model.upload_file_response import UploadFileResponse
from dify_oapi.client import Client
from dify_oapi.core.http.async_transport import ATransport
from dify_oapi.core.http.transport import Transport
from dify_oapi.core.model.request_option import RequestOption


class TestChatAPIIntegration:
    """Test complete Chat API integration flows."""

    @pytest.fixture
    def client(self):
        """Create test client."""
        return Client.builder().domain("https://api.dify.ai").build()

    @pytest.fixture
    def request_option(self):
        """Create test request option."""
        return RequestOption.builder().api_key("test-api-key").build()

    def test_complete_chat_flow(self, client, request_option):
        """Test complete chat conversation flow."""
        with patch.object(Transport, "execute") as mock_execute:
            # 1. Send initial chat message
            chat_body = (
                ChatRequestBody.builder()
                .query("Hello, how are you?")
                .user("test-user")
                .response_mode("blocking")
                .inputs({})
                .auto_generate_name(True)
                .build()
            )
            chat_request = ChatRequest.builder().request_body(chat_body).build()

            mock_execute.return_value = ChatResponse(
                message_id="msg-123", conversation_id="conv-123", answer="Hello! I'm doing well, thank you for asking."
            )

            response = client.chat.v1.chat.chat(chat_request, request_option, False)
            assert response.message_id == "msg-123"
            assert response.conversation_id == "conv-123"
            assert "Hello!" in response.answer

            # 2. Get suggested questions
            suggested_request = GetSuggestedQuestionsRequest.builder().message_id("msg-123").user("test-user").build()

            mock_execute.return_value = GetSuggestedQuestionsResponse(
                result="success", data=["What can you help me with?", "Tell me about yourself", "How do you work?"]
            )

            suggested_response = client.chat.v1.chat.suggested(suggested_request, request_option)
            assert suggested_response.result == "success"
            assert len(suggested_response.data) == 3

            # 3. Continue conversation
            continue_body = (
                ChatRequestBody.builder()
                .query("What can you help me with?")
                .user("test-user")
                .response_mode("blocking")
                .conversation_id("conv-123")
                .build()
            )
            continue_request = ChatRequest.builder().request_body(continue_body).build()

            mock_execute.return_value = ChatResponse(
                message_id="msg-124",
                conversation_id="conv-123",
                answer="I can help you with various tasks including answering questions, writing, and analysis.",
            )

            continue_response = client.chat.v1.chat.chat(continue_request, request_option, False)
            assert continue_response.message_id == "msg-124"
            assert continue_response.conversation_id == "conv-123"

    def test_streaming_chat_flow(self, client, request_option):
        """Test streaming chat flow."""
        with patch.object(Transport, "execute") as mock_execute:
            chat_body = (
                ChatRequestBody.builder().query("Tell me a story").user("test-user").response_mode("streaming").build()
            )
            chat_request = ChatRequest.builder().request_body(chat_body).build()

            # Mock streaming response
            mock_execute.return_value = iter(
                [
                    b'data: {"event": "message", "answer": "Once upon a time"}\n\n',
                    b'data: {"event": "message", "answer": " there was a"}\n\n',
                    b'data: {"event": "message_end", "metadata": {}}\n\n',
                ]
            )

            response = client.chat.v1.chat.chat(chat_request, request_option, True)
            chunks = list(response)
            assert len(chunks) == 3
            assert b"Once upon a time" in chunks[0]

    def test_stop_chat_generation(self, client, request_option):
        """Test stop chat generation."""
        with patch.object(Transport, "execute") as mock_execute:
            stop_body = StopChatRequestBody.builder().user("test-user").build()
            stop_request = StopChatRequest.builder().task_id("task-123").request_body(stop_body).build()

            mock_execute.return_value = StopChatResponse(result="success")

            response = client.chat.v1.chat.stop(stop_request, request_option)
            assert response.result == "success"

    def test_file_upload_and_chat_flow(self, client, request_option):
        """Test file upload followed by chat with file."""
        with patch.object(Transport, "execute") as mock_execute:
            # 1. Upload file
            file_data = BytesIO(b"test image content")
            upload_request = UploadFileRequest.builder().file(file_data, "test.jpg").user("test-user").build()

            mock_execute.return_value = UploadFileResponse(
                id="file-123", name="test.jpg", size=1024, extension="jpg", mime_type="image/jpeg"
            )

            upload_response = client.chat.v1.file.upload(upload_request, request_option)
            assert upload_response.id == "file-123"
            assert upload_response.name == "test.jpg"

            # 2. Use uploaded file in chat
            chat_file = (
                ChatFile.builder().type("image").transfer_method("local_file").upload_file_id("file-123").build()
            )

            chat_body = (
                ChatRequestBody.builder()
                .query("What's in this image?")
                .user("test-user")
                .response_mode("blocking")
                .files([chat_file])
                .build()
            )
            chat_request = ChatRequest.builder().request_body(chat_body).build()

            mock_execute.return_value = ChatResponse(
                message_id="msg-125", answer="I can see an image with test content."
            )

            chat_response = client.chat.v1.chat.chat(chat_request, request_option, False)
            assert "image" in chat_response.answer

    def test_feedback_management_flow(self, client, request_option):
        """Test complete feedback management flow."""
        with patch.object(Transport, "execute") as mock_execute:
            # 1. Submit positive feedback
            feedback_body = (
                SubmitFeedbackRequestBody.builder().rating("like").user("test-user").content("Great response!").build()
            )
            feedback_request = SubmitFeedbackRequest.builder().message_id("msg-123").request_body(feedback_body).build()

            mock_execute.return_value = SubmitFeedbackResponse(result="success")

            feedback_response = client.chat.v1.feedback.submit(feedback_request, request_option)
            assert feedback_response.result == "success"

            # 2. Get feedback list
            get_feedbacks_request = GetFeedbacksRequest.builder().page(1).limit(20).build()

            mock_execute.return_value = GetFeedbacksResponse(
                data=[{"id": "feedback-123", "rating": "like", "content": "Great response!", "message_id": "msg-123"}]
            )

            feedbacks_response = client.chat.v1.feedback.list(get_feedbacks_request, request_option)
            assert len(feedbacks_response.data) == 1
            assert feedbacks_response.data[0]["rating"] == "like"

    def test_conversation_management_flow(self, client, request_option):
        """Test complete conversation management flow."""
        with patch.object(Transport, "execute") as mock_execute:
            # 1. Get conversations list
            conversations_request = (
                GetConversationListRequest.builder().user("test-user").limit(20).sort_by("-updated_at").build()
            )

            mock_execute.return_value = GetConversationListResponse(
                data=[{"id": "conv-123", "name": "Test Conversation", "status": "normal"}], has_more=False, limit=20
            )

            conversations_response = client.chat.v1.conversation.list(conversations_request, request_option)
            assert len(conversations_response.data) == 1
            assert conversations_response.data[0]["id"] == "conv-123"

            # 2. Get message history
            history_request = (
                MessageHistoryRequest.builder().conversation_id("conv-123").user("test-user").limit(20).build()
            )

            mock_execute.return_value = MessageHistoryResponse(
                data=[{"id": "msg-123", "query": "Hello", "answer": "Hi there!", "conversation_id": "conv-123"}],
                has_more=False,
                limit=20,
            )

            history_response = client.chat.v1.conversation.history(history_request, request_option)
            assert len(history_response.data) == 1
            assert history_response.data[0]["id"] == "msg-123"

            # 3. Rename conversation
            rename_body = (
                RenameConversationRequestBody.builder().name("Updated Conversation Name").user("test-user").build()
            )
            rename_request = (
                RenameConversationRequest.builder().conversation_id("conv-123").request_body(rename_body).build()
            )

            mock_execute.return_value = RenameConversationResponse(id="conv-123", name="Updated Conversation Name")

            rename_response = client.chat.v1.conversation.rename(rename_request, request_option)
            assert rename_response.name == "Updated Conversation Name"

            # 4. Get conversation variables
            variables_request = (
                GetConversationVariablesRequest.builder()
                .conversation_id("conv-123")
                .user("test-user")
                .limit(20)
                .build()
            )

            mock_execute.return_value = GetConversationVariablesResponse(
                data=[{"id": "var-123", "name": "user_name", "value": "John", "value_type": "string"}],
                has_more=False,
                limit=20,
            )

            variables_response = client.chat.v1.conversation.variables(variables_request, request_option)
            assert len(variables_response.data) == 1
            assert variables_response.data[0]["name"] == "user_name"

            # 5. Delete conversation
            delete_body = DeleteConversationRequestBody.builder().user("test-user").build()
            delete_request = (
                DeleteConversationRequest.builder().conversation_id("conv-123").request_body(delete_body).build()
            )

            mock_execute.return_value = DeleteConversationResponse()

            delete_response = client.chat.v1.conversation.delete(delete_request, request_option)
            assert delete_response is not None

    def test_audio_processing_flow(self, client, request_option):
        """Test complete audio processing flow."""
        with patch.object(Transport, "execute") as mock_execute:
            # 1. Audio to text
            audio_data = BytesIO(b"mock audio content")
            audio_request = AudioToTextRequest.builder().file(audio_data, "test.mp3").user("test-user").build()

            mock_execute.return_value = AudioToTextResponse(text="Hello, this is a test audio message.")

            audio_response = client.chat.v1.audio.to_text(audio_request, request_option)
            assert "Hello" in audio_response.text

            # 2. Text to audio
            text_request = TextToAudioRequest.builder().text("Hello, this is a test message.").user("test-user").build()

            mock_execute.return_value = b"mock audio binary data"

            text_response = client.chat.v1.audio.to_audio(text_request, request_option)
            assert isinstance(text_response, bytes)
            assert b"mock audio" in text_response

    def test_application_information_flow(self, client, request_option):
        """Test complete application information flow."""
        with patch.object(Transport, "execute") as mock_execute:
            # 1. Get app info
            info_request = GetAppInfoRequest.builder().build()

            mock_execute.return_value = GetAppInfoResponse(
                name="Test Chat App", description="A test chat application", tags=["ai", "chat"]
            )

            info_response = client.chat.v1.app.info(info_request, request_option)
            assert info_response.name == "Test Chat App"
            assert "ai" in info_response.tags

            # 2. Get app parameters
            params_request = GetAppParametersRequest.builder().user("test-user").build()

            mock_execute.return_value = GetAppParametersResponse(
                opening_statement="Welcome to the chat!",
                suggested_questions=["How can I help?", "What can you do?"],
                speech_to_text={"enabled": True},
                text_to_speech={"enabled": True, "voice": "default"},
            )

            params_response = client.chat.v1.app.parameters(params_request, request_option)
            assert params_response.opening_statement == "Welcome to the chat!"
            assert len(params_response.suggested_questions) == 2

            # 3. Get app meta
            meta_request = GetAppMetaRequest.builder().build()

            mock_execute.return_value = GetAppMetaResponse(
                tool_icons={"search": {"background": "#000", "content": "🔍"}}
            )

            meta_response = client.chat.v1.app.meta(meta_request, request_option)
            assert "search" in meta_response.tool_icons

            # 4. Get site settings
            site_request = GetSiteSettingsRequest.builder().build()

            mock_execute.return_value = GetSiteSettingsResponse(
                title="Test Chat Site", chat_color_theme="blue", icon_type="emoji", icon="💬"
            )

            site_response = client.chat.v1.app.site(site_request, request_option)
            assert site_response.title == "Test Chat Site"
            assert site_response.icon == "💬"

    def test_annotation_management_flow(self, client, request_option):
        """Test complete annotation management flow."""
        with patch.object(Transport, "execute") as mock_execute:
            # 1. List annotations
            list_request = ListAnnotationsRequest.builder().page(1).limit(20).build()

            mock_execute.return_value = ListAnnotationsResponse(
                data=[
                    {
                        "id": "ann-123",
                        "question": "What is AI?",
                        "answer": "AI is artificial intelligence.",
                        "hit_count": 5,
                    }
                ],
                has_more=False,
                total=1,
                page=1,
                limit=20,
            )

            list_response = client.chat.v1.annotation.list(list_request, request_option)
            assert len(list_response.data) == 1
            assert list_response.data[0]["question"] == "What is AI?"

            # 2. Create annotation
            create_body = (
                CreateAnnotationRequestBody.builder()
                .question("What is machine learning?")
                .answer("Machine learning is a subset of AI.")
                .build()
            )
            create_request = CreateAnnotationRequest.builder().request_body(create_body).build()

            mock_execute.return_value = CreateAnnotationResponse(
                id="ann-124",
                question="What is machine learning?",
                answer="Machine learning is a subset of AI.",
                hit_count=0,
            )

            create_response = client.chat.v1.annotation.create(create_request, request_option)
            assert create_response.id == "ann-124"
            assert "machine learning" in create_response.question

            # 3. Update annotation
            update_body = (
                UpdateAnnotationRequestBody.builder()
                .question("What is machine learning?")
                .answer("Machine learning is a method of data analysis that automates analytical model building.")
                .build()
            )
            update_request = (
                UpdateAnnotationRequest.builder().annotation_id("ann-124").request_body(update_body).build()
            )

            mock_execute.return_value = UpdateAnnotationResponse(
                id="ann-124",
                question="What is machine learning?",
                answer="Machine learning is a method of data analysis that automates analytical model building.",
                hit_count=0,
            )

            update_response = client.chat.v1.annotation.update(update_request, request_option)
            assert "automates analytical" in update_response.answer

            # 4. Configure annotation reply
            config_body = (
                ConfigureAnnotationReplyRequestBody.builder()
                .score_threshold(0.8)
                .embedding_provider_name("openai")
                .embedding_model_name("text-embedding-ada-002")
                .build()
            )
            config_request = (
                ConfigureAnnotationReplyRequest.builder().action("enable").request_body(config_body).build()
            )

            mock_execute.return_value = ConfigureAnnotationReplyResponse(job_id="job-123", job_status="running")

            config_response = client.chat.v1.annotation.configure(config_request, request_option)
            assert config_response.job_id == "job-123"
            assert config_response.job_status == "running"

            # 5. Get annotation reply status
            status_request = GetAnnotationReplyStatusRequest.builder().action("enable").job_id("job-123").build()

            mock_execute.return_value = GetAnnotationReplyStatusResponse(
                job_id="job-123", job_status="completed", error_msg=None
            )

            status_response = client.chat.v1.annotation.status(status_request, request_option)
            assert status_response.job_status == "completed"
            assert status_response.error_msg is None

            # 6. Delete annotation
            delete_request = DeleteAnnotationRequest.builder().annotation_id("ann-124").build()

            mock_execute.return_value = DeleteAnnotationResponse()

            delete_response = client.chat.v1.annotation.delete(delete_request, request_option)
            assert delete_response is not None

    @pytest.mark.asyncio
    async def test_async_chat_flow(self, client, request_option):
        """Test async chat operations."""
        with patch.object(ATransport, "aexecute") as mock_aexecute:
            chat_body = (
                ChatRequestBody.builder().query("Hello async world").user("test-user").response_mode("blocking").build()
            )
            chat_request = ChatRequest.builder().request_body(chat_body).build()

            mock_aexecute.return_value = ChatResponse(message_id="msg-async-123", answer="Hello from async world!")

            response = await client.chat.v1.chat.achat(chat_request, request_option, False)
            assert response.message_id == "msg-async-123"
            assert "async world" in response.answer

    def test_error_handling_scenarios(self, client, request_option):
        """Test error handling across different APIs."""
        with patch.object(Transport, "execute") as mock_execute:
            # Test chat error
            chat_body = ChatRequestBody.builder().query("Test").user("test-user").build()
            chat_request = ChatRequest.builder().request_body(chat_body).build()

            mock_execute.side_effect = Exception("API Error: Invalid request")

            with pytest.raises(Exception) as exc_info:
                client.chat.v1.chat.chat(chat_request, request_option, False)
            assert "API Error" in str(exc_info.value)

    def test_all_resources_accessible(self, client):
        """Test that all 7 resources are accessible through client."""
        # Verify all resources exist
        assert hasattr(client.chat.v1, "chat")
        assert hasattr(client.chat.v1, "file")
        assert hasattr(client.chat.v1, "feedback")
        assert hasattr(client.chat.v1, "conversation")
        assert hasattr(client.chat.v1, "audio")
        assert hasattr(client.chat.v1, "app")
        assert hasattr(client.chat.v1, "annotation")

        # Verify resource methods exist
        assert hasattr(client.chat.v1.chat, "chat")
        assert hasattr(client.chat.v1.chat, "stop")
        assert hasattr(client.chat.v1.chat, "suggested")

        assert hasattr(client.chat.v1.file, "upload")

        assert hasattr(client.chat.v1.feedback, "submit")
        assert hasattr(client.chat.v1.feedback, "list")

        assert hasattr(client.chat.v1.conversation, "list")
        assert hasattr(client.chat.v1.conversation, "delete")
        assert hasattr(client.chat.v1.conversation, "rename")
        assert hasattr(client.chat.v1.conversation, "history")
        assert hasattr(client.chat.v1.conversation, "variables")

        assert hasattr(client.chat.v1.audio, "to_text")
        assert hasattr(client.chat.v1.audio, "to_audio")

        assert hasattr(client.chat.v1.app, "info")
        assert hasattr(client.chat.v1.app, "parameters")
        assert hasattr(client.chat.v1.app, "meta")
        assert hasattr(client.chat.v1.app, "site")

        assert hasattr(client.chat.v1.annotation, "list")
        assert hasattr(client.chat.v1.annotation, "create")
        assert hasattr(client.chat.v1.annotation, "update")
        assert hasattr(client.chat.v1.annotation, "delete")
        assert hasattr(client.chat.v1.annotation, "configure")
        assert hasattr(client.chat.v1.annotation, "status")

    def test_backward_compatibility(self, client):
        """Test backward compatibility with existing message resource."""
        # Verify deprecated message resource still exists
        assert hasattr(client.chat.v1, "message")

        # Verify deprecated methods still work
        assert hasattr(client.chat.v1.message, "suggested")
        assert hasattr(client.chat.v1.message, "history")
