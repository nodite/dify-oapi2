"""Text chunk event data model.

This module defines the data structure for text_chunk streaming events.
"""

from pydantic import BaseModel


class TextChunkData(BaseModel):
    """Data structure for text_chunk streaming event."""

    text: str
    from_variable_selector: list[str]

    @staticmethod
    def builder() -> "TextChunkDataBuilder":
        """Create a new TextChunkData builder."""
        return TextChunkDataBuilder()


class TextChunkDataBuilder:
    """Builder for TextChunkData."""

    def __init__(self):
        self._text_chunk_data = TextChunkData(text="", from_variable_selector=[])

    def build(self) -> TextChunkData:
        """Build the TextChunkData instance."""
        return self._text_chunk_data

    def text(self, text: str) -> "TextChunkDataBuilder":
        """Set the text chunk."""
        self._text_chunk_data.text = text
        return self

    def from_variable_selector(self, from_variable_selector: list[str]) -> "TextChunkDataBuilder":
        """Set the variable selector path."""
        self._text_chunk_data.from_variable_selector = from_variable_selector
        return self
