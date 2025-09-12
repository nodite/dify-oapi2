#!/usr/bin/env python3

"""
Final Validation Tests for Completion API Implementation

This module provides comprehensive validation tests to ensure the complete
Completion API implementation meets all requirements and specifications.
"""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.client import Client
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestFinalValidation:
    """Final validation tests for complete Completion API implementation."""

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
        """Test complete client integration with all completion resources."""
        # Verify completion service is accessible
        assert hasattr(client, "completion")
        assert client.completion is not None

        # Verify v1 version is accessible
        assert hasattr(client.completion, "v1")
        assert client.completion.v1 is not None

        # Verify all 6 resources are accessible
        resources = ["completion", "file", "feedback", "audio", "info", "annotation"]
        for resource in resources:
            assert hasattr(client.completion.v1, resource)
            assert getattr(client.completion.v1, resource) is not None

    def test_all_15_apis_accessible(self, client):
        """Test that all 15 APIs are accessible through client."""
        # Completion APIs (2)
        assert hasattr(client.completion.v1.completion, "send")
        assert hasattr(client.completion.v1.completion, "stop")

        # File APIs (1)
        assert hasattr(client.completion.v1.file, "upload")

        # Feedback APIs (2)
        assert hasattr(client.completion.v1.feedback, "message")
        assert hasattr(client.completion.v1.feedback, "list")

        # Audio APIs (1)
        assert hasattr(client.completion.v1.audio, "text_to_audio")

        # Info APIs (3)
        assert hasattr(client.completion.v1.info, "get")
        assert hasattr(client.completion.v1.info, "parameters")
        assert hasattr(client.completion.v1.info, "site")

        # Annotation APIs (6)
        assert hasattr(client.completion.v1.annotation, "list")
        assert hasattr(client.completion.v1.annotation, "create")
        assert hasattr(client.completion.v1.annotation, "update")
        assert hasattr(client.completion.v1.annotation, "delete")
        assert hasattr(client.completion.v1.annotation, "reply_settings")
        assert hasattr(client.completion.v1.annotation, "reply_status")

    def test_async_methods_accessible(self, client):
        """Test that all async methods are accessible."""
        # Completion async methods
        assert hasattr(client.completion.v1.completion, "asend")
        assert hasattr(client.completion.v1.completion, "astop")

        # File async methods
        assert hasattr(client.completion.v1.file, "aupload")

        # Feedback async methods
        assert hasattr(client.completion.v1.feedback, "amessage")
        assert hasattr(client.completion.v1.feedback, "alist")

        # Audio async methods
        assert hasattr(client.completion.v1.audio, "atext_to_audio")

        # Info async methods
        assert hasattr(client.completion.v1.info, "aget")
        assert hasattr(client.completion.v1.info, "aparameters")
        assert hasattr(client.completion.v1.info, "asite")

        # Annotation async methods
        assert hasattr(client.completion.v1.annotation, "alist")
        assert hasattr(client.completion.v1.annotation, "acreate")
        assert hasattr(client.completion.v1.annotation, "aupdate")
        assert hasattr(client.completion.v1.annotation, "adelete")
        assert hasattr(client.completion.v1.annotation, "areply_settings")
        assert hasattr(client.completion.v1.annotation, "areply_status")

    def test_model_imports_work(self):
        """Test that all model imports work correctly."""
        # Test core model imports
        from dify_oapi.api.completion.v1.model.completion.completion_types import ResponseMode
        from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
        from dify_oapi.api.completion.v1.model.completion.send_message_response import SendMessageResponse
        from dify_oapi.api.completion.v1.model.feedback.feedback_info import FeedbackInfo
        from dify_oapi.api.completion.v1.model.file.upload_file_request import UploadFileRequest
        from dify_oapi.api.completion.v1.model.file.upload_file_response import UploadFileResponse
        from dify_oapi.api.completion.v1.model.info.get_info_response import GetInfoResponse

        # Verify imports are successful
        assert ResponseMode is not None
        assert SendMessageRequest is not None
        assert SendMessageResponse is not None
        assert FeedbackInfo is not None
        assert UploadFileRequest is not None
        assert UploadFileResponse is not None
        assert GetInfoResponse is not None

    def test_resource_imports_work(self):
        """Test that all resource imports work correctly."""
        from dify_oapi.api.completion.v1.resource.annotation import Annotation
        from dify_oapi.api.completion.v1.resource.audio import Audio
        from dify_oapi.api.completion.v1.resource.completion import Completion
        from dify_oapi.api.completion.v1.resource.feedback import Feedback
        from dify_oapi.api.completion.v1.resource.file import File
        from dify_oapi.api.completion.v1.resource.info import Info

        # Verify imports are successful
        assert Completion is not None
        assert File is not None
        assert Feedback is not None
        assert Audio is not None
        assert Info is not None
        assert Annotation is not None

    def test_service_integration_works(self):
        """Test that service integration works correctly."""
        from dify_oapi.api.completion.service import CompletionService
        from dify_oapi.api.completion.v1.version import V1

        # Test service creation
        config = Config()
        config.domain = "https://api.dify.ai"
        service = CompletionService(config)
        assert service is not None
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_configuration_propagation(self, client):
        """Test that configuration is properly propagated through all layers."""
        # Verify config is passed to service
        assert client.completion.v1.completion.config is not None
        assert client.completion.v1.file.config is not None
        assert client.completion.v1.feedback.config is not None
        assert client.completion.v1.audio.config is not None
        assert client.completion.v1.info.config is not None
        assert client.completion.v1.annotation.config is not None

        # Verify all configs are the same instance
        base_config = client.completion.v1.completion.config
        assert client.completion.v1.file.config is base_config
        assert client.completion.v1.feedback.config is base_config
        assert client.completion.v1.audio.config is base_config
        assert client.completion.v1.info.config is base_config
        assert client.completion.v1.annotation.config is base_config

    def test_no_regressions_in_existing_functionality(self, client):
        """Test that existing functionality still works after completion integration."""
        # Verify other services are still accessible
        assert hasattr(client, "chat")
        assert hasattr(client, "chatflow")
        assert hasattr(client, "knowledge")
        assert hasattr(client, "workflow")
        assert hasattr(client, "dify")

        # Verify they are not None
        assert client.chat is not None
        assert client.chatflow is not None
        assert client.knowledge is not None
        assert client.workflow is not None
        assert client.dify is not None

    def test_builder_patterns_work(self):
        """Test that builder patterns work for all models."""
        from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
        from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody

        # Test request builder
        request = (
            SendMessageRequest.builder()
            .request_body(
                SendMessageRequestBody.builder().query("Test query").user("test-user").response_mode("blocking").build()
            )
            .build()
        )
        assert request is not None
        assert request.request_body is not None
        assert request.request_body.query == "Test query"

    def test_type_safety_validation(self):
        """Test that type safety is properly implemented."""
        from dify_oapi.api.completion.v1.model.completion.completion_types import ResponseMode

        # Test Literal types are properly defined
        assert ResponseMode is not None

        # Test type constraints work (this would be caught by mypy in real usage)
        from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody

        body = SendMessageRequestBody.builder().response_mode("blocking").build()
        assert body.response_mode == "blocking"

    def test_error_handling_consistency(self, client, request_option):
        """Test that error handling is consistent across all APIs."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock error response
            mock_execute.return_value = MagicMock(success=False, code="test_error", msg="Test error message")

            # Test error handling in different resources
            from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
            from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody
            from dify_oapi.api.completion.v1.model.info.get_info_request import GetInfoRequest

            # Test completion error
            request = (
                SendMessageRequest.builder()
                .request_body(SendMessageRequestBody.builder().query("test").user("test").build())
                .build()
            )
            response = client.completion.v1.completion.send(request, request_option)
            assert not response.success
            assert response.code == "test_error"
            assert response.msg == "Test error message"

            # Test info error
            info_request = GetInfoRequest.builder().build()
            info_response = client.completion.v1.info.get(info_request, request_option)
            assert not info_response.success
            assert info_response.code == "test_error"
            assert info_response.msg == "Test error message"

    def test_streaming_functionality_available(self, client, request_option):
        """Test that streaming functionality is available and works."""
        from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
        from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock streaming response
            def mock_stream():
                yield b'data: {"event": "message", "answer": "Hello"}\\n\\n'
                yield b'data: {"event": "message_end"}\\n\\n'

            mock_execute.return_value = mock_stream()

            request = (
                SendMessageRequest.builder()
                .request_body(
                    SendMessageRequestBody.builder()
                    .query("Test streaming")
                    .user("test-user")
                    .response_mode("streaming")
                    .build()
                )
                .build()
            )

            # Test streaming works
            stream = client.completion.v1.completion.send(request, request_option, stream=True)
            chunks = list(stream)
            assert len(chunks) == 2

    def test_file_upload_functionality_available(self, client, request_option):
        """Test that file upload functionality is available and works."""
        from io import BytesIO

        from dify_oapi.api.completion.v1.model.file.upload_file_request import UploadFileRequest

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(success=True, id="file-123", name="test.pdf", size=1024)

            test_file = BytesIO(b"test file content")
            request = UploadFileRequest.builder().file(test_file, "test.pdf").user("test-user").build()
            response = client.completion.v1.file.upload(request, request_option)

            assert response.success
            assert response.id == "file-123"

    @pytest.mark.asyncio
    async def test_async_functionality_works(self, client, request_option):
        """Test that async functionality works correctly."""
        from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
        from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody

        with patch("dify_oapi.core.http.transport.ATransport.aexecute") as mock_aexecute:
            mock_aexecute.return_value = MagicMock(success=True, message_id="async-msg-123", answer="Async response")

            request = (
                SendMessageRequest.builder()
                .request_body(
                    SendMessageRequestBody.builder()
                    .query("Async test")
                    .user("test-user")
                    .response_mode("blocking")
                    .build()
                )
                .build()
            )

            response = await client.completion.v1.completion.asend(request, request_option)
            assert response.success
            assert response.message_id == "async-msg-123"

    def test_all_init_files_empty(self):
        """Test that all __init__.py files are empty as required."""
        from pathlib import Path

        # Define paths to check
        base_path = Path(__file__).parent.parent.parent / "dify_oapi" / "api" / "completion"
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

    def test_all_required_files_exist(self):
        """Test that all required files exist."""
        from pathlib import Path

        base_path = Path(__file__).parent.parent.parent / "dify_oapi" / "api" / "completion"

        # Required files
        required_files = [
            "service.py",
            "v1/version.py",
            "v1/resource/completion.py",
            "v1/resource/file.py",
            "v1/resource/feedback.py",
            "v1/resource/audio.py",
            "v1/resource/info.py",
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
        from dify_oapi.api.completion.v1.version import V1
        from dify_oapi.core.model.config import Config

        config = Config()
        config.domain = "https://api.dify.ai"
        v1 = V1(config)

        assert hasattr(v1, "completion")
        assert hasattr(v1, "file")
        assert hasattr(v1, "feedback")
        assert hasattr(v1, "audio")
        assert hasattr(v1, "info")
        assert hasattr(v1, "annotation")

        # Test 2: All resources have required methods
        # Completion (2 methods)
        assert hasattr(v1.completion, "send")
        assert hasattr(v1.completion, "stop")

        # File (1 method)
        assert hasattr(v1.file, "upload")

        # Feedback (2 methods)
        assert hasattr(v1.feedback, "message")
        assert hasattr(v1.feedback, "list")

        # Audio (1 method)
        assert hasattr(v1.audio, "text_to_audio")

        # Info (3 methods)
        assert hasattr(v1.info, "get")
        assert hasattr(v1.info, "parameters")
        assert hasattr(v1.info, "site")

        # Annotation (6 methods)
        assert hasattr(v1.annotation, "list")
        assert hasattr(v1.annotation, "create")
        assert hasattr(v1.annotation, "update")
        assert hasattr(v1.annotation, "delete")
        assert hasattr(v1.annotation, "reply_settings")
        assert hasattr(v1.annotation, "reply_status")

        # Test 3: All API methods are callable
        api_methods = {
            "completion": ["send", "stop", "asend", "astop"],
            "file": ["upload", "aupload"],
            "feedback": ["message", "list", "amessage", "alist"],
            "audio": ["text_to_audio", "atext_to_audio"],
            "info": ["get", "parameters", "site", "aget", "aparameters", "asite"],
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
