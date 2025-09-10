from io import BytesIO

from dify_oapi.api.chatflow.v1.model.audio_to_text_request import AudioToTextRequest
from dify_oapi.api.chatflow.v1.model.audio_to_text_response import AudioToTextResponse
from dify_oapi.api.chatflow.v1.model.text_to_audio_request import TextToAudioRequest
from dify_oapi.api.chatflow.v1.model.text_to_audio_request_body import TextToAudioRequestBody
from dify_oapi.api.chatflow.v1.model.text_to_audio_response import TextToAudioResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestAudioToTextModels:
    def test_request_builder(self):
        """Test AudioToTextRequest builder pattern"""
        audio_data = BytesIO(b"fake audio data")

        request = AudioToTextRequest.builder().file(audio_data, "test.mp3").user("test-user").build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/audio-to-text"
        assert request.file == audio_data
        assert request.user == "test-user"
        assert "file" in request.files
        assert request.files["file"][0] == "test.mp3"
        assert request.files["file"][1] == audio_data
        assert request.body == {"user": "test-user"}

    def test_request_validation(self):
        """Test AudioToTextRequest field validation"""
        request = AudioToTextRequest.builder().build()

        # Test default values
        assert request.file is None
        assert request.user is None
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/audio-to-text"

    def test_file_upload_handling(self):
        """Test file upload handling with different file names"""
        audio_data = BytesIO(b"test audio")

        # Test with custom file name
        request = AudioToTextRequest.builder().file(audio_data, "custom.wav").build()
        assert request.files["file"][0] == "custom.wav"

        # Test with default file name
        request = AudioToTextRequest.builder().file(audio_data).build()
        assert request.files["file"][0] == "audio"

    def test_response_inheritance(self):
        """Test AudioToTextResponse inherits from BaseResponse"""
        response = AudioToTextResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_builder(self):
        """Test AudioToTextResponse builder pattern"""
        response = AudioToTextResponse.builder().text("Hello world").build()

        assert response.text == "Hello world"

    def test_response_data_access(self):
        """Test AudioToTextResponse data access"""
        response = AudioToTextResponse()
        response.text = "Transcribed text"

        assert response.text == "Transcribed text"


class TestTextToAudioModels:
    def test_request_builder(self):
        """Test TextToAudioRequest builder pattern"""
        request_body = TextToAudioRequestBody.builder().text("Hello world").user("test-user").streaming(False).build()

        request = TextToAudioRequest.builder().request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/text-to-audio"
        assert request.request_body == request_body
        assert request.body is not None

    def test_request_validation(self):
        """Test TextToAudioRequest field validation"""
        request = TextToAudioRequest.builder().build()

        # Test default values
        assert request.request_body is None
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/text-to-audio"

    def test_request_body_builder(self):
        """Test TextToAudioRequestBody builder pattern"""
        request_body = (
            TextToAudioRequestBody.builder()
            .message_id("msg-123")
            .text("Hello world")
            .user("test-user")
            .streaming(True)
            .build()
        )

        assert request_body.message_id == "msg-123"
        assert request_body.text == "Hello world"
        assert request_body.user == "test-user"
        assert request_body.streaming is True

    def test_request_body_validation(self):
        """Test TextToAudioRequestBody field validation"""
        request_body = TextToAudioRequestBody()

        # Test default values
        assert request_body.message_id is None
        assert request_body.text is None
        assert request_body.user is None
        assert request_body.streaming is None

    def test_request_body_message_id_priority(self):
        """Test TextToAudioRequestBody with message_id priority"""
        request_body = TextToAudioRequestBody.builder().message_id("msg-123").user("test-user").build()

        assert request_body.message_id == "msg-123"
        assert request_body.text is None
        assert request_body.user == "test-user"

    def test_request_body_text_input(self):
        """Test TextToAudioRequestBody with text input"""
        request_body = (
            TextToAudioRequestBody.builder().text("Convert this to speech").user("test-user").streaming(False).build()
        )

        assert request_body.message_id is None
        assert request_body.text == "Convert this to speech"
        assert request_body.user == "test-user"
        assert request_body.streaming is False

    def test_response_inheritance(self):
        """Test TextToAudioResponse inherits from BaseResponse"""
        response = TextToAudioResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_builder(self):
        """Test TextToAudioResponse builder pattern"""
        response = TextToAudioResponse.builder().build()
        assert isinstance(response, TextToAudioResponse)
        assert isinstance(response, BaseResponse)

    def test_binary_response_handling(self):
        """Test TextToAudioResponse handles binary data"""
        response = TextToAudioResponse()

        # Binary audio data is handled by Transport layer
        # Response should inherit BaseResponse properties
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")


class TestTTSModelsIntegration:
    def test_audio_to_text_complete_flow(self):
        """Test complete AudioToText request/response flow"""
        # Create request
        audio_data = BytesIO(b"audio content")
        request = AudioToTextRequest.builder().file(audio_data, "speech.mp3").user("integration-user").build()

        # Verify request structure
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/audio-to-text"
        assert request.files["file"][0] == "speech.mp3"
        assert request.body["user"] == "integration-user"

        # Create response
        response = AudioToTextResponse.builder().text("Transcribed speech content").build()

        # Verify response structure
        assert response.text == "Transcribed speech content"
        assert isinstance(response, BaseResponse)

    def test_text_to_audio_complete_flow(self):
        """Test complete TextToAudio request/response flow"""
        # Create request body
        request_body = (
            TextToAudioRequestBody.builder()
            .text("Convert this text to speech")
            .user("integration-user")
            .streaming(False)
            .build()
        )

        # Create request
        request = TextToAudioRequest.builder().request_body(request_body).build()

        # Verify request structure
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/text-to-audio"
        assert request.request_body.text == "Convert this text to speech"
        assert request.request_body.user == "integration-user"
        assert request.request_body.streaming is False

        # Create response
        response = TextToAudioResponse.builder().build()

        # Verify response structure
        assert isinstance(response, BaseResponse)

    def test_audio_format_support(self):
        """Test support for different audio formats"""
        formats = ["mp3", "wav", "m4a", "webm", "mp4", "mpeg", "mpga"]

        for format_ext in formats:
            audio_data = BytesIO(f"fake {format_ext} data".encode())
            request = AudioToTextRequest.builder().file(audio_data, f"test.{format_ext}").user("test-user").build()

            assert request.files["file"][0] == f"test.{format_ext}"
            assert request.files["file"][1] == audio_data

    def test_streaming_support(self):
        """Test streaming support for text-to-audio"""
        # Test streaming enabled
        request_body = (
            TextToAudioRequestBody.builder().text("Stream this audio").user("test-user").streaming(True).build()
        )
        assert request_body.streaming is True

        # Test streaming disabled
        request_body = (
            TextToAudioRequestBody.builder().text("Don't stream this audio").user("test-user").streaming(False).build()
        )
        assert request_body.streaming is False
