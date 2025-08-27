from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse


class PreviewFileResponse(BaseResponse):
    content_type: str | None = None
    content_length: int | None = None
    content: bytes | None = None
