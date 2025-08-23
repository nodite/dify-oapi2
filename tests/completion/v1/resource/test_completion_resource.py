from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from unittest.mock import Mock, patch

import pytest

from dify_oapi.api.completion.v1.model.completion.completion_inputs import CompletionInputs
from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody
from dify_oapi.api.completion.v1.model.completion.send_message_response import SendMessageResponse
from dify_oapi.api.completion.v1.model.completion.stop_response_request import StopResponseRequest
from dify_oapi.api.completion.v1.model.completion.stop_response_request_body import StopResponseRequestBody
from dify_oapi.api.completion.v1.model.completion.stop_response_response import StopResponseResponse
from dify_oapi.api.completion.v1.resource.completion import Completion
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestCompletion:
    """Test cases for Completion resource."""

    @pytest.fixture
    def config(self) -> Config:
        """Create a test config."""
        config = Config()
        config.domain = "https://api.dify.ai"
        return config

    @pytest.fixture
    def request_option(self) -> RequestOption:
        """Create a test request option."""
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def completion(self, config: Config) -> Completion:
        """Create a Completion resource instance."""
        return Completion(config)

    @pytest.fixture
    def send_message_request(self) -> SendMessageRequest:
        """Create a test send message request."""
        inputs = CompletionInputs.builder().query("What is AI?").build()
        request_body = (
            SendMessageRequestBody.builder().inputs(inputs).response_mode("blocking").user("test-user").build()
        )
        return SendMessageRequest.builder().request_body(request_body).build()

    @pytest.fixture
    def stop_response_request(self) -> StopResponseRequest:
        """Create a test stop response request."""
        request_body = StopResponseRequestBody.builder().user("test-user").build()
        return StopResponseRequest.builder().task_id("test-task-id").request_body(request_body).build()

    # ===== SEND MESSAGE TESTS =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_send_message_blocking(
        self,
        mock_execute: Mock,
        completion: Completion,
        send_message_request: SendMessageRequest,
        request_option: RequestOption,
    ) -> None:
        """Test send_message with blocking response mode."""
        # Arrange
        expected_response = SendMessageResponse(
            message_id="test-message-id",
            mode="completion",
            answer="AI is artificial intelligence.",
            created_at=1705395332,
        )
        mock_execute.return_value = expected_response

        # Act
        result = completion.send_message(send_message_request, request_option, stream=False)

        # Assert
        assert isinstance(result, SendMessageResponse)
        assert result.message_id == "test-message-id"
        assert result.answer == "AI is artificial intelligence."
        mock_execute.assert_called_once_with(
            completion.config,
            send_message_request,
            unmarshal_as=SendMessageResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_send_message_streaming(
        self,
        mock_execute: Mock,
        completion: Completion,
        send_message_request: SendMessageRequest,
        request_option: RequestOption,
    ) -> None:
        """Test send_message with streaming response mode."""

        # Arrange
        def mock_stream_generator() -> Iterator[bytes]:
            yield b"AI"
            yield b" is"
            yield b" artificial intelligence."

        mock_execute.return_value = mock_stream_generator()

        # Act
        result = completion.send_message(send_message_request, request_option, stream=True)

        # Assert
        assert isinstance(result, Iterator)
        chunks: list[bytes] = list(result)
        assert chunks == [b"AI", b" is", b" artificial intelligence."]
        mock_execute.assert_called_once_with(
            completion.config, send_message_request, stream=True, option=request_option
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_asend_message_blocking(
        self,
        mock_aexecute: Mock,
        completion: Completion,
        send_message_request: SendMessageRequest,
        request_option: RequestOption,
    ) -> None:
        """Test asend_message with blocking response mode."""
        # Arrange
        expected_response = SendMessageResponse(
            message_id="test-message-id",
            mode="completion",
            answer="AI is artificial intelligence.",
            created_at=1705395332,
        )
        mock_aexecute.return_value = expected_response

        # Act
        result = await completion.asend_message(send_message_request, request_option, stream=False)

        # Assert
        assert isinstance(result, SendMessageResponse)
        assert result.message_id == "test-message-id"
        assert result.answer == "AI is artificial intelligence."
        mock_aexecute.assert_called_once_with(
            completion.config,
            send_message_request,
            unmarshal_as=SendMessageResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_asend_message_streaming(
        self,
        mock_aexecute: Mock,
        completion: Completion,
        send_message_request: SendMessageRequest,
        request_option: RequestOption,
    ) -> None:
        """Test asend_message with streaming response mode."""

        # Arrange
        async def mock_async_stream_generator() -> AsyncIterator[bytes]:
            yield b"AI"
            yield b" is"
            yield b" artificial intelligence."

        mock_aexecute.return_value = mock_async_stream_generator()

        # Act
        result = await completion.asend_message(send_message_request, request_option, stream=True)

        # Assert
        assert hasattr(result, "__aiter__")  # Check if it's an async iterator
        chunks: list[bytes] = []
        async for chunk in result:
            chunks.append(chunk)
        assert chunks == [b"AI", b" is", b" artificial intelligence."]
        mock_aexecute.assert_called_once_with(
            completion.config, send_message_request, stream=True, option=request_option
        )

    # ===== STOP RESPONSE TESTS =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_stop_response(
        self,
        mock_execute: Mock,
        completion: Completion,
        stop_response_request: StopResponseRequest,
        request_option: RequestOption,
    ) -> None:
        """Test stop_response method."""
        # Arrange
        expected_response = StopResponseResponse(result="success")
        mock_execute.return_value = expected_response

        # Act
        result = completion.stop_response(stop_response_request, request_option)

        # Assert
        assert isinstance(result, StopResponseResponse)
        assert result.result == "success"
        mock_execute.assert_called_once_with(
            completion.config,
            stop_response_request,
            unmarshal_as=StopResponseResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_astop_response(
        self,
        mock_aexecute: Mock,
        completion: Completion,
        stop_response_request: StopResponseRequest,
        request_option: RequestOption,
    ) -> None:
        """Test astop_response method."""
        # Arrange
        expected_response = StopResponseResponse(result="success")
        mock_aexecute.return_value = expected_response

        # Act
        result = await completion.astop_response(stop_response_request, request_option)

        # Assert
        assert isinstance(result, StopResponseResponse)
        assert result.result == "success"
        mock_aexecute.assert_called_once_with(
            completion.config,
            stop_response_request,
            unmarshal_as=StopResponseResponse,
            option=request_option,
        )

    # ===== ERROR HANDLING TESTS =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_send_message_error_handling(
        self,
        mock_execute: Mock,
        completion: Completion,
        send_message_request: SendMessageRequest,
        request_option: RequestOption,
    ) -> None:
        """Test send_message error handling."""
        # Arrange
        mock_execute.side_effect = Exception("API Error")

        # Act & Assert
        with pytest.raises(Exception, match="API Error"):
            completion.send_message(send_message_request, request_option, stream=False)

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_send_message_streaming_error_handling(
        self,
        mock_execute: Mock,
        completion: Completion,
        send_message_request: SendMessageRequest,
        request_option: RequestOption,
    ) -> None:
        """Test send_message streaming error handling."""
        # Arrange
        mock_execute.side_effect = Exception("Streaming Error")

        # Act & Assert
        with pytest.raises(Exception, match="Streaming Error"):
            completion.send_message(send_message_request, request_option, stream=True)

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_stop_response_error_handling(
        self,
        mock_execute: Mock,
        completion: Completion,
        stop_response_request: StopResponseRequest,
        request_option: RequestOption,
    ) -> None:
        """Test stop_response error handling."""
        # Arrange
        mock_execute.side_effect = Exception("Stop Error")

        # Act & Assert
        with pytest.raises(Exception, match="Stop Error"):
            completion.stop_response(stop_response_request, request_option)

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_asend_message_error_handling(
        self,
        mock_aexecute: Mock,
        completion: Completion,
        send_message_request: SendMessageRequest,
        request_option: RequestOption,
    ) -> None:
        """Test asend_message error handling."""
        # Arrange
        mock_aexecute.side_effect = Exception("Async API Error")

        # Act & Assert
        with pytest.raises(Exception, match="Async API Error"):
            await completion.asend_message(send_message_request, request_option, stream=False)

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_asend_message_streaming_error_handling(
        self,
        mock_aexecute: Mock,
        completion: Completion,
        send_message_request: SendMessageRequest,
        request_option: RequestOption,
    ) -> None:
        """Test asend_message streaming error handling."""
        # Arrange
        mock_aexecute.side_effect = Exception("Async Streaming Error")

        # Act & Assert
        with pytest.raises(Exception, match="Async Streaming Error"):
            await completion.asend_message(send_message_request, request_option, stream=True)

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_astop_response_error_handling(
        self,
        mock_aexecute: Mock,
        completion: Completion,
        stop_response_request: StopResponseRequest,
        request_option: RequestOption,
    ) -> None:
        """Test astop_response error handling."""
        # Arrange
        mock_aexecute.side_effect = Exception("Async Stop Error")

        # Act & Assert
        with pytest.raises(Exception, match="Async Stop Error"):
            await completion.astop_response(stop_response_request, request_option)

    # ===== CONFIGURATION TESTS =====

    def test_completion_initialization(self, config: Config) -> None:
        """Test Completion resource initialization."""
        # Act
        completion = Completion(config)

        # Assert
        assert completion.config == config
        assert isinstance(completion.config, Config)

    def test_completion_config_propagation(self, completion: Completion, config: Config) -> None:
        """Test that config is properly stored and accessible."""
        # Assert
        assert completion.config is config
        assert completion.config.domain == "https://api.dify.ai"
