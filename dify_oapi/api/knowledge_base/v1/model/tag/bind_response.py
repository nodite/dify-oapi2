from __future__ import annotations

from typing import Optional
from dify_oapi.core.model.base_response import BaseResponse


class BindResponse(BaseResponse):
    result: Optional[str] = None