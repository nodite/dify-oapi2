from __future__ import annotations

from pydantic import BaseModel


class DeleteMetadataResponse(BaseModel):
    """Empty response for 204 No Content"""

    @staticmethod
    def builder() -> DeleteMetadataResponseBuilder:
        return DeleteMetadataResponseBuilder()


class DeleteMetadataResponseBuilder:
    def __init__(self):
        self._response = DeleteMetadataResponse()

    def build(self) -> DeleteMetadataResponse:
        return self._response