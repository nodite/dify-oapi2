from pydantic import BaseModel


class BindTagsToDatasetRequestBody(BaseModel):
    target_id: str | None = None
    tag_ids: list[str] | None = None

    @staticmethod
    def builder() -> "BindTagsToDatasetRequestBodyBuilder":
        return BindTagsToDatasetRequestBodyBuilder()


class BindTagsToDatasetRequestBodyBuilder:
    def __init__(self):
        self._bind_tags_to_dataset_request_body = BindTagsToDatasetRequestBody()

    def build(self) -> BindTagsToDatasetRequestBody:
        return self._bind_tags_to_dataset_request_body

    def target_id(self, target_id: str) -> "BindTagsToDatasetRequestBodyBuilder":
        self._bind_tags_to_dataset_request_body.target_id = target_id
        return self

    def tag_ids(self, tag_ids: list[str]) -> "BindTagsToDatasetRequestBodyBuilder":
        self._bind_tags_to_dataset_request_body.tag_ids = tag_ids
        return self
