"""End-to-end integration tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


class TestEndToEnd:
    """Test end-to-end workflows."""

    @pytest.fixture
    def client(self):
        """Create client."""
        return Client.builder().domain("https://api.dify.ai").build()

    @pytest.fixture
    def request_option(self):
        """Create request option."""
        return RequestOption.builder().api_key("test-key").build()

    def test_chat_workflow(self, client, request_option):
        """Test complete chat workflow."""
        req_body = ChatRequestBody.builder().query("Hello").user("user-123").build()
        req = ChatRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock chat response
            mock_execute.return_value = MagicMock(
                answer="Hello! How can I help you?", conversation_id="conv-123", message_id="msg-123"
            )

            result = client.chat.v1.chat.chat(req, request_option)
            assert result.answer == "Hello! How can I help you?"
            assert hasattr(result, "conversation_id")
            assert hasattr(result, "message_id")

    def test_knowledge_workflow(self, client, request_option):
        """Test complete knowledge workflow."""
        from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
        from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody

        req_body = CreateDatasetRequestBody.builder().name("Test Dataset").build()
        req = CreateDatasetRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(
                id="dataset-123", name="Test Dataset", created_at="2024-01-01T00:00:00Z"
            )

            result = client.knowledge.v1.dataset.create(req, request_option)
            assert hasattr(result, "id")
            assert hasattr(result, "name")

    def test_multi_service_workflow(self, client, request_option):
        """Test workflow using multiple services."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Test chat service
            mock_execute.return_value = MagicMock(answer="response")
            chat_result = client.chat.v1.chat.chat(MagicMock(), request_option)
            assert hasattr(chat_result, "answer")

            # Test knowledge service
            mock_execute.return_value = MagicMock(data=[])
            knowledge_result = client.knowledge.v1.dataset.list(MagicMock(), request_option)
            assert hasattr(knowledge_result, "data")

            # Test workflow service
            mock_execute.return_value = MagicMock(workflow_run_id="run-123")
            workflow_result = client.workflow.v1.workflow.run(MagicMock(), request_option)
            assert hasattr(workflow_result, "workflow_run_id")
