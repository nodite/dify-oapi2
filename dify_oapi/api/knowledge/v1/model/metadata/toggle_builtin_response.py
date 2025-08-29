from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse


class ToggleBuiltinResponse(BaseResponse):
    result: str | None = None
