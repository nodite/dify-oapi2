"""Ping event data model.

This module defines the data structure for ping streaming events.
"""

from pydantic import BaseModel


class PingData(BaseModel):
    """Data structure for ping streaming event (empty data)."""

    pass

    @staticmethod
    def builder() -> "PingDataBuilder":
        """Create a new PingData builder."""
        return PingDataBuilder()


class PingDataBuilder:
    """Builder for PingData."""

    def __init__(self):
        self._ping_data = PingData()

    def build(self) -> PingData:
        """Build the PingData instance."""
        return self._ping_data
