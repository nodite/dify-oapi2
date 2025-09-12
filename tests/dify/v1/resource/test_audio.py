"""Dify audio resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.dify.v1.resource.audio import Audio


class TestAudio:
    """Test Dify Audio resource."""

    @pytest.fixture
    def audio(self, mock_config):
        """Create Audio instance."""
        return Audio(mock_config)

    def test_to_text(self, audio, request_option):
        """Test speech to text."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(text="transcribed text")
            result = audio.to_text(MagicMock(), request_option)
            assert result.text == "transcribed text"

    def test_from_text(self, audio, request_option):
        """Test text to audio."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(audio_url="http://example.com/audio.mp3")
            result = audio.from_text(MagicMock(), request_option)
            assert result.audio_url == "http://example.com/audio.mp3"
