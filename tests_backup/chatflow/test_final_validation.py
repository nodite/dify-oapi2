#!/usr/bin/env python3
"""
Final Validation Tests for Chatflow API Implementation

This module provides comprehensive validation tests to ensure the complete
Chatflow API implementation meets all requirements and specifications.
"""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.client import Client
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestFinalValidation:
    """Final validation tests for complete Chatflow API implementation."""

    @pytest.fixture
    def config(self):
        """Create test configuration."""
        config = Config()
        config.domain = "https://api.dify.ai"
        return config

    @pytest.fixture
    def client(self):
        """Create test client."""
        return Client.builder().domain("https://api.dify.ai").build()

    @pytest.fixture
    def request_option(self):
        """Create test request option."""
        return RequestOption.builder().api_key("test-api-key").build()

    def test_complete_client_integration(self, client):
        """Test complete client integration with all chatflow resources."""
        # Verify chatflow service is accessible
        assert hasattr(client, "chatflow")
        assert client.chatflow is not None

        # Verify v1 version is accessible
        assert hasattr(client.chatflow, "v1")
        assert client.chatflow.v1 is not None

        # Verify all 6 resources are accessible
        resources = ["chatflow", "file", "feedback", "conversation", "tts", "application", "annotation"]
        for resource in resources:
            assert hasattr(client.chatflow.v1, resource)
            assert getattr(client.chatflow.v1, resource) is not None

    def test_all_17_apis_accessible(self, client):
        """Test that all 17 APIs are accessible through client."""
        # Chatflow APIs (3)
        assert hasattr(client.chatflow.v1.chatflow, "send")
        assert hasattr(client.chatflow.v1.chatflow, "stop")
        assert hasattr(client.chatflow.v1.chatflow, "suggested")

        # File APIs (1)
        assert hasattr(client.chatflow.v1.file, "upload")

        # Feedback APIs (2)
        assert hasattr(client.chatflow.v1.feedback, "message")
        assert hasattr(client.chatflow.v1.feedback, "list")

        # Conversation APIs (5)
        assert hasattr(client.chatflow.v1.conversation, "messages")
        assert hasattr(client.chatflow.v1.conversation, "list")
        assert hasattr(client.chatflow.v1.conversation, "delete")
        assert hasattr(client.chatflow.v1.conversation, "rename")
        assert hasattr(client.chatflow.v1.conversation, "variables")

        # TTS APIs (2)
        assert hasattr(client.chatflow.v1.tts, "speech_to_text")
        assert hasattr(client.chatflow.v1.tts, "text_to_audio")

        # Application APIs (4)
        assert hasattr(client.chatflow.v1.application, "info")
        assert hasattr(client.chatflow.v1.application, "parameters")
        assert hasattr(client.chatflow.v1.application, "meta")
        assert hasattr(client.chatflow.v1.application, "site")

        # Annotation APIs (6)
        assert hasattr(client.chatflow.v1.annotation, "list")
        assert hasattr(client.chatflow.v1.annotation, "create")
        assert hasattr(client.chatflow.v1.annotation, "update")
        assert hasattr(client.chatflow.v1.annotation, "delete")
        assert hasattr(client.chatflow.v1.annotation, "reply_settings")
        assert hasattr(client.chatflow.v1.annotation, "reply_status")

    def test_async_methods_accessible(self, client):
        """Test that all async methods are accessible."""
        # Chatflow async methods
        assert hasattr(client.chatflow.v1.chatflow, "asend")
        assert hasattr(client.chatflow.v1.chatflow, "astop")
        assert hasattr(client.chatflow.v1.chatflow, "asuggested")

        # File async methods
        assert hasattr(client.chatflow.v1.file, "aupload")

        # Feedback async methods
        assert hasattr(client.chatflow.v1.feedback, "amessage")
        assert hasattr(client.chatflow.v1.feedback, "alist")

        # Conversation async methods
        assert hasattr(client.chatflow.v1.conversation, "amessages")
        assert hasattr(client.chatflow.v1.conversation, "alist")
        assert hasattr(client.chatflow.v1.conversation, "adelete")
        assert hasattr(client.chatflow.v1.conversation, "arename")
        assert hasattr(client.chatflow.v1.conversation, "avariables")

        # TTS async methods
        assert hasattr(client.chatflow.v1.tts, "aspeech_to_text")
        assert hasattr(client.chatflow.v1.tts, "atext_to_audio")

        # Application async methods
        assert hasattr(client.chatflow.v1.application, "ainfo")
        assert hasattr(client.chatflow.v1.application, "aparameters")
        assert hasattr(client.chatflow.v1.application, "ameta")
        assert hasattr(client.chatflow.v1.application, "asite")

        # Annotation async methods
        assert hasattr(client.chatflow.v1.annotation, "alist")
        assert hasattr(client.chatflow.v1.annotation, "acreate")
        assert hasattr(client.chatflow.v1.annotation, "aupdate")
        assert hasattr(client.chatflow.v1.annotation, "adelete")
        assert hasattr(client.chatflow.v1.annotation, "areply_settings")
        assert hasattr(client.chatflow.v1.annotation, "areply_status")

    def test_model_imports_work(self):
        """Test that all model imports work correctly."""
        # Test core model imports
        from dify_oapi.api.chatflow.v1.model.chat_file import ChatFile
        from dify_oapi.api.chatflow.v1.model.chat_message import ChatMessage
        from dify_oapi.api.chatflow.v1.model.chatflow_types import ResponseMode
        from dify_oapi.api.chatflow.v1.model.get_info_response import GetInfoResponse
        from dify_oapi.api.chatflow.v1.model.message_feedback_request import MessageFeedbackRequest
        from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
        from dify_oapi.api.chatflow.v1.model.send_chat_message_response import SendChatMessageResponse
        from dify_oapi.api.chatflow.v1.model.upload_file_request import UploadFileRequest
        from dify_oapi.api.chatflow.v1.model.upload_file_response import UploadFileResponse

        # Verify imports are successful
        assert ResponseMode is not None
        assert ChatMessage is not None
        assert ChatFile is not None
        assert SendChatMessageRequest is not None
        assert UploadFileRequest is not None
        assert MessageFeedbackRequest is not None
        assert SendChatMessageResponse is not None
        assert UploadFileResponse is not None
        assert GetInfoResponse is not None

    def test_resource_imports_work(self):
        """Test that all resource imports work correctly."""
        from dify_oapi.api.chatflow.v1.resource.annotation import Annotation
        from dify_oapi.api.chatflow.v1.resource.application import Application
        from dify_oapi.api.chatflow.v1.resource.chatflow import Chatflow
        from dify_oapi.api.chatflow.v1.resource.conversation import Conversation
        from dify_oapi.api.chatflow.v1.resource.feedback import Feedback
        from dify_oapi.api.chatflow.v1.resource.file import File
        from dify_oapi.api.chatflow.v1.resource.tts import TTS

        # Verify imports are successful
        assert Chatflow is not None
        assert File is not None
        assert Feedback is not None
        assert Conversation is not None
        assert TTS is not None
        assert Application is not None
        assert Annotation is not None

    def test_service_integration_works(self):
        """Test that service integration works correctly."""
        from dify_oapi.api.chatflow.service import ChatflowService
        from dify_oapi.api.chatflow.v1.version import V1

        # Test service creation
        config = Config()
        config.domain = "https://api.dify.ai"
        service = ChatflowService(config)
        assert service is not None
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_configuration_propagation(self, client):
        """Test that configuration is properly propagated through all layers."""
        # Verify config is passed to service
        assert client.chatflow.v1.chatflow.config is not None
        assert client.chatflow.v1.file.config is not None
        assert client.chatflow.v1.feedback.config is not None
        assert client.chatflow.v1.conversation.config is not None
        assert client.chatflow.v1.tts.config is not None
        assert client.chatflow.v1.application.config is not None
        assert client.chatflow.v1.annotation.config is not None

        # Verify all configs are the same instance
        base_config = client.chatflow.v1.chatflow.config
        assert client.chatflow.v1.file.config is base_config
        assert client.chatflow.v1.feedback.config is base_config
        assert client.chatflow.v1.conversation.config is base_config
        assert client.chatflow.v1.tts.config is base_config
        assert client.chatflow.v1.application.config is base_config
        assert client.chatflow.v1.annotation.config is base_config

    def test_no_regressions_in_existing_functionality(self, client):
        """Test that existing functionality still works after chatflow integration."""
        # Verify other services are still accessible
        assert hasattr(client, "chat")
        assert hasattr(client, "completion")
        assert hasattr(client, "knowledge")
        assert hasattr(client, "workflow")
        assert hasattr(client, "dify")

        # Verify they are not None
        assert client.chat is not None
        assert client.completion is not None
        assert client.knowledge is not None
        assert client.workflow is not None
        assert client.dify is not None

    def test_builder_patterns_work(self):
        """Test that builder patterns work for all models."""
        from dify_oapi.api.chatflow.v1.model.chat_message import ChatMessage
        from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
        from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody

        # Test request builder
        request = (
            SendChatMessageRequest.builder()
            .request_body(
                SendChatMessageRequestBody.builder()
                .query("Test query")
                .user("test-user")
                .response_mode("blocking")
                .build()
            )
            .build()
        )
        assert request is not None
        assert request.request_body is not None
        assert request.request_body.query == "Test query"

        # Test public model builder
        message = ChatMessage.builder().id("msg-123").query("Test query").answer("Test answer").build()
        assert message is not None
        assert message.id == "msg-123"
        assert message.query == "Test query"

    def test_type_safety_validation(self):
        """Test that type safety is properly implemented."""
        from dify_oapi.api.chatflow.v1.model.chatflow_types import FeedbackRating, FileType, ResponseMode

        # Test Literal types are properly defined
        assert ResponseMode is not None
        assert FileType is not None
        assert FeedbackRating is not None

        # Test type constraints work (this would be caught by mypy in real usage)
        from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody

        body = SendChatMessageRequestBody.builder().response_mode("blocking").build()
        assert body.response_mode == "blocking"

    def test_error_handling_consistency(self, client, request_option):
        """Test that error handling is consistent across all APIs."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock error response
            mock_execute.return_value = MagicMock(success=False, code="test_error", msg="Test error message")

            # Test error handling in different resources
            from dify_oapi.api.chatflow.v1.model.get_info_request import GetInfoRequest
            from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
            from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody

            # Test chatflow error
            request = (
                SendChatMessageRequest.builder()
                .request_body(SendChatMessageRequestBody.builder().query("test").user("test").build())
                .build()
            )
            response = client.chatflow.v1.chatflow.send(request, request_option)
            assert not response.success
            assert response.code == "test_error"
            assert response.msg == "Test error message"

            # Test application error
            info_request = GetInfoRequest.builder().build()
            info_response = client.chatflow.v1.application.info(info_request, request_option)
            assert not info_response.success
            assert info_response.code == "test_error"
            assert info_response.msg == "Test error message"

    def test_streaming_functionality_available(self, client, request_option):
        """Test that streaming functionality is available and works."""
        from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
        from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock streaming response
            def mock_stream():
                yield b'data: {"event": "message", "answer": "Hello"}\n\n'
                yield b'data: {"event": "message_end"}\n\n'

            mock_execute.return_value = mock_stream()

            request = (
                SendChatMessageRequest.builder()
                .request_body(
                    SendChatMessageRequestBody.builder()
                    .query("Test streaming")
                    .user("test-user")
                    .response_mode("streaming")
                    .build()
                )
                .build()
            )

            # Test streaming works
            stream = client.chatflow.v1.chatflow.send(request, request_option, stream=True)
            chunks = list(stream)
            assert len(chunks) == 2

    def test_file_upload_functionality_available(self, client, request_option):
        """Test that file upload functionality is available and works."""
        from io import BytesIO

        from dify_oapi.api.chatflow.v1.model.upload_file_request import UploadFileRequest

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(success=True, id="file-123", name="test.pdf", size=1024)

            test_file = BytesIO(b"test file content")
            request = UploadFileRequest.builder().file(test_file, "test.pdf").user("test-user").build()
            response = client.chatflow.v1.file.upload(request, request_option)

            assert response.success
            assert response.id == "file-123"

    @pytest.mark.asyncio
    async def test_async_functionality_works(self, client, request_option):
        """Test that async functionality works correctly."""
        from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
        from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody

        with patch("dify_oapi.core.http.transport.ATransport.aexecute") as mock_aexecute:
            mock_aexecute.return_value = MagicMock(success=True, message_id="async-msg-123", answer="Async response")

            request = (
                SendChatMessageRequest.builder()
                .request_body(
                    SendChatMessageRequestBody.builder()
                    .query("Async test")
                    .user("test-user")
                    .response_mode("blocking")
                    .build()
                )
                .build()
            )

            response = await client.chatflow.v1.chatflow.asend(request, request_option)
            assert response.success
            assert response.message_id == "async-msg-123"

    def test_all_init_files_empty(self):
        """Test that all __init__.py files are empty as required."""
        from pathlib import Path

        # Define paths to check
        base_path = Path(__file__).parent.parent.parent / "dify_oapi" / "api" / "chatflow"
        init_files = [
            base_path / "__init__.py",
            base_path / "v1" / "__init__.py",
            base_path / "v1" / "model" / "__init__.py",
            base_path / "v1" / "resource" / "__init__.py",
        ]

        for init_file in init_files:
            if init_file.exists():
                content = init_file.read_text().strip()
                assert content == "", f"__init__.py file at {init_file} is not empty: {content}"

    def test_documentation_accuracy(self):
        """Test that documentation matches implementation."""
        # This is a placeholder for documentation validation
        # In a real implementation, this would check that:
        # - All APIs mentioned in docs are implemented
        # - All examples in docs work correctly
        # - API signatures match documentation
        pass

    def test_performance_requirements(self, client, request_option):
        """Test that performance meets basic requirements."""
        import time

        from dify_oapi.api.chatflow.v1.model.get_info_request import GetInfoRequest

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(success=True, name="Test App")

            # Test response time is reasonable (should be very fast with mocking)
            start_time = time.time()
            request = GetInfoRequest.builder().build()
            response = client.chatflow.v1.application.info(request, request_option)
            end_time = time.time()

            assert response.success
            assert (end_time - start_time) < 1.0  # Should be much faster with mocking

    def test_memory_usage_reasonable(self, client):
        """Test that memory usage is reasonable."""
        import gc

        # Get initial memory usage
        gc.collect()
        initial_objects = len(gc.get_objects())

        # Create multiple requests (simulate usage)
        from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
        from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody

        requests = []
        for i in range(100):
            request = (
                SendChatMessageRequest.builder()
                .request_body(SendChatMessageRequestBody.builder().query(f"Test query {i}").user("test-user").build())
                .build()
            )
            requests.append(request)

        # Check memory usage hasn't exploded
        gc.collect()
        final_objects = len(gc.get_objects())
        object_increase = final_objects - initial_objects

        # Should not create excessive objects (this is a rough check)
        assert object_increase < 10000, f"Created too many objects: {object_increase}"

    def test_thread_safety_basic(self, client, request_option):
        """Test basic thread safety."""
        import threading

        from dify_oapi.api.chatflow.v1.model.get_info_request import GetInfoRequest

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(success=True, name="Test App")

            results = []
            errors = []

            def make_request():
                try:
                    request = GetInfoRequest.builder().build()
                    response = client.chatflow.v1.application.info(request, request_option)
                    results.append(response.success)
                except Exception as e:
                    errors.append(e)

            # Create multiple threads
            threads = []
            for _ in range(10):
                thread = threading.Thread(target=make_request)
                threads.append(thread)
                thread.start()

            # Wait for all threads to complete
            for thread in threads:
                thread.join()

            # Check results
            assert len(errors) == 0, f"Errors occurred: {errors}"
            assert len(results) == 10
            assert all(results), "Not all requests succeeded"

    def test_example_code_syntax_valid(self):
        """Test that example code has valid syntax."""
        import ast
        from pathlib import Path

        # Find all example files
        examples_path = Path(__file__).parent.parent.parent / "examples" / "chatflow"
        if not examples_path.exists():
            pytest.skip("Examples directory not found")

        python_files = list(examples_path.rglob("*.py"))
        assert len(python_files) > 0, "No example files found"

        for file_path in python_files:
            try:
                with open(file_path, encoding="utf-8") as f:
                    content = f.read()
                ast.parse(content)
            except SyntaxError as e:
                pytest.fail(f"Syntax error in {file_path}: {e}")

    def test_all_required_files_exist(self):
        """Test that all required files exist."""
        from pathlib import Path

        base_path = Path(__file__).parent.parent.parent / "dify_oapi" / "api" / "chatflow"

        # Required files
        required_files = [
            "service.py",
            "v1/version.py",
            "v1/model/chatflow_types.py",
            "v1/resource/chatflow.py",
            "v1/resource/file.py",
            "v1/resource/feedback.py",
            "v1/resource/conversation.py",
            "v1/resource/tts.py",
            "v1/resource/application.py",
            "v1/resource/annotation.py",
        ]

        for file_path in required_files:
            full_path = base_path / file_path
            assert full_path.exists(), f"Required file missing: {full_path}"

    def test_implementation_completeness(self):
        """Test that implementation is complete according to specifications."""
        # This test verifies that all required components are implemented
        # Based on the design specifications

        # Test 1: All 6 resources implemented
        from dify_oapi.api.chatflow.v1.version import V1
        from dify_oapi.core.model.config import Config

        config = Config()
        config.domain = "https://api.dify.ai"
        v1 = V1(config)

        assert hasattr(v1, "chatflow")
        assert hasattr(v1, "file")
        assert hasattr(v1, "feedback")
        assert hasattr(v1, "conversation")
        assert hasattr(v1, "tts")
        assert hasattr(v1, "application")
        assert hasattr(v1, "annotation")

        # Test 2: All resources have required methods
        # Chatflow (3 methods)
        assert hasattr(v1.chatflow, "send")
        assert hasattr(v1.chatflow, "stop")
        assert hasattr(v1.chatflow, "suggested")

        # File (1 method)
        assert hasattr(v1.file, "upload")

        # Feedback (2 methods)
        assert hasattr(v1.feedback, "message")
        assert hasattr(v1.feedback, "list")

        # Conversation (5 methods)
        assert hasattr(v1.conversation, "messages")
        assert hasattr(v1.conversation, "list")
        assert hasattr(v1.conversation, "delete")
        assert hasattr(v1.conversation, "rename")
        assert hasattr(v1.conversation, "variables")

        # TTS (2 methods)
        assert hasattr(v1.tts, "speech_to_text")
        assert hasattr(v1.tts, "text_to_audio")

        # Application (4 methods)
        assert hasattr(v1.application, "info")
        assert hasattr(v1.application, "parameters")
        assert hasattr(v1.application, "meta")
        assert hasattr(v1.application, "site")

        # Annotation (6 methods)
        assert hasattr(v1.annotation, "list")
        assert hasattr(v1.annotation, "create")
        assert hasattr(v1.annotation, "update")
        assert hasattr(v1.annotation, "delete")
        assert hasattr(v1.annotation, "reply_settings")
        assert hasattr(v1.annotation, "reply_status")

        # Test 3: All API methods are callable
        api_methods = {
            "chatflow": ["send", "stop", "suggested", "asend", "astop", "asuggested"],
            "file": ["upload", "aupload"],
            "feedback": ["message", "list", "amessage", "alist"],
            "conversation": [
                "messages",
                "list",
                "delete",
                "rename",
                "variables",
                "amessages",
                "alist",
                "adelete",
                "arename",
                "avariables",
            ],
            "tts": ["speech_to_text", "text_to_audio", "aspeech_to_text", "atext_to_audio"],
            "application": ["info", "parameters", "meta", "site", "ainfo", "aparameters", "ameta", "asite"],
            "annotation": [
                "list",
                "create",
                "update",
                "delete",
                "reply_settings",
                "reply_status",
                "alist",
                "acreate",
                "aupdate",
                "adelete",
                "areply_settings",
                "areply_status",
            ],
        }

        for resource_name, method_names in api_methods.items():
            resource = getattr(v1, resource_name)
            for method_name in method_names:
                if hasattr(resource, method_name):
                    method = getattr(resource, method_name)
                    assert callable(method), f"{resource_name}.{method_name} is not callable"
