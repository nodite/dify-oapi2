"""TTS message event data model.

This module defines the data structure for tts_message streaming events.
"""

from pydantic import BaseModel


class TtsMessageData(BaseModel):
    """Data structure for tts_message streaming event."""

    message_id: str
    audio: str  # Base64 encoded audio data
    created_at: int

    @staticmethod
    def builder() -> "TtsMessageDataBuilder":
        """Create a new TtsMessageData builder."""
        return TtsMessageDataBuilder()


class TtsMessageDataBuilder:
    """Builder for TtsMessageData."""

    def __init__(self):
        self._tts_message_data = TtsMessageData(message_id="", audio="", created_at=0)

    def build(self) -> TtsMessageData:
        """Build the TtsMessageData instance."""
        return self._tts_message_data

    def message_id(self, message_id: str) -> "TtsMessageDataBuilder":
        """Set the message ID."""
        self._tts_message_data.message_id = message_id
        return self

    def audio(self, audio: str) -> "TtsMessageDataBuilder":
        """Set the base64 encoded audio data."""
        self._tts_message_data.audio = audio
        return self

    def created_at(self, created_at: int) -> "TtsMessageDataBuilder":
        """Set the creation timestamp."""
        self._tts_message_data.created_at = created_at
        return self
