"""Tests for Audio Processing API models."""

from io import BytesIO

import pytest

from dify_oapi.api.chat.v1.model.audio_to_text_request import AudioToTextRequest
from dify_oapi.api.chat.v1.model.audio_to_text_request_body import AudioToTextRequestBody
from dify_oapi.api.chat.v1.model.audio_to_text_response import AudioToTextResponse
from dify_oapi.api.chat.v1.model.text_to_audio_request import TextToAudioRequest
from dify_oapi.api.chat.v1.model.text_to_audio_request_body import TextToAudioRequestBody
from dify_oapi.api.chat.v1.model.text_to_audio_response import TextToAudioResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestAudioToTextModels:
    """Test audio-to-text API models."""

    def test_audio_to_text_request_builder(self):
        """Test AudioToTextRequest builder pattern."""
        request_body = AudioToTextRequestBody.builder().user("test-user").build()
        file_data = BytesIO(b"test audio content")
        request = AudioToTextRequest.builder().request_body(request_body).file(file_data, "test.mp3").build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/audio-to-text"
        assert request.request_body.user == "test-user"
        assert request.file is not None
        assert "file" in request.files

    def test_audio_to_text_request_body_validation(self):
        """Test AudioToTextRequestBody field validation."""
        # Test required user field
        body = AudioToTextRequestBody.builder().user("test-user").build()
        assert body.user == "test-user"

        # Test user field is required
        with pytest.raises(ValueError):
            AudioToTextRequestBody(user=None)

    def test_audio_to_text_response_inheritance(self):
        """Test AudioToTextResponse inherits from BaseResponse."""
        response = AudioToTextResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")

    def test_audio_file_upload_functionality(self):
        """Test audio file upload functionality."""
        file_data = BytesIO(b"mock audio data")
        request_body = AudioToTextRequestBody.builder().user("test-user").build()
        request = AudioToTextRequest.builder().request_body(request_body).file(file_data, "test.wav").build()

        assert request.files["file"][0] == "test.wav"
        assert request.files["file"][1] == file_data

    def test_supported_audio_format_validation(self):
        """Test supported audio format validation."""
        # This test verifies that the model accepts various audio formats
        supported_formats = ["mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"]

        for format_ext in supported_formats:
            file_data = BytesIO(b"test audio content")
            request_body = AudioToTextRequestBody.builder().user("test-user").build()
            request = (
                AudioToTextRequest.builder().request_body(request_body).file(file_data, f"test.{format_ext}").build()
            )
            assert request.files["file"][0] == f"test.{format_ext}"


class TestTextToAudioModels:
    """Test text-to-audio API models."""

    def test_text_to_audio_request_builder(self):
        """Test TextToAudioRequest builder pattern."""
        request_body = TextToAudioRequestBody.builder().text("Hello world").user("test-user").build()
        request = TextToAudioRequest.builder().request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/text-to-audio"
        assert request.request_body.text == "Hello world"
        assert request.request_body.user == "test-user"

    def test_text_to_audio_request_body_validation(self):
        """Test TextToAudioRequestBody field validation."""
        # Test with text field
        body = TextToAudioRequestBody.builder().text("Hello world").user("test-user").build()
        assert body.text == "Hello world"
        assert body.user == "test-user"
        assert body.message_id is None

        # Test with message_id field
        body = TextToAudioRequestBody.builder().message_id("msg-123").user("test-user").build()
        assert body.message_id == "msg-123"
        assert body.user == "test-user"
        assert body.text is None

        # Test user field is required
        with pytest.raises(ValueError):
            TextToAudioRequestBody(user=None)

    def test_text_to_audio_response_inheritance(self):
        """Test TextToAudioResponse inherits from BaseResponse."""
        response = TextToAudioResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")

    def test_text_to_audio_parameter_validation(self):
        """Test text-to-audio parameter validation."""
        # Test both text and message_id can be optional
        body = TextToAudioRequestBody.builder().user("test-user").build()
        assert body.text is None
        assert body.message_id is None
        assert body.user == "test-user"

    def test_multipart_form_data_handling(self):
        """Test multipart/form-data handling."""
        request_body = TextToAudioRequestBody.builder().text("Test speech content").user("test-user").build()
        request = TextToAudioRequest.builder().request_body(request_body).build()

        # Verify the request body is properly serialized for multipart/form-data
        assert request.body is not None
        assert isinstance(request.body, dict)

    def test_binary_response_handling(self):
        """Test binary response handling."""
        # TextToAudioResponse should be able to handle binary audio data
        response = TextToAudioResponse()

        # The response inherits from BaseResponse which provides error handling
        # The actual binary data would be handled by the transport layer
        assert isinstance(response, BaseResponse)
