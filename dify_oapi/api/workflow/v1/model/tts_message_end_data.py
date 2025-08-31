"""TTS message end event data model.

This module defines the data structure for tts_message_end streaming events.
"""

from pydantic import BaseModel


class TtsMessageEndData(BaseModel):
    """Data structure for tts_message_end streaming event."""

    message_id: str
    audio: str  # Empty string for end event
    created_at: int

    @staticmethod
    def builder() -> "TtsMessageEndDataBuilder":
        """Create a new TtsMessageEndData builder."""
        return TtsMessageEndDataBuilder()


class TtsMessageEndDataBuilder:
    """Builder for TtsMessageEndData."""

    def __init__(self):
        self._tts_message_end_data = TtsMessageEndData(message_id="", audio="", created_at=0)

    def build(self) -> TtsMessageEndData:
        """Build the TtsMessageEndData instance."""
        return self._tts_message_end_data

    def message_id(self, message_id: str) -> "TtsMessageEndDataBuilder":
        """Set the message ID."""
        self._tts_message_end_data.message_id = message_id
        return self

    def audio(self, audio: str) -> "TtsMessageEndDataBuilder":
        """Set the audio data (empty for end event)."""
        self._tts_message_end_data.audio = audio
        return self

    def created_at(self, created_at: int) -> "TtsMessageEndDataBuilder":
        """Set the creation timestamp."""
        self._tts_message_end_data.created_at = created_at
        return self
