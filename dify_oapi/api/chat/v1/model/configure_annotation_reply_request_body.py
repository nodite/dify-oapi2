from __future__ import annotations

from pydantic import BaseModel


class ConfigureAnnotationReplyRequestBody(BaseModel):
    """Request body for configuring annotation reply settings."""

    embedding_provider_name: str | None = None
    embedding_model_name: str | None = None
    score_threshold: float = 0.0

    @staticmethod
    def builder() -> ConfigureAnnotationReplyRequestBodyBuilder:
        return ConfigureAnnotationReplyRequestBodyBuilder()


class ConfigureAnnotationReplyRequestBodyBuilder:
    """Builder for ConfigureAnnotationReplyRequestBody."""

    def __init__(self):
        self._configure_annotation_reply_request_body = ConfigureAnnotationReplyRequestBody()

    def build(self) -> ConfigureAnnotationReplyRequestBody:
        return self._configure_annotation_reply_request_body

    def embedding_provider_name(
        self, embedding_provider_name: str | None
    ) -> ConfigureAnnotationReplyRequestBodyBuilder:
        self._configure_annotation_reply_request_body.embedding_provider_name = embedding_provider_name
        return self

    def embedding_model_name(self, embedding_model_name: str | None) -> ConfigureAnnotationReplyRequestBodyBuilder:
        self._configure_annotation_reply_request_body.embedding_model_name = embedding_model_name
        return self

    def score_threshold(self, score_threshold: float) -> ConfigureAnnotationReplyRequestBodyBuilder:
        self._configure_annotation_reply_request_body.score_threshold = score_threshold
        return self
