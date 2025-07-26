from __future__ import annotations

from pydantic import BaseModel


class DeleteResponse(BaseModel):
    """Empty response for 204 No Content"""

    @staticmethod
    def builder() -> DeleteResponseBuilder:
        return DeleteResponseBuilder()


class DeleteResponseBuilder:
    def __init__(self):
        self._response = DeleteResponse()

    def build(self) -> DeleteResponse:
        return self._response