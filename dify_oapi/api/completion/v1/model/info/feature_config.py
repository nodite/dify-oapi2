from __future__ import annotations

from pydantic import BaseModel


class SuggestedQuestionsAfterAnswerConfig(BaseModel):
    """Configuration for suggested questions after answer feature."""

    enabled: bool

    @staticmethod
    def builder() -> SuggestedQuestionsAfterAnswerConfigBuilder:
        return SuggestedQuestionsAfterAnswerConfigBuilder()


class SuggestedQuestionsAfterAnswerConfigBuilder:
    def __init__(self):
        self._config = SuggestedQuestionsAfterAnswerConfig(enabled=False)

    def build(self) -> SuggestedQuestionsAfterAnswerConfig:
        return self._config

    def enabled(self, enabled: bool) -> SuggestedQuestionsAfterAnswerConfigBuilder:
        self._config.enabled = enabled
        return self


class SpeechToTextConfig(BaseModel):
    """Configuration for speech to text feature."""

    enabled: bool

    @staticmethod
    def builder() -> SpeechToTextConfigBuilder:
        return SpeechToTextConfigBuilder()


class SpeechToTextConfigBuilder:
    def __init__(self):
        self._config = SpeechToTextConfig(enabled=False)

    def build(self) -> SpeechToTextConfig:
        return self._config

    def enabled(self, enabled: bool) -> SpeechToTextConfigBuilder:
        self._config.enabled = enabled
        return self


class RetrieverResourceConfig(BaseModel):
    """Configuration for retriever resource (citation and attribution) feature."""

    enabled: bool

    @staticmethod
    def builder() -> RetrieverResourceConfigBuilder:
        return RetrieverResourceConfigBuilder()


class RetrieverResourceConfigBuilder:
    def __init__(self):
        self._config = RetrieverResourceConfig(enabled=False)

    def build(self) -> RetrieverResourceConfig:
        return self._config

    def enabled(self, enabled: bool) -> RetrieverResourceConfigBuilder:
        self._config.enabled = enabled
        return self


class AnnotationReplyConfig(BaseModel):
    """Configuration for annotation reply feature."""

    enabled: bool

    @staticmethod
    def builder() -> AnnotationReplyConfigBuilder:
        return AnnotationReplyConfigBuilder()


class AnnotationReplyConfigBuilder:
    def __init__(self):
        self._config = AnnotationReplyConfig(enabled=False)

    def build(self) -> AnnotationReplyConfig:
        return self._config

    def enabled(self, enabled: bool) -> AnnotationReplyConfigBuilder:
        self._config.enabled = enabled
        return self
