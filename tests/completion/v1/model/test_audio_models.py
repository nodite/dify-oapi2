from __future__ import annotations

from dify_oapi.api.completion.v1.model.audio.text_to_audio_request import TextToAudioRequest
from dify_oapi.api.completion.v1.model.audio.text_to_audio_request_body import TextToAudioRequestBody
from dify_oapi.api.completion.v1.model.audio.text_to_audio_response import TextToAudioResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestTextToAudioModels:
    """Test TextToAudio API models."""

    def test_request_builder(self) -> None:
        """Test TextToAudioRequest builder pattern."""
        request_body = TextToAudioRequestBody.builder().text("Hello world").user("test-user").build()

        request = TextToAudioRequest.builder().request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/text-to-audio"
        assert request.request_body == request_body
        assert request.body is not None

    def test_request_validation(self) -> None:
        """Test TextToAudioRequest validation."""
        request = TextToAudioRequest.builder().build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/text-to-audio"

    def test_request_body_builder(self) -> None:
        """Test TextToAudioRequestBody builder pattern."""
        # Test with text
        request_body = TextToAudioRequestBody.builder().text("Convert this to audio").user("user-123").build()

        assert request_body.text == "Convert this to audio"
        assert request_body.user == "user-123"
        assert request_body.message_id is None

    def test_request_body_validation(self) -> None:
        """Test TextToAudioRequestBody validation."""
        # Test with message_id
        request_body_msg = TextToAudioRequestBody.builder().message_id("message-456").user("user-123").build()

        assert request_body_msg.message_id == "message-456"
        assert request_body_msg.user == "user-123"
        assert request_body_msg.text is None

        # Test empty request body
        empty_request_body = TextToAudioRequestBody.builder().build()
        assert empty_request_body.text is None
        assert empty_request_body.message_id is None
        assert empty_request_body.user is None

    def test_response_inheritance(self) -> None:
        """Test TextToAudioResponse inherits from BaseResponse."""
        response = TextToAudioResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test TextToAudioResponse data access."""
        response = TextToAudioResponse(content_type="audio/wav", data=b"audio binary data")

        assert response.content_type == "audio/wav"
        assert response.data == b"audio binary data"
