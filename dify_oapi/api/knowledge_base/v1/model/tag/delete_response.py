from __future__ import annotations

from pydantic import BaseModel


class DeleteTagResponse(BaseModel):
    result: str

    @staticmethod
    def builder() -> DeleteTagResponseBuilder:
        return DeleteTagResponseBuilder()


class DeleteTagResponseBuilder:
    def __init__(self):
        self._response = DeleteTagResponse(result="")

    def build(self) -> DeleteTagResponse:
        return self._response

    def result(self, result: str) -> DeleteTagResponseBuilder:
        self._response.result = result
        return self