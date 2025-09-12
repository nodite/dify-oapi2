from __future__ import annotations

from pydantic import BaseModel

from dify_oapi.core.model.base_response import BaseResponse

from .retriever_resource import RetrieverResource
from .usage_info import UsageInfo


class ChatResponse(BaseResponse):
    """Chat response model."""

    event: str | None = None
    task_id: str | None = None
    id: str | None = None
    message_id: str | None = None
    conversation_id: str | None = None
    mode: str | None = None
    answer: str | None = None
    metadata: ChatResponseMetadata | None = None
    created_at: int | None = None


class ChatResponseMetadata(BaseModel):
    """Chat response metadata model."""

    annotation_reply: str | None = None
    usage: UsageInfo | None = None
    retriever_resources: list[RetrieverResource] | None = None
