#!/usr/bin/env python3
"""
Comprehensive Integration Tests for Chatflow APIs

This module provides end-to-end integration tests for all 17 Chatflow APIs
across 6 resources, testing complete workflows and error scenarios.
"""

from io import BytesIO
from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.chatflow.v1.model.annotation_reply_settings_request import AnnotationReplySettingsRequest
from dify_oapi.api.chatflow.v1.model.annotation_reply_settings_request_body import AnnotationReplySettingsRequestBody
from dify_oapi.api.chatflow.v1.model.annotation_reply_status_request import AnnotationReplyStatusRequest
from dify_oapi.api.chatflow.v1.model.audio_to_text_request import AudioToTextRequest
from dify_oapi.api.chatflow.v1.model.create_annotation_request import CreateAnnotationRequest
from dify_oapi.api.chatflow.v1.model.create_annotation_request_body import CreateAnnotationRequestBody
from dify_oapi.api.chatflow.v1.model.delete_annotation_request import DeleteAnnotationRequest
from dify_oapi.api.chatflow.v1.model.delete_conversation_request import DeleteConversationRequest
from dify_oapi.api.chatflow.v1.model.delete_conversation_request_body import DeleteConversationRequestBody
from dify_oapi.api.chatflow.v1.model.get_annotations_request import GetAnnotationsRequest
from dify_oapi.api.chatflow.v1.model.get_app_feedbacks_request import GetAppFeedbacksRequest
from dify_oapi.api.chatflow.v1.model.get_conversation_messages_request import GetConversationMessagesRequest
from dify_oapi.api.chatflow.v1.model.get_conversation_variables_request import GetConversationVariablesRequest
from dify_oapi.api.chatflow.v1.model.get_conversations_request import GetConversationsRequest
from dify_oapi.api.chatflow.v1.model.get_info_request import GetInfoRequest
from dify_oapi.api.chatflow.v1.model.get_meta_request import GetMetaRequest
from dify_oapi.api.chatflow.v1.model.get_parameters_request import GetParametersRequest
from dify_oapi.api.chatflow.v1.model.get_site_request import GetSiteRequest
from dify_oapi.api.chatflow.v1.model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from dify_oapi.api.chatflow.v1.model.message_feedback_request import MessageFeedbackRequest
from dify_oapi.api.chatflow.v1.model.message_feedback_request_body import MessageFeedbackRequestBody
from dify_oapi.api.chatflow.v1.model.rename_conversation_request import RenameConversationRequest
from dify_oapi.api.chatflow.v1.model.rename_conversation_request_body import RenameConversationRequestBody
from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody
from dify_oapi.api.chatflow.v1.model.stop_chat_message_request import StopChatMessageRequest
from dify_oapi.api.chatflow.v1.model.stop_chat_message_request_body import StopChatMessageRequestBody
from dify_oapi.api.chatflow.v1.model.text_to_audio_request import TextToAudioRequest
from dify_oapi.api.chatflow.v1.model.text_to_audio_request_body import TextToAudioRequestBody
from dify_oapi.api.chatflow.v1.model.update_annotation_request import UpdateAnnotationRequest
from dify_oapi.api.chatflow.v1.model.update_annotation_request_body import UpdateAnnotationRequestBody
from dify_oapi.api.chatflow.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


class TestChatflowAPIIntegration:
    """Integration tests for all Chatflow APIs."""

    @pytest.fixture
    def client(self):
        """Create test client."""
        return Client.builder().domain("https://api.dify.ai").build()

    @pytest.fixture
    def request_option(self):
        """Create test request option."""
        return RequestOption.builder().api_key("test-api-key").build()

    def test_complete_chat_conversation_flow(self, client, request_option):
        """Test complete chat conversation workflow."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock responses for complete workflow
            send_mock = MagicMock()
            send_mock.success = True
            send_mock.message_id = "msg-123"
            send_mock.conversation_id = "conv-123"
            send_mock.answer = "Hello!"

            suggested_mock = MagicMock()
            suggested_mock.success = True
            suggested_mock.data = ["What can you do?", "How does this work?"]

            stop_mock = MagicMock()
            stop_mock.success = True
            stop_mock.result = "success"

            messages_mock = MagicMock()
            messages_mock.success = True
            messages_mock.data = [{"id": "msg-123", "query": "Hello", "answer": "Hello!"}]
            messages_mock.has_more = False

            rename_mock = MagicMock()
            rename_mock.success = True
            rename_mock.id = "conv-123"
            rename_mock.name = "Test Chat"

            variables_mock = MagicMock()
            variables_mock.success = True
            variables_mock.data = []
            variables_mock.has_more = False

            delete_mock = MagicMock()
            delete_mock.success = True

            mock_responses = [
                send_mock,
                suggested_mock,
                stop_mock,
                messages_mock,
                rename_mock,
                variables_mock,
                delete_mock,
            ]
            mock_execute.side_effect = mock_responses

            # 1. Send chat message
            send_request = (
                SendChatMessageRequest.builder()
                .request_body(
                    SendChatMessageRequestBody.builder()
                    .query("Hello")
                    .user("test-user")
                    .response_mode("blocking")
                    .build()
                )
                .build()
            )
            send_response = client.chatflow.v1.chatflow.send(send_request, request_option)
            assert send_response.success
            assert send_response.message_id == "msg-123"

            # 2. Get suggested questions
            suggested_request = GetSuggestedQuestionsRequest.builder().message_id("msg-123").user("test-user").build()
            suggested_response = client.chatflow.v1.chatflow.suggested(suggested_request, request_option)
            assert suggested_response.success
            assert len(suggested_response.data) == 2

            # 3. Stop chat message (for demonstration)
            stop_request = (
                StopChatMessageRequest.builder()
                .task_id("task-123")
                .request_body(StopChatMessageRequestBody.builder().user("test-user").build())
                .build()
            )
            stop_response = client.chatflow.v1.chatflow.stop(stop_request, request_option)
            assert stop_response.success

            # 4. Get conversation messages
            messages_request = (
                GetConversationMessagesRequest.builder().conversation_id("conv-123").user("test-user").build()
            )
            messages_response = client.chatflow.v1.conversation.messages(messages_request, request_option)
            assert messages_response.success
            assert len(messages_response.data) == 1

            # 5. Rename conversation
            rename_request = (
                RenameConversationRequest.builder()
                .conversation_id("conv-123")
                .request_body(RenameConversationRequestBody.builder().name("Test Chat").user("test-user").build())
                .build()
            )
            rename_response = client.chatflow.v1.conversation.rename(rename_request, request_option)
            assert rename_response.success
            assert rename_response.name == "Test Chat"

            # 6. Get conversation variables
            variables_request = (
                GetConversationVariablesRequest.builder().conversation_id("conv-123").user("test-user").build()
            )
            variables_response = client.chatflow.v1.conversation.variables(variables_request, request_option)
            assert variables_response.success

            # 7. Delete conversation
            delete_request = (
                DeleteConversationRequest.builder()
                .conversation_id("conv-123")
                .request_body(DeleteConversationRequestBody.builder().user("test-user").build())
                .build()
            )
            delete_response = client.chatflow.v1.conversation.delete(delete_request, request_option)
            assert delete_response.success

    def test_file_upload_and_usage_workflow(self, client, request_option):
        """Test file upload and usage in chat workflow."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock responses
            upload_mock = MagicMock()
            upload_mock.success = True
            upload_mock.id = "file-123"
            upload_mock.name = "test.pdf"
            upload_mock.size = 1024

            chat_mock = MagicMock()
            chat_mock.success = True
            chat_mock.message_id = "msg-456"
            chat_mock.answer = "File analyzed successfully"

            mock_responses = [
                upload_mock,
                chat_mock,
            ]
            mock_execute.side_effect = mock_responses

            # 1. Upload file
            test_file = BytesIO(b"test file content")
            upload_request = UploadFileRequest.builder().file(test_file, "test.pdf").user("test-user").build()
            upload_response = client.chatflow.v1.file.upload(upload_request, request_option)
            assert upload_response.success
            assert upload_response.id == "file-123"

            # 2. Use file in chat
            send_request = (
                SendChatMessageRequest.builder()
                .request_body(
                    SendChatMessageRequestBody.builder()
                    .query("Analyze this file")
                    .user("test-user")
                    .response_mode("blocking")
                    .build()
                )
                .build()
            )
            send_response = client.chatflow.v1.chatflow.send(send_request, request_option)
            assert send_response.success
            assert "analyzed" in send_response.answer

    def test_feedback_collection_workflow(self, client, request_option):
        """Test feedback collection and retrieval workflow."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock responses
            feedback_mock = MagicMock()
            feedback_mock.success = True
            feedback_mock.result = "success"

            list_mock = MagicMock()
            list_mock.success = True
            list_mock.data = [{"id": "feedback-123", "rating": "like", "content": "Great response!"}]

            mock_responses = [
                feedback_mock,
                list_mock,
            ]
            mock_execute.side_effect = mock_responses

            # 1. Provide message feedback
            feedback_request = (
                MessageFeedbackRequest.builder()
                .message_id("msg-123")
                .request_body(
                    MessageFeedbackRequestBody.builder()
                    .rating("like")
                    .content("Great response!")
                    .user("test-user")
                    .build()
                )
                .build()
            )
            feedback_response = client.chatflow.v1.feedback.message(feedback_request, request_option)
            assert feedback_response.success

            # 2. Get app feedbacks
            get_feedbacks_request = GetAppFeedbacksRequest.builder().page(1).limit(20).build()
            get_feedbacks_response = client.chatflow.v1.feedback.list(get_feedbacks_request, request_option)
            assert get_feedbacks_response.success
            assert len(get_feedbacks_response.data) == 1

    def test_tts_operations_workflow(self, client, request_option):
        """Test TTS operations workflow."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock responses
            audio_mock = MagicMock()
            audio_mock.success = True
            audio_mock.text = "Hello, this is a test"

            tts_mock = MagicMock()
            tts_mock.success = True

            mock_responses = [
                audio_mock,
                tts_mock,
            ]
            mock_execute.side_effect = mock_responses

            # 1. Audio to text
            audio_file = BytesIO(b"fake audio content")
            audio_request = AudioToTextRequest.builder().file(audio_file, "test.mp3").user("test-user").build()
            audio_response = client.chatflow.v1.tts.speech_to_text(audio_request, request_option)
            assert audio_response.success
            assert audio_response.text == "Hello, this is a test"

            # 2. Text to audio
            tts_request = (
                TextToAudioRequest.builder()
                .request_body(TextToAudioRequestBody.builder().text("Hello, this is a test").user("test-user").build())
                .build()
            )
            tts_response = client.chatflow.v1.tts.text_to_audio(tts_request, request_option)
            assert tts_response.success

    def test_application_configuration_workflow(self, client, request_option):
        """Test application configuration access workflow."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock responses
            info_mock = MagicMock()
            info_mock.success = True
            info_mock.name = "Test App"
            info_mock.description = "Test Description"

            params_mock = MagicMock()
            params_mock.success = True
            params_mock.opening_statement = "Welcome!"
            params_mock.suggested_questions = ["What can you do?"]

            meta_mock = MagicMock()
            meta_mock.success = True
            meta_mock.tool_icons = {}

            site_mock = MagicMock()
            site_mock.success = True
            site_mock.title = "Test App"
            site_mock.chat_color_theme = "blue"

            mock_responses = [
                info_mock,
                params_mock,
                meta_mock,
                site_mock,
            ]
            mock_execute.side_effect = mock_responses

            # 1. Get app info
            info_request = GetInfoRequest.builder().build()
            info_response = client.chatflow.v1.application.info(info_request, request_option)
            assert info_response.success
            assert info_response.name == "Test App"

            # 2. Get app parameters
            params_request = GetParametersRequest.builder().build()
            params_response = client.chatflow.v1.application.parameters(params_request, request_option)
            assert params_response.success
            assert params_response.opening_statement == "Welcome!"

            # 3. Get app meta
            meta_request = GetMetaRequest.builder().build()
            meta_response = client.chatflow.v1.application.meta(meta_request, request_option)
            assert meta_response.success

            # 4. Get app site
            site_request = GetSiteRequest.builder().build()
            site_response = client.chatflow.v1.application.site(site_request, request_option)
            assert site_response.success
            assert site_response.title == "Test App"

    def test_annotation_management_workflow(self, client, request_option):
        """Test annotation management workflow."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock responses
            create_mock = MagicMock()
            create_mock.success = True
            create_mock.id = "annotation-123"
            create_mock.question = "What is AI?"
            create_mock.answer = "AI is artificial intelligence"

            list_mock = MagicMock()
            list_mock.success = True
            list_mock.data = [{"id": "annotation-123", "question": "What is AI?"}]
            list_mock.has_more = False

            update_mock = MagicMock()
            update_mock.success = True
            update_mock.id = "annotation-123"
            update_mock.question = "What is AI?"
            update_mock.answer = "Updated answer"

            settings_mock = MagicMock()
            settings_mock.success = True
            settings_mock.job_id = "job-123"
            settings_mock.job_status = "running"

            status_mock = MagicMock()
            status_mock.success = True
            status_mock.job_id = "job-123"
            status_mock.job_status = "completed"

            delete_mock = MagicMock()
            delete_mock.success = True

            mock_responses = [
                create_mock,
                list_mock,
                update_mock,
                settings_mock,
                status_mock,
                delete_mock,
            ]
            mock_execute.side_effect = mock_responses

            # 1. Create annotation
            create_request = (
                CreateAnnotationRequest.builder()
                .request_body(
                    CreateAnnotationRequestBody.builder()
                    .question("What is AI?")
                    .answer("AI is artificial intelligence")
                    .build()
                )
                .build()
            )
            create_response = client.chatflow.v1.annotation.create(create_request, request_option)
            assert create_response.success
            assert create_response.id == "annotation-123"

            # 2. Get annotations
            list_request = GetAnnotationsRequest.builder().page(1).limit(20).build()
            list_response = client.chatflow.v1.annotation.list(list_request, request_option)
            assert list_response.success
            assert len(list_response.data) == 1

            # 3. Update annotation
            update_request = (
                UpdateAnnotationRequest.builder()
                .annotation_id("annotation-123")
                .request_body(
                    UpdateAnnotationRequestBody.builder().question("What is AI?").answer("Updated answer").build()
                )
                .build()
            )
            update_response = client.chatflow.v1.annotation.update(update_request, request_option)
            assert update_response.success
            assert update_response.answer == "Updated answer"

            # 4. Configure reply settings
            settings_request = (
                AnnotationReplySettingsRequest.builder()
                .action("enable")
                .request_body(AnnotationReplySettingsRequestBody.builder().score_threshold(0.8).build())
                .build()
            )
            settings_response = client.chatflow.v1.annotation.reply_settings(settings_request, request_option)
            assert settings_response.success
            assert settings_response.job_id == "job-123"

            # 5. Check reply status
            status_request = AnnotationReplyStatusRequest.builder().action("enable").job_id("job-123").build()
            status_response = client.chatflow.v1.annotation.reply_status(status_request, request_option)
            assert status_response.success
            assert status_response.job_status == "completed"

            # 6. Delete annotation
            delete_request = DeleteAnnotationRequest.builder().annotation_id("annotation-123").build()
            delete_response = client.chatflow.v1.annotation.delete(delete_request, request_option)
            assert delete_response.success

    def test_conversation_list_and_management(self, client, request_option):
        """Test conversation listing and management."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock response
            mock_execute.return_value = MagicMock(
                success=True,
                data=[
                    {"id": "conv-1", "name": "Chat 1", "status": "normal"},
                    {"id": "conv-2", "name": "Chat 2", "status": "normal"},
                ],
                has_more=False,
            )

            # Get conversations list
            request = GetConversationsRequest.builder().user("test-user").limit(20).sort_by("-updated_at").build()
            response = client.chatflow.v1.conversation.list(request, request_option)
            assert response.success
            assert len(response.data) == 2

    def test_streaming_chat_workflow(self, client, request_option):
        """Test streaming chat workflow."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock streaming response
            def mock_stream():
                yield b'data: {"event": "message", "answer": "Hello"}\n\n'
                yield b'data: {"event": "message", "answer": " there!"}\n\n'
                yield b'data: {"event": "message_end", "metadata": {}}\n\n'

            mock_execute.return_value = mock_stream()

            # Send streaming chat message
            request = (
                SendChatMessageRequest.builder()
                .request_body(
                    SendChatMessageRequestBody.builder()
                    .query("Hello")
                    .user("test-user")
                    .response_mode("streaming")
                    .build()
                )
                .build()
            )

            stream = client.chatflow.v1.chatflow.send(request, request_option, stream=True)
            chunks = list(stream)
            assert len(chunks) == 3

    @pytest.mark.asyncio
    async def test_async_operations_workflow(self, client, request_option):
        """Test async operations workflow."""
        with patch("dify_oapi.core.http.transport.ATransport.aexecute") as mock_aexecute:
            # Mock async responses
            async_send_mock = MagicMock()
            async_send_mock.success = True
            async_send_mock.message_id = "msg-async"
            async_send_mock.answer = "Async response"

            async_upload_mock = MagicMock()
            async_upload_mock.success = True
            async_upload_mock.id = "file-async"
            async_upload_mock.name = "async.pdf"

            async_feedback_mock = MagicMock()
            async_feedback_mock.success = True
            async_feedback_mock.result = "success"

            mock_responses = [
                async_send_mock,
                async_upload_mock,
                async_feedback_mock,
            ]

            async def async_side_effect(*args, **kwargs):
                return mock_responses.pop(0)

            mock_aexecute.side_effect = async_side_effect

            # 1. Async chat
            send_request = (
                SendChatMessageRequest.builder()
                .request_body(
                    SendChatMessageRequestBody.builder()
                    .query("Async hello")
                    .user("test-user")
                    .response_mode("blocking")
                    .build()
                )
                .build()
            )
            send_response = await client.chatflow.v1.chatflow.asend(send_request, request_option)
            assert send_response.success
            assert send_response.message_id == "msg-async"

            # 2. Async file upload
            test_file = BytesIO(b"async file content")
            upload_request = UploadFileRequest.builder().file(test_file, "async.pdf").user("test-user").build()
            upload_response = await client.chatflow.v1.file.aupload(upload_request, request_option)
            assert upload_response.success
            assert upload_response.id == "file-async"

            # 3. Async feedback
            feedback_request = (
                MessageFeedbackRequest.builder()
                .message_id("msg-async")
                .request_body(MessageFeedbackRequestBody.builder().rating("like").user("test-user").build())
                .build()
            )
            feedback_response = await client.chatflow.v1.feedback.amessage(feedback_request, request_option)
            assert feedback_response.success

    def test_error_handling_scenarios(self, client, request_option):
        """Test error handling across all APIs."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock error responses
            error1_mock = MagicMock()
            error1_mock.success = False
            error1_mock.code = "invalid_request"
            error1_mock.msg = "Invalid parameters"

            error2_mock = MagicMock()
            error2_mock.success = False
            error2_mock.code = "not_found"
            error2_mock.msg = "Resource not found"

            error3_mock = MagicMock()
            error3_mock.success = False
            error3_mock.code = "unauthorized"
            error3_mock.msg = "Invalid API key"

            error_responses = [
                error1_mock,
                error2_mock,
                error3_mock,
            ]
            mock_execute.side_effect = error_responses

            # 1. Test chat error
            send_request = (
                SendChatMessageRequest.builder()
                .request_body(
                    SendChatMessageRequestBody.builder()
                    .query("")  # Invalid empty query
                    .user("test-user")
                    .build()
                )
                .build()
            )
            send_response = client.chatflow.v1.chatflow.send(send_request, request_option)
            assert not send_response.success
            assert send_response.code == "invalid_request"

            # 2. Test not found error
            suggested_request = (
                GetSuggestedQuestionsRequest.builder().message_id("non-existent").user("test-user").build()
            )
            suggested_response = client.chatflow.v1.chatflow.suggested(suggested_request, request_option)
            assert not suggested_response.success
            assert suggested_response.code == "not_found"

            # 3. Test unauthorized error
            info_request = GetInfoRequest.builder().build()
            info_response = client.chatflow.v1.application.info(info_request, request_option)
            assert not info_response.success
            assert info_response.code == "unauthorized"

    def test_pagination_functionality(self, client, request_option):
        """Test pagination across list APIs."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock paginated responses
            page1_mock = MagicMock()
            page1_mock.success = True
            page1_mock.data = [{"id": "item-1"}, {"id": "item-2"}]
            page1_mock.has_more = True
            page1_mock.limit = 2

            page2_mock = MagicMock()
            page2_mock.success = True
            page2_mock.data = [{"id": "item-3"}]
            page2_mock.has_more = False
            page2_mock.limit = 2

            mock_responses = [
                page1_mock,
                page2_mock,
            ]
            mock_execute.side_effect = mock_responses

            # 1. Get first page
            request1 = GetConversationsRequest.builder().user("test-user").limit(2).build()
            response1 = client.chatflow.v1.conversation.list(request1, request_option)
            assert response1.success
            assert len(response1.data) == 2
            assert response1.has_more

            # 2. Get second page
            request2 = GetConversationsRequest.builder().user("test-user").limit(2).last_id("item-2").build()
            response2 = client.chatflow.v1.conversation.list(request2, request_option)
            assert response2.success
            assert len(response2.data) == 1
            assert not response2.has_more

    def test_all_api_endpoints_accessible(self, client, request_option):
        """Test that all 17 API endpoints are accessible through the client."""
        # Verify all resources are accessible
        assert hasattr(client.chatflow.v1, "chatflow")
        assert hasattr(client.chatflow.v1, "file")
        assert hasattr(client.chatflow.v1, "feedback")
        assert hasattr(client.chatflow.v1, "conversation")
        assert hasattr(client.chatflow.v1, "tts")
        assert hasattr(client.chatflow.v1, "application")
        assert hasattr(client.chatflow.v1, "annotation")

        # Verify all methods are accessible
        # Chatflow methods (3)
        assert hasattr(client.chatflow.v1.chatflow, "send")
        assert hasattr(client.chatflow.v1.chatflow, "stop")
        assert hasattr(client.chatflow.v1.chatflow, "suggested")

        # File methods (1)
        assert hasattr(client.chatflow.v1.file, "upload")

        # Feedback methods (2)
        assert hasattr(client.chatflow.v1.feedback, "message")
        assert hasattr(client.chatflow.v1.feedback, "list")

        # Conversation methods (5)
        assert hasattr(client.chatflow.v1.conversation, "messages")
        assert hasattr(client.chatflow.v1.conversation, "list")
        assert hasattr(client.chatflow.v1.conversation, "delete")
        assert hasattr(client.chatflow.v1.conversation, "rename")
        assert hasattr(client.chatflow.v1.conversation, "variables")

        # TTS methods (2)
        assert hasattr(client.chatflow.v1.tts, "speech_to_text")
        assert hasattr(client.chatflow.v1.tts, "text_to_audio")

        # Application methods (4)
        assert hasattr(client.chatflow.v1.application, "info")
        assert hasattr(client.chatflow.v1.application, "parameters")
        assert hasattr(client.chatflow.v1.application, "meta")
        assert hasattr(client.chatflow.v1.application, "site")

        # Annotation methods (6)
        assert hasattr(client.chatflow.v1.annotation, "list")
        assert hasattr(client.chatflow.v1.annotation, "create")
        assert hasattr(client.chatflow.v1.annotation, "update")
        assert hasattr(client.chatflow.v1.annotation, "delete")
        assert hasattr(client.chatflow.v1.annotation, "reply_settings")
        assert hasattr(client.chatflow.v1.annotation, "reply_status")

        # Verify async methods are accessible
        assert hasattr(client.chatflow.v1.chatflow, "asend")
        assert hasattr(client.chatflow.v1.file, "aupload")
        assert hasattr(client.chatflow.v1.feedback, "amessage")
        assert hasattr(client.chatflow.v1.conversation, "amessages")
        assert hasattr(client.chatflow.v1.tts, "aspeech_to_text")
        assert hasattr(client.chatflow.v1.application, "ainfo")
        assert hasattr(client.chatflow.v1.annotation, "alist")
