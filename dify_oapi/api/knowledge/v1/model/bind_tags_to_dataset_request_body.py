from pydantic import BaseModel


class BindTagsToDatasetRequestBody(BaseModel):
    dataset_id: str | None = None
    tag_ids: list[str] | None = None

    @staticmethod
    def builder() -> "BindTagsToDatasetRequestBodyBuilder":
        return BindTagsToDatasetRequestBodyBuilder()


class BindTagsToDatasetRequestBodyBuilder:
    def __init__(self):
        self._bind_tags_to_dataset_request_body = BindTagsToDatasetRequestBody()

    def build(self) -> BindTagsToDatasetRequestBody:
        return self._bind_tags_to_dataset_request_body

    def dataset_id(self, dataset_id: str) -> "BindTagsToDatasetRequestBodyBuilder":
        self._bind_tags_to_dataset_request_body.dataset_id = dataset_id
        return self

    def tag_ids(self, tag_ids: list[str]) -> "BindTagsToDatasetRequestBodyBuilder":
        self._bind_tags_to_dataset_request_body.tag_ids = tag_ids
        return self
