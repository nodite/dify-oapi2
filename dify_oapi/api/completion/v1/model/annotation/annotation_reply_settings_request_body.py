from __future__ import annotations

from pydantic import BaseModel


class AnnotationReplySettingsRequestBody(BaseModel):
    embedding_provider_name: str | None = None
    embedding_model_name: str | None = None
    score_threshold: float | None = None

    @staticmethod
    def builder() -> AnnotationReplySettingsRequestBodyBuilder:
        return AnnotationReplySettingsRequestBodyBuilder()


class AnnotationReplySettingsRequestBodyBuilder:
    def __init__(self):
        self._annotation_reply_settings_request_body = AnnotationReplySettingsRequestBody()

    def build(self) -> AnnotationReplySettingsRequestBody:
        return self._annotation_reply_settings_request_body

    def embedding_provider_name(self, embedding_provider_name: str) -> AnnotationReplySettingsRequestBodyBuilder:
        self._annotation_reply_settings_request_body.embedding_provider_name = embedding_provider_name
        return self

    def embedding_model_name(self, embedding_model_name: str) -> AnnotationReplySettingsRequestBodyBuilder:
        self._annotation_reply_settings_request_body.embedding_model_name = embedding_model_name
        return self

    def score_threshold(self, score_threshold: float) -> AnnotationReplySettingsRequestBodyBuilder:
        self._annotation_reply_settings_request_body.score_threshold = score_threshold
        return self
