from __future__ import annotations

from unittest.mock import AsyncMock, Mock, patch

import pytest

from dify_oapi.api.completion.v1.model.audio.text_to_audio_request import TextToAudioRequest
from dify_oapi.api.completion.v1.model.audio.text_to_audio_request_body import TextToAudioRequestBody
from dify_oapi.api.completion.v1.model.audio.text_to_audio_response import TextToAudioResponse
from dify_oapi.api.completion.v1.resource.audio import Audio
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestAudio:
    @pytest.fixture
    def config(self) -> Config:
        config = Config()
        config.domain = "https://api.dify.ai"
        return config

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def audio_resource(self, config: Config) -> Audio:
        return Audio(config)

    @pytest.fixture
    def text_to_audio_request(self) -> TextToAudioRequest:
        request_body = TextToAudioRequestBody.builder().text("Hello, this is a test message").user("test-user").build()
        return TextToAudioRequest.builder().request_body(request_body).build()

    @pytest.fixture
    def text_to_audio_response(self) -> TextToAudioResponse:
        return TextToAudioResponse(content_type="audio/wav", data=b"fake_audio_data")

    def test_audio_initialization(self, config: Config) -> None:
        audio = Audio(config)
        assert audio.config == config

    @patch("dify_oapi.api.completion.v1.resource.audio.Transport.execute")
    def test_text_to_audio_sync(
        self,
        mock_execute: Mock,
        audio_resource: Audio,
        text_to_audio_request: TextToAudioRequest,
        request_option: RequestOption,
        text_to_audio_response: TextToAudioResponse,
    ) -> None:
        # Arrange
        mock_execute.return_value = text_to_audio_response

        # Act
        result = audio_resource.text_to_audio(text_to_audio_request, request_option)

        # Assert
        assert result == text_to_audio_response
        mock_execute.assert_called_once_with(
            audio_resource.config, text_to_audio_request, unmarshal_as=TextToAudioResponse, option=request_option
        )

    @patch("dify_oapi.api.completion.v1.resource.audio.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_text_to_audio_async(
        self,
        mock_aexecute: AsyncMock,
        audio_resource: Audio,
        text_to_audio_request: TextToAudioRequest,
        request_option: RequestOption,
        text_to_audio_response: TextToAudioResponse,
    ) -> None:
        # Arrange
        mock_aexecute.return_value = text_to_audio_response

        # Act
        result = await audio_resource.atext_to_audio(text_to_audio_request, request_option)

        # Assert
        assert result == text_to_audio_response
        mock_aexecute.assert_called_once_with(
            audio_resource.config, text_to_audio_request, unmarshal_as=TextToAudioResponse, option=request_option
        )

    @patch("dify_oapi.api.completion.v1.resource.audio.Transport.execute")
    def test_text_to_audio_with_message_id(
        self,
        mock_execute: Mock,
        audio_resource: Audio,
        request_option: RequestOption,
        text_to_audio_response: TextToAudioResponse,
    ) -> None:
        # Arrange
        request_body = TextToAudioRequestBody.builder().message_id("test-message-id").user("test-user").build()
        request = TextToAudioRequest.builder().request_body(request_body).build()
        mock_execute.return_value = text_to_audio_response

        # Act
        result = audio_resource.text_to_audio(request, request_option)

        # Assert
        assert result == text_to_audio_response
        mock_execute.assert_called_once_with(
            audio_resource.config, request, unmarshal_as=TextToAudioResponse, option=request_option
        )

    @patch("dify_oapi.api.completion.v1.resource.audio.Transport.execute")
    def test_text_to_audio_error_handling(
        self,
        mock_execute: Mock,
        audio_resource: Audio,
        text_to_audio_request: TextToAudioRequest,
        request_option: RequestOption,
    ) -> None:
        # Arrange
        mock_execute.side_effect = Exception("API Error")

        # Act & Assert
        with pytest.raises(Exception, match="API Error"):
            audio_resource.text_to_audio(text_to_audio_request, request_option)

    @patch("dify_oapi.api.completion.v1.resource.audio.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_text_to_audio_async_error_handling(
        self,
        mock_aexecute: AsyncMock,
        audio_resource: Audio,
        text_to_audio_request: TextToAudioRequest,
        request_option: RequestOption,
    ) -> None:
        # Arrange
        mock_aexecute.side_effect = Exception("Async API Error")

        # Act & Assert
        with pytest.raises(Exception, match="Async API Error"):
            await audio_resource.atext_to_audio(text_to_audio_request, request_option)

    def test_text_to_audio_binary_data_handling(
        self,
        audio_resource: Audio,
        request_option: RequestOption,
    ) -> None:
        # Arrange
        request_body = TextToAudioRequestBody.builder().text("Test audio content").user("test-user").build()
        request = TextToAudioRequest.builder().request_body(request_body).build()

        # Mock response with binary data
        binary_response = TextToAudioResponse(
            content_type="audio/mp3",
            data=b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR",  # Sample binary data
        )

        with patch("dify_oapi.api.completion.v1.resource.audio.Transport.execute") as mock_execute:
            mock_execute.return_value = binary_response

            # Act
            result = audio_resource.text_to_audio(request, request_option)

            # Assert
            assert result.data == b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR"
            assert result.content_type == "audio/mp3"
            assert result.success is True

    @patch("dify_oapi.api.completion.v1.resource.audio.Transport.execute")
    def test_text_to_audio_different_content_types(
        self,
        mock_execute: Mock,
        audio_resource: Audio,
        text_to_audio_request: TextToAudioRequest,
        request_option: RequestOption,
    ) -> None:
        # Test different audio content types
        content_types = ["audio/wav", "audio/mp3", "audio/mpeg", "audio/ogg"]

        for content_type in content_types:
            # Arrange
            response = TextToAudioResponse(content_type=content_type, data=b"fake_audio_data")
            mock_execute.return_value = response

            # Act
            result = audio_resource.text_to_audio(text_to_audio_request, request_option)

            # Assert
            assert result.content_type == content_type
            assert result.data == b"fake_audio_data"
