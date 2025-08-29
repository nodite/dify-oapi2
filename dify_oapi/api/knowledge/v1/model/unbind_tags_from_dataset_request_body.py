from pydantic import BaseModel


class UnbindTagsFromDatasetRequestBody(BaseModel):
    dataset_id: str | None = None
    tag_ids: list[str] | None = None

    @staticmethod
    def builder() -> "UnbindTagsFromDatasetRequestBodyBuilder":
        return UnbindTagsFromDatasetRequestBodyBuilder()


class UnbindTagsFromDatasetRequestBodyBuilder:
    def __init__(self):
        self._unbind_tags_from_dataset_request_body = UnbindTagsFromDatasetRequestBody()

    def build(self) -> UnbindTagsFromDatasetRequestBody:
        return self._unbind_tags_from_dataset_request_body

    def dataset_id(self, dataset_id: str) -> "UnbindTagsFromDatasetRequestBodyBuilder":
        self._unbind_tags_from_dataset_request_body.dataset_id = dataset_id
        return self

    def tag_ids(self, tag_ids: list[str]) -> "UnbindTagsFromDatasetRequestBodyBuilder":
        self._unbind_tags_from_dataset_request_body.tag_ids = tag_ids
        return self
