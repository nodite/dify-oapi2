from __future__ import annotations

from typing import Optional
from dify_oapi.core.model.base_response import BaseResponse


class ToggleBuiltinResponse(BaseResponse):
    result: Optional[str] = None