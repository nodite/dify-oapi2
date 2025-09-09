from io import BytesIO

import pytest

from dify_oapi.api.chatflow.v1.model.audio_to_text_request import AudioToTextRequest
from dify_oapi.api.chatflow.v1.model.audio_to_text_response import AudioToTextResponse
from dify_oapi.api.chatflow.v1.model.text_to_audio_request import TextToAudioRequest
from dify_oapi.api.chatflow.v1.model.text_to_audio_request_body import TextToAudioRequestBody
from dify_oapi.api.chatflow.v1.model.text_to_audio_response import TextToAudioResponse
from dify_oapi.api.chatflow.v1.resource.tts import TTS
from dify_oapi.core.http.transport.async_transport import ATransport
from dify_oapi.core.http.transport.sync_transport import Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestTTSResource:
    def setup_method(self):
        """Setup test fixtures"""
        self.config = Config()
        self.tts = TTS(self.config)
        self.request_option = RequestOption.builder().api_key("test-api-key").build()

    def test_tts_initialization(self):
        """Test TTS resource initialization"""
        assert self.tts.config == self.config
        assert isinstance(self.tts, TTS)

    def test_speech_to_text_sync(self, mocker):
        """Test speech_to_text method (sync)"""
        # Mock Transport.execute
        mock_execute = mocker.patch.object(Transport, "execute")
        mock_response = AudioToTextResponse.builder().text("Transcribed text").build()
        mock_execute.return_value = mock_response

        # Create request
        audio_data = BytesIO(b"fake audio data")
        request = AudioToTextRequest.builder().file(audio_data, "test.mp3").user("test-user").build()

        # Execute method
        response = self.tts.speech_to_text(request, self.request_option)

        # Verify call
        mock_execute.assert_called_once_with(
            self.config, request, unmarshal_as=AudioToTextResponse, option=self.request_option
        )
        assert response == mock_response

    @pytest.mark.asyncio
    async def test_speech_to_text_async(self, mocker):
        """Test aspeech_to_text method (async)"""
        # Mock ATransport.aexecute
        mock_aexecute = mocker.patch.object(ATransport, "aexecute")
        mock_response = AudioToTextResponse.builder().text("Transcribed text").build()
        mock_aexecute.return_value = mock_response

        # Create request
        audio_data = BytesIO(b"fake audio data")
        request = AudioToTextRequest.builder().file(audio_data, "test.mp3").user("test-user").build()

        # Execute method
        response = await self.tts.aspeech_to_text(request, self.request_option)

        # Verify call
        mock_aexecute.assert_called_once_with(
            self.config, request, unmarshal_as=AudioToTextResponse, option=self.request_option
        )
        assert response == mock_response

    def test_text_to_audio_sync(self, mocker):
        """Test text_to_audio method (sync)"""
        # Mock Transport.execute
        mock_execute = mocker.patch.object(Transport, "execute")
        mock_response = TextToAudioResponse.builder().build()
        mock_execute.return_value = mock_response

        # Create request
        request_body = TextToAudioRequestBody.builder().text("Hello world").user("test-user").streaming(False).build()
        request = TextToAudioRequest.builder().request_body(request_body).build()

        # Execute method
        response = self.tts.text_to_audio(request, self.request_option)

        # Verify call
        mock_execute.assert_called_once_with(
            self.config, request, unmarshal_as=TextToAudioResponse, option=self.request_option
        )
        assert response == mock_response

    @pytest.mark.asyncio
    async def test_text_to_audio_async(self, mocker):
        """Test atext_to_audio method (async)"""
        # Mock ATransport.aexecute
        mock_aexecute = mocker.patch.object(ATransport, "aexecute")
        mock_response = TextToAudioResponse.builder().build()
        mock_aexecute.return_value = mock_response

        # Create request
        request_body = TextToAudioRequestBody.builder().text("Hello world").user("test-user").streaming(False).build()
        request = TextToAudioRequest.builder().request_body(request_body).build()

        # Execute method
        response = await self.tts.atext_to_audio(request, self.request_option)

        # Verify call
        mock_aexecute.assert_called_once_with(
            self.config, request, unmarshal_as=TextToAudioResponse, option=self.request_option
        )
        assert response == mock_response

    def test_speech_to_text_with_different_audio_formats(self, mocker):
        """Test speech_to_text with different audio formats"""
        # Mock Transport.execute
        mock_execute = mocker.patch.object(Transport, "execute")
        mock_response = AudioToTextResponse.builder().text("Transcribed text").build()
        mock_execute.return_value = mock_response

        formats = ["mp3", "wav", "m4a", "webm", "mp4", "mpeg", "mpga"]

        for format_ext in formats:
            audio_data = BytesIO(f"fake {format_ext} data".encode())
            request = AudioToTextRequest.builder().file(audio_data, f"test.{format_ext}").user("test-user").build()

            response = self.tts.speech_to_text(request, self.request_option)

            assert response == mock_response

    def test_text_to_audio_with_message_id(self, mocker):
        """Test text_to_audio with message_id instead of text"""
        # Mock Transport.execute
        mock_execute = mocker.patch.object(Transport, "execute")
        mock_response = TextToAudioResponse.builder().build()
        mock_execute.return_value = mock_response

        # Create request with message_id
        request_body = TextToAudioRequestBody.builder().message_id("msg-123").user("test-user").build()
        request = TextToAudioRequest.builder().request_body(request_body).build()

        # Execute method
        response = self.tts.text_to_audio(request, self.request_option)

        # Verify call
        mock_execute.assert_called_once_with(
            self.config, request, unmarshal_as=TextToAudioResponse, option=self.request_option
        )
        assert response == mock_response

    def test_text_to_audio_streaming_mode(self, mocker):
        """Test text_to_audio with streaming enabled"""
        # Mock Transport.execute
        mock_execute = mocker.patch.object(Transport, "execute")
        mock_response = TextToAudioResponse.builder().build()
        mock_execute.return_value = mock_response

        # Create request with streaming enabled
        request_body = (
            TextToAudioRequestBody.builder().text("Stream this audio").user("test-user").streaming(True).build()
        )
        request = TextToAudioRequest.builder().request_body(request_body).build()

        # Execute method
        response = self.tts.text_to_audio(request, self.request_option)

        # Verify call
        mock_execute.assert_called_once_with(
            self.config, request, unmarshal_as=TextToAudioResponse, option=self.request_option
        )
        assert response == mock_response

    def test_speech_to_text_error_handling(self, mocker):
        """Test speech_to_text error handling"""
        # Mock Transport.execute to raise exception
        mock_execute = mocker.patch.object(Transport, "execute")
        mock_execute.side_effect = Exception("API Error")

        # Create request
        audio_data = BytesIO(b"fake audio data")
        request = AudioToTextRequest.builder().file(audio_data, "test.mp3").user("test-user").build()

        # Execute method and expect exception
        with pytest.raises(Exception, match="API Error"):
            self.tts.speech_to_text(request, self.request_option)

    @pytest.mark.asyncio
    async def test_text_to_audio_async_error_handling(self, mocker):
        """Test atext_to_audio error handling"""
        # Mock ATransport.aexecute to raise exception
        mock_aexecute = mocker.patch.object(ATransport, "aexecute")
        mock_aexecute.side_effect = Exception("Async API Error")

        # Create request
        request_body = TextToAudioRequestBody.builder().text("Hello world").user("test-user").build()
        request = TextToAudioRequest.builder().request_body(request_body).build()

        # Execute method and expect exception
        with pytest.raises(Exception, match="Async API Error"):
            await self.tts.atext_to_audio(request, self.request_option)


class TestTTSResourceIntegration:
    def setup_method(self):
        """Setup test fixtures"""
        self.config = Config()
        self.tts = TTS(self.config)
        self.request_option = RequestOption.builder().api_key("test-api-key").build()

    def test_complete_speech_to_text_flow(self, mocker):
        """Test complete speech-to-text workflow"""
        # Mock Transport.execute
        mock_execute = mocker.patch.object(Transport, "execute")
        mock_response = AudioToTextResponse.builder().text("Hello, this is a test transcription").build()
        mock_execute.return_value = mock_response

        # Create audio file
        audio_data = BytesIO(b"fake audio content for transcription")
        request = AudioToTextRequest.builder().file(audio_data, "speech.mp3").user("integration-user").build()

        # Execute speech-to-text
        response = self.tts.speech_to_text(request, self.request_option)

        # Verify response
        assert response.text == "Hello, this is a test transcription"
        assert isinstance(response, AudioToTextResponse)

    @pytest.mark.asyncio
    async def test_complete_text_to_audio_flow(self, mocker):
        """Test complete text-to-audio workflow"""
        # Mock ATransport.aexecute
        mock_aexecute = mocker.patch.object(ATransport, "aexecute")
        mock_response = TextToAudioResponse.builder().build()
        mock_aexecute.return_value = mock_response

        # Create text-to-audio request
        request_body = (
            TextToAudioRequestBody.builder()
            .text("Convert this text to speech for integration testing")
            .user("integration-user")
            .streaming(False)
            .build()
        )
        request = TextToAudioRequest.builder().request_body(request_body).build()

        # Execute text-to-audio
        response = await self.tts.atext_to_audio(request, self.request_option)

        # Verify response
        assert isinstance(response, TextToAudioResponse)

    def test_tts_round_trip_simulation(self, mocker):
        """Test simulated round-trip: text -> audio -> text"""
        # Mock both operations
        mock_execute = mocker.patch.object(Transport, "execute")

        # First call: text-to-audio
        audio_response = TextToAudioResponse.builder().build()
        mock_execute.return_value = audio_response

        request_body = TextToAudioRequestBody.builder().text("Round trip test").user("test-user").build()
        text_to_audio_request = TextToAudioRequest.builder().request_body(request_body).build()

        audio_result = self.tts.text_to_audio(text_to_audio_request, self.request_option)
        assert isinstance(audio_result, TextToAudioResponse)

        # Second call: audio-to-text (simulated)
        text_response = AudioToTextResponse.builder().text("Round trip test").build()
        mock_execute.return_value = text_response

        audio_data = BytesIO(b"simulated audio data")
        audio_to_text_request = AudioToTextRequest.builder().file(audio_data, "roundtrip.mp3").user("test-user").build()

        text_result = self.tts.speech_to_text(audio_to_text_request, self.request_option)
        assert text_result.text == "Round trip test"

    def test_tts_resource_method_accessibility(self):
        """Test all TTS resource methods are accessible"""
        # Verify all expected methods exist
        assert hasattr(self.tts, "speech_to_text")
        assert hasattr(self.tts, "aspeech_to_text")
        assert hasattr(self.tts, "text_to_audio")
        assert hasattr(self.tts, "atext_to_audio")

        # Verify methods are callable
        assert callable(self.tts.speech_to_text)
        assert callable(self.tts.aspeech_to_text)
        assert callable(self.tts.text_to_audio)
        assert callable(self.tts.atext_to_audio)
