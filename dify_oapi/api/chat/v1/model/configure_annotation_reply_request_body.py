from __future__ import annotations

from pydantic import BaseModel, Field


class ConfigureAnnotationReplyRequestBody(BaseModel):
    """Request body for configuring annotation reply settings."""

    embedding_provider_name: str | None = Field(None, description="Specified embedding model provider name (Optional)")
    embedding_model_name: str | None = Field(None, description="Specified embedding model name (Optional)")
    score_threshold: float = Field(..., description="Similarity threshold for matching annotated replies")

    @classmethod
    def builder(cls) -> ConfigureAnnotationReplyRequestBodyBuilder:
        """Create a ConfigureAnnotationReplyRequestBody builder."""
        return ConfigureAnnotationReplyRequestBodyBuilder()


class ConfigureAnnotationReplyRequestBodyBuilder:
    """Builder for ConfigureAnnotationReplyRequestBody."""

    def __init__(self) -> None:
        self._configure_annotation_reply_request_body = ConfigureAnnotationReplyRequestBody(score_threshold=0.0)

    def embedding_provider_name(
        self, embedding_provider_name: str | None
    ) -> ConfigureAnnotationReplyRequestBodyBuilder:
        """Set embedding provider name."""
        self._configure_annotation_reply_request_body.embedding_provider_name = embedding_provider_name
        return self

    def embedding_model_name(self, embedding_model_name: str | None) -> ConfigureAnnotationReplyRequestBodyBuilder:
        """Set embedding model name."""
        self._configure_annotation_reply_request_body.embedding_model_name = embedding_model_name
        return self

    def score_threshold(self, score_threshold: float) -> ConfigureAnnotationReplyRequestBodyBuilder:
        """Set similarity threshold."""
        self._configure_annotation_reply_request_body.score_threshold = score_threshold
        return self

    def build(self) -> ConfigureAnnotationReplyRequestBody:
        """Build the ConfigureAnnotationReplyRequestBody instance."""
        return self._configure_annotation_reply_request_body
