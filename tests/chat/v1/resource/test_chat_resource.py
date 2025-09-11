from collections.abc import AsyncGenerator
from unittest.mock import patch

import pytest

from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.api.chat.v1.model.chat_response import ChatResponse
from dify_oapi.api.chat.v1.model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from dify_oapi.api.chat.v1.model.get_suggested_questions_response import GetSuggestedQuestionsResponse
from dify_oapi.api.chat.v1.model.stop_chat_request import StopChatRequest
from dify_oapi.api.chat.v1.model.stop_chat_request_body import StopChatRequestBody
from dify_oapi.api.chat.v1.model.stop_chat_response import StopChatResponse
from dify_oapi.api.chat.v1.resource.chat import Chat
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestChatResource:
    @pytest.fixture
    def chat_resource(self):
        """Create Chat resource instance for testing"""
        config = Config()
        return Chat(config)

    @pytest.fixture
    def request_option(self):
        """Create RequestOption for testing"""
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def chat_request(self):
        """Create ChatRequest for testing"""
        request_body = (
            ChatRequestBody.builder().query("Hello, how are you?").user("test-user").response_mode("blocking").build()
        )
        return ChatRequest.builder().request_body(request_body).build()

    @pytest.fixture
    def stop_chat_request(self):
        """Create StopChatRequest for testing"""
        request_body = StopChatRequestBody.builder().user("test-user").build()
        return StopChatRequest.builder().task_id("test-task-id").request_body(request_body).build()

    @pytest.fixture
    def suggested_questions_request(self):
        """Create GetSuggestedQuestionsRequest for testing"""
        return GetSuggestedQuestionsRequest.builder().message_id("test-message-id").user("test-user").build()

    def test_chat_resource_initialization(self, chat_resource):
        """Test Chat resource initialization"""
        assert isinstance(chat_resource, Chat)
        assert hasattr(chat_resource, "config")
        assert chat_resource.config is not None

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_chat_blocking(self, mock_execute, chat_resource, chat_request, request_option):
        """Test blocking chat method"""
        # Setup mock response
        mock_response = ChatResponse(
            message_id="test-message-id",
            conversation_id="test-conversation-id",
            answer="Hello! I'm doing well, thank you for asking.",
        )
        mock_execute.return_value = mock_response

        # Execute request
        result = chat_resource.chat(chat_request, request_option, stream=False)

        # Verify result
        assert isinstance(result, ChatResponse)
        assert result.message_id == "test-message-id"
        assert result.conversation_id == "test-conversation-id"
        assert result.answer == "Hello! I'm doing well, thank you for asking."

        # Verify Transport.execute was called correctly
        mock_execute.assert_called_once_with(
            chat_resource.config, chat_request, unmarshal_as=ChatResponse, option=request_option
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_chat_streaming(self, mock_execute, chat_resource, chat_request, request_option):
        """Test streaming chat method"""
        # Setup mock streaming response
        mock_stream = iter([b"Hello", b" there", b"!"])
        mock_execute.return_value = mock_stream

        # Execute streaming request
        result = chat_resource.chat(chat_request, request_option, stream=True)

        # Verify result is iterable (can be generator or iterator)
        assert hasattr(result, "__iter__")
        assert hasattr(result, "__next__")

        # Verify Transport.execute was called correctly
        mock_execute.assert_called_once_with(chat_resource.config, chat_request, option=request_option, stream=True)

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_chat_default_blocking(self, mock_execute, chat_resource, chat_request, request_option):
        """Test chat method defaults to blocking mode"""
        # Setup mock response
        mock_response = ChatResponse(answer="Default response")
        mock_execute.return_value = mock_response

        # Execute request without stream parameter
        result = chat_resource.chat(chat_request, request_option)

        # Verify result is ChatResponse (blocking mode)
        assert isinstance(result, ChatResponse)
        assert result.answer == "Default response"

        # Verify Transport.execute was called in blocking mode
        mock_execute.assert_called_once_with(
            chat_resource.config, chat_request, unmarshal_as=ChatResponse, option=request_option
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_achat_blocking(self, mock_aexecute, chat_resource, chat_request, request_option):
        """Test async blocking chat method"""
        # Setup mock response
        mock_response = ChatResponse(message_id="async-message-id", answer="Async response")
        mock_aexecute.return_value = mock_response

        # Execute async request
        result = await chat_resource.achat(chat_request, request_option, stream=False)

        # Verify result
        assert isinstance(result, ChatResponse)
        assert result.message_id == "async-message-id"
        assert result.answer == "Async response"

        # Verify ATransport.aexecute was called correctly
        mock_aexecute.assert_called_once_with(
            chat_resource.config, chat_request, unmarshal_as=ChatResponse, option=request_option
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_achat_streaming(self, mock_aexecute, chat_resource, chat_request, request_option):
        """Test async streaming chat method"""

        # Setup mock async streaming response
        async def mock_async_generator():
            yield b"Async"
            yield b" stream"
            yield b" response"

        mock_aexecute.return_value = mock_async_generator()

        # Execute async streaming request
        result = await chat_resource.achat(chat_request, request_option, stream=True)

        # Verify result is an async generator
        assert isinstance(result, AsyncGenerator)

        # Verify ATransport.aexecute was called correctly
        mock_aexecute.assert_called_once_with(chat_resource.config, chat_request, option=request_option, stream=True)

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_stop_chat(self, mock_execute, chat_resource, stop_chat_request, request_option):
        """Test stop chat method"""
        # Setup mock response
        mock_response = StopChatResponse(result="success")
        mock_execute.return_value = mock_response

        # Execute request
        result = chat_resource.stop(stop_chat_request, request_option)

        # Verify result
        assert isinstance(result, StopChatResponse)
        assert result.result == "success"

        # Verify Transport.execute was called correctly
        mock_execute.assert_called_once_with(
            chat_resource.config, stop_chat_request, unmarshal_as=StopChatResponse, option=request_option
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_astop_chat(self, mock_aexecute, chat_resource, stop_chat_request, request_option):
        """Test async stop chat method"""
        # Setup mock response
        mock_response = StopChatResponse(result="success")
        mock_aexecute.return_value = mock_response

        # Execute async request
        result = await chat_resource.astop(stop_chat_request, request_option)

        # Verify result
        assert isinstance(result, StopChatResponse)
        assert result.result == "success"

        # Verify ATransport.aexecute was called correctly
        mock_aexecute.assert_called_once_with(
            chat_resource.config, stop_chat_request, unmarshal_as=StopChatResponse, option=request_option
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_suggested_questions(self, mock_execute, chat_resource, suggested_questions_request, request_option):
        """Test suggested questions method"""
        # Setup mock response
        mock_response = GetSuggestedQuestionsResponse(
            result="success", data=["What is AI?", "How does machine learning work?", "Tell me about Python"]
        )
        mock_execute.return_value = mock_response

        # Execute request
        result = chat_resource.suggested(suggested_questions_request, request_option)

        # Verify result
        assert isinstance(result, GetSuggestedQuestionsResponse)
        assert result.result == "success"
        assert len(result.data) == 3
        assert "What is AI?" in result.data

        # Verify Transport.execute was called correctly
        mock_execute.assert_called_once_with(
            chat_resource.config,
            suggested_questions_request,
            unmarshal_as=GetSuggestedQuestionsResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_asuggested_questions(
        self, mock_aexecute, chat_resource, suggested_questions_request, request_option
    ):
        """Test async suggested questions method"""
        # Setup mock response
        mock_response = GetSuggestedQuestionsResponse(result="success", data=["Async question 1", "Async question 2"])
        mock_aexecute.return_value = mock_response

        # Execute async request
        result = await chat_resource.asuggested(suggested_questions_request, request_option)

        # Verify result
        assert isinstance(result, GetSuggestedQuestionsResponse)
        assert result.result == "success"
        assert len(result.data) == 2
        assert "Async question 1" in result.data

        # Verify ATransport.aexecute was called correctly
        mock_aexecute.assert_called_once_with(
            chat_resource.config,
            suggested_questions_request,
            unmarshal_as=GetSuggestedQuestionsResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_error_handling(self, mock_execute, chat_resource, chat_request, request_option):
        """Test error handling in chat methods"""
        # Setup mock to raise exception
        mock_execute.side_effect = Exception("API Error")

        # Verify exception is propagated
        with pytest.raises(Exception, match="API Error"):
            chat_resource.chat(chat_request, request_option)

    def test_method_signatures(self, chat_resource):
        """Test that all required methods exist with correct signatures"""
        # Test sync methods exist
        assert hasattr(chat_resource, "chat")
        assert hasattr(chat_resource, "stop")
        assert hasattr(chat_resource, "suggested")

        # Test async methods exist
        assert hasattr(chat_resource, "achat")
        assert hasattr(chat_resource, "astop")
        assert hasattr(chat_resource, "asuggested")

        # Test methods are callable
        assert callable(chat_resource.chat)
        assert callable(chat_resource.stop)
        assert callable(chat_resource.suggested)
        assert callable(chat_resource.achat)
        assert callable(chat_resource.astop)
        assert callable(chat_resource.asuggested)
