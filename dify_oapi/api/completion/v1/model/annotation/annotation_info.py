from __future__ import annotations

from pydantic import BaseModel


class AnnotationInfo(BaseModel):
    id: str | None = None
    question: str | None = None
    answer: str | None = None
    hit_count: int | None = None
    created_at: int | None = None

    @staticmethod
    def builder() -> AnnotationInfoBuilder:
        return AnnotationInfoBuilder()


class AnnotationInfoBuilder:
    def __init__(self):
        self._annotation_info = AnnotationInfo()

    def build(self) -> AnnotationInfo:
        return self._annotation_info

    def id(self, id: str) -> AnnotationInfoBuilder:
        self._annotation_info.id = id
        return self

    def question(self, question: str) -> AnnotationInfoBuilder:
        self._annotation_info.question = question
        return self

    def answer(self, answer: str) -> AnnotationInfoBuilder:
        self._annotation_info.answer = answer
        return self

    def hit_count(self, hit_count: int) -> AnnotationInfoBuilder:
        self._annotation_info.hit_count = hit_count
        return self

    def created_at(self, created_at: int) -> AnnotationInfoBuilder:
        self._annotation_info.created_at = created_at
        return self
