from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse


class UnbindResponse(BaseResponse):
    result: str | None = None
