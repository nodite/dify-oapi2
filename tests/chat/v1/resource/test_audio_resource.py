from io import BytesIO
from unittest.mock import patch

import pytest

from dify_oapi.api.chat.v1.model.audio_to_text_request import AudioToTextRequest
from dify_oapi.api.chat.v1.model.audio_to_text_response import AudioToTextResponse
from dify_oapi.api.chat.v1.model.text_to_audio_request import TextToAudioRequest
from dify_oapi.api.chat.v1.resource.audio import Audio
from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.raw_response import RawResponse
from dify_oapi.core.model.request_option import RequestOption


class TestAudioResource:
    @pytest.fixture
    def audio_resource(self):
        config = Config()
        return Audio(config)

    @pytest.fixture
    def mock_transport(self):
        with patch.object(Transport, "execute") as mock:
            yield mock

    @pytest.fixture
    def mock_atransport(self):
        with patch.object(ATransport, "aexecute") as mock:
            yield mock

    def test_audio_to_text(self, audio_resource, mock_transport):
        """Test audio to text method"""
        request = AudioToTextRequest.builder().build()
        option = RequestOption.builder().build()

        mock_transport.return_value = AudioToTextResponse()
        result = audio_resource.to_text(request, option)

        assert isinstance(result, AudioToTextResponse)
        mock_transport.assert_called_once_with(
            audio_resource.config, request, unmarshal_as=AudioToTextResponse, option=option
        )

    def test_text_to_audio(self, audio_resource, mock_transport):
        """Test text to audio method"""
        request = TextToAudioRequest.builder().build()
        option = RequestOption.builder().build()

        mock_response = RawResponse()
        mock_response.content = b"audio_data"
        mock_transport.return_value = mock_response
        result = audio_resource.to_audio(request, option)

        assert isinstance(result, bytes)
        assert result == b"audio_data"
        mock_transport.assert_called_once_with(audio_resource.config, request, option=option)

    async def test_async_audio_to_text(self, audio_resource, mock_atransport):
        """Test async audio to text method"""
        request = AudioToTextRequest.builder().build()
        option = RequestOption.builder().build()

        mock_atransport.return_value = AudioToTextResponse()
        result = await audio_resource.ato_text(request, option)

        assert isinstance(result, AudioToTextResponse)
        mock_atransport.assert_called_once_with(
            audio_resource.config, request, unmarshal_as=AudioToTextResponse, option=option
        )

    async def test_async_text_to_audio(self, audio_resource, mock_atransport):
        """Test async text to audio method"""
        request = TextToAudioRequest.builder().build()
        option = RequestOption.builder().build()

        mock_response = RawResponse()
        mock_response.content = b"async_audio_data"
        mock_atransport.return_value = mock_response
        result = await audio_resource.ato_audio(request, option)

        assert isinstance(result, bytes)
        assert result == b"async_audio_data"
        mock_atransport.assert_called_once_with(audio_resource.config, request, option=option)

    def test_audio_format_validation(self, audio_resource):
        """Test audio format validation through request building"""
        from dify_oapi.api.chat.v1.model.audio_to_text_request_body import AudioToTextRequestBody

        # Test that request can be built with proper audio file
        file_data = BytesIO(b"fake_audio_content")
        request_body = AudioToTextRequestBody.builder().user("test-user").build()
        request = AudioToTextRequest.builder().file(file_data, "test.mp3").request_body(request_body).build()

        assert request.file is not None
        assert "file" in request.files
        assert request.request_body.user == "test-user"

    def test_text_to_audio_parameters(self, audio_resource):
        """Test text to audio request parameters"""
        from dify_oapi.api.chat.v1.model.text_to_audio_request_body import TextToAudioRequestBody

        # Test with text parameter
        request_body = TextToAudioRequestBody.builder().text("Hello world").user("test-user").build()
        request = TextToAudioRequest.builder().request_body(request_body).build()

        assert request.request_body.text == "Hello world"
        assert request.request_body.user == "test-user"

        # Test with message_id parameter
        request_body = TextToAudioRequestBody.builder().message_id("msg-123").user("test-user").build()
        request = TextToAudioRequest.builder().request_body(request_body).build()

        assert request.request_body.message_id == "msg-123"
        assert request.request_body.user == "test-user"

    def test_file_size_limits(self, audio_resource):
        """Test file size limits handling"""
        from dify_oapi.api.chat.v1.model.audio_to_text_request_body import AudioToTextRequestBody

        # Test with large file data (simulated)
        large_file_data = BytesIO(b"x" * (16 * 1024 * 1024))  # 16MB
        request_body = AudioToTextRequestBody.builder().user("test-user").build()
        request = AudioToTextRequest.builder().file(large_file_data, "large.mp3").request_body(request_body).build()

        # The request should be built successfully, actual size validation happens at transport level
        assert request.file is not None
        assert request.request_body.user == "test-user"

    def test_audio_resource_initialization(self, audio_resource):
        """Test audio resource initialization"""
        assert audio_resource.config is not None
        assert hasattr(audio_resource, "to_text")
        assert hasattr(audio_resource, "ato_text")
        assert hasattr(audio_resource, "to_audio")
        assert hasattr(audio_resource, "ato_audio")

    def test_method_signatures(self, audio_resource):
        """Test method signatures are correct"""
        import inspect

        # Test to_text method signature
        sig = inspect.signature(audio_resource.to_text)
        params = list(sig.parameters.keys())
        assert "request" in params
        assert "option" in params

        # Test to_audio method signature
        sig = inspect.signature(audio_resource.to_audio)
        params = list(sig.parameters.keys())
        assert "request" in params
        assert "option" in params

        # Test async methods exist
        assert hasattr(audio_resource, "ato_text")
        assert hasattr(audio_resource, "ato_audio")
