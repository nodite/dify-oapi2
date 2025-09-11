from unittest.mock import patch

import pytest

from dify_oapi.api.chatflow.v1.model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from dify_oapi.api.chatflow.v1.model.get_suggested_questions_response import GetSuggestedQuestionsResponse
from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
from dify_oapi.api.chatflow.v1.model.send_chat_message_response import SendChatMessageResponse
from dify_oapi.api.chatflow.v1.model.stop_chat_message_request import StopChatMessageRequest
from dify_oapi.api.chatflow.v1.model.stop_chat_message_response import StopChatMessageResponse
from dify_oapi.api.chatflow.v1.resource.chatflow import Chatflow
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestChatflowResource:
    @pytest.fixture
    def config(self):
        config = Config()
        config.domain = "https://api.dify.ai"
        return config

    @pytest.fixture
    def request_option(self):
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def chatflow_resource(self, config):
        return Chatflow(config)

    @pytest.fixture
    def send_request(self):
        return SendChatMessageRequest.builder().build()

    @pytest.fixture
    def stop_request(self):
        return StopChatMessageRequest.builder().build()

    @pytest.fixture
    def suggested_request(self):
        return GetSuggestedQuestionsRequest.builder().build()

    def test_chatflow_resource_initialization(self, config):
        """Test Chatflow resource initialization."""
        resource = Chatflow(config)
        assert resource.config == config

    @patch("dify_oapi.api.chatflow.v1.resource.chatflow.Transport.execute")
    def test_send_blocking_mode(self, mock_execute, chatflow_resource, send_request, request_option):
        """Test send method in blocking mode."""
        mock_response = SendChatMessageResponse(success=True)
        mock_execute.return_value = mock_response

        result = chatflow_resource.send(send_request, request_option, stream=False)

        assert result == mock_response
        mock_execute.assert_called_once_with(
            chatflow_resource.config,
            send_request,
            unmarshal_as=SendChatMessageResponse,
            option=request_option,
        )

    @patch("dify_oapi.api.chatflow.v1.resource.chatflow.Transport.execute")
    def test_send_streaming_mode(self, mock_execute, chatflow_resource, send_request, request_option):
        """Test send method in streaming mode."""
        mock_generator = (b"chunk1", b"chunk2", b"chunk3")
        mock_execute.return_value = mock_generator

        result = chatflow_resource.send(send_request, request_option, stream=True)

        assert result == mock_generator
        mock_execute.assert_called_once_with(chatflow_resource.config, send_request, stream=True, option=request_option)

    @patch("dify_oapi.api.chatflow.v1.resource.chatflow.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_asend_blocking_mode(self, mock_aexecute, chatflow_resource, send_request, request_option):
        """Test asend method in blocking mode."""
        mock_response = SendChatMessageResponse(success=True)
        mock_aexecute.return_value = mock_response

        result = await chatflow_resource.asend(send_request, request_option, stream=False)

        assert result == mock_response
        mock_aexecute.assert_called_once_with(
            chatflow_resource.config,
            send_request,
            unmarshal_as=SendChatMessageResponse,
            option=request_option,
        )

    @patch("dify_oapi.api.chatflow.v1.resource.chatflow.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_asend_streaming_mode(self, mock_aexecute, chatflow_resource, send_request, request_option):
        """Test asend method in streaming mode."""

        async def mock_async_generator():
            yield b"chunk1"
            yield b"chunk2"
            yield b"chunk3"

        mock_aexecute.return_value = mock_async_generator()

        result = await chatflow_resource.asend(send_request, request_option, stream=True)

        # For async generators, we need to check the type
        assert hasattr(result, "__aiter__")
        mock_aexecute.assert_called_once_with(
            chatflow_resource.config, send_request, stream=True, option=request_option
        )

    @patch("dify_oapi.api.chatflow.v1.resource.chatflow.Transport.execute")
    def test_stop(self, mock_execute, chatflow_resource, stop_request, request_option):
        """Test stop method."""
        mock_response = StopChatMessageResponse(success=True, result="success")
        mock_execute.return_value = mock_response

        result = chatflow_resource.stop(stop_request, request_option)

        assert result == mock_response
        mock_execute.assert_called_once_with(
            chatflow_resource.config,
            stop_request,
            unmarshal_as=StopChatMessageResponse,
            option=request_option,
        )

    @patch("dify_oapi.api.chatflow.v1.resource.chatflow.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_astop(self, mock_aexecute, chatflow_resource, stop_request, request_option):
        """Test astop method."""
        mock_response = StopChatMessageResponse(success=True, result="success")
        mock_aexecute.return_value = mock_response

        result = await chatflow_resource.astop(stop_request, request_option)

        assert result == mock_response
        mock_aexecute.assert_called_once_with(
            chatflow_resource.config,
            stop_request,
            unmarshal_as=StopChatMessageResponse,
            option=request_option,
        )

    @patch("dify_oapi.api.chatflow.v1.resource.chatflow.Transport.execute")
    def test_suggested(self, mock_execute, chatflow_resource, suggested_request, request_option):
        """Test suggested method."""
        mock_response = GetSuggestedQuestionsResponse(success=True, result="success", data=["Question 1", "Question 2"])
        mock_execute.return_value = mock_response

        result = chatflow_resource.suggested(suggested_request, request_option)

        assert result == mock_response
        mock_execute.assert_called_once_with(
            chatflow_resource.config,
            suggested_request,
            unmarshal_as=GetSuggestedQuestionsResponse,
            option=request_option,
        )

    @patch("dify_oapi.api.chatflow.v1.resource.chatflow.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_asuggested(self, mock_aexecute, chatflow_resource, suggested_request, request_option):
        """Test asuggested method."""
        mock_response = GetSuggestedQuestionsResponse(success=True, result="success", data=["Question 1", "Question 2"])
        mock_aexecute.return_value = mock_response

        result = await chatflow_resource.asuggested(suggested_request, request_option)

        assert result == mock_response
        mock_aexecute.assert_called_once_with(
            chatflow_resource.config,
            suggested_request,
            unmarshal_as=GetSuggestedQuestionsResponse,
            option=request_option,
        )

    @patch("dify_oapi.api.chatflow.v1.resource.chatflow.Transport.execute")
    def test_send_error_handling(self, mock_execute, chatflow_resource, send_request, request_option):
        """Test send method error handling."""
        mock_execute.side_effect = Exception("API Error")

        with pytest.raises(Exception, match="API Error"):
            chatflow_resource.send(send_request, request_option)

    @patch("dify_oapi.api.chatflow.v1.resource.chatflow.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_asend_error_handling(self, mock_aexecute, chatflow_resource, send_request, request_option):
        """Test asend method error handling."""
        mock_aexecute.side_effect = Exception("API Error")

        with pytest.raises(Exception, match="API Error"):
            await chatflow_resource.asend(send_request, request_option)

    @patch("dify_oapi.api.chatflow.v1.resource.chatflow.Transport.execute")
    def test_stop_error_handling(self, mock_execute, chatflow_resource, stop_request, request_option):
        """Test stop method error handling."""
        mock_execute.side_effect = Exception("API Error")

        with pytest.raises(Exception, match="API Error"):
            chatflow_resource.stop(stop_request, request_option)

    @patch("dify_oapi.api.chatflow.v1.resource.chatflow.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_astop_error_handling(self, mock_aexecute, chatflow_resource, stop_request, request_option):
        """Test astop method error handling."""
        mock_aexecute.side_effect = Exception("API Error")

        with pytest.raises(Exception, match="API Error"):
            await chatflow_resource.astop(stop_request, request_option)

    @patch("dify_oapi.api.chatflow.v1.resource.chatflow.Transport.execute")
    def test_suggested_error_handling(self, mock_execute, chatflow_resource, suggested_request, request_option):
        """Test suggested method error handling."""
        mock_execute.side_effect = Exception("API Error")

        with pytest.raises(Exception, match="API Error"):
            chatflow_resource.suggested(suggested_request, request_option)

    @patch("dify_oapi.api.chatflow.v1.resource.chatflow.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_asuggested_error_handling(self, mock_aexecute, chatflow_resource, suggested_request, request_option):
        """Test asuggested method error handling."""
        mock_aexecute.side_effect = Exception("API Error")

        with pytest.raises(Exception, match="API Error"):
            await chatflow_resource.asuggested(suggested_request, request_option)
