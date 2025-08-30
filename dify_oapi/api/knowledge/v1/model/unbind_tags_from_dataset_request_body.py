from pydantic import BaseModel


class UnbindTagsFromDatasetRequestBody(BaseModel):
    target_id: str | None = None
    tag_id: str | None = None

    @staticmethod
    def builder() -> "UnbindTagsFromDatasetRequestBodyBuilder":
        return UnbindTagsFromDatasetRequestBodyBuilder()


class UnbindTagsFromDatasetRequestBodyBuilder:
    def __init__(self):
        self._unbind_tags_from_dataset_request_body = UnbindTagsFromDatasetRequestBody()

    def build(self) -> UnbindTagsFromDatasetRequestBody:
        return self._unbind_tags_from_dataset_request_body

    def target_id(self, target_id: str) -> "UnbindTagsFromDatasetRequestBodyBuilder":
        self._unbind_tags_from_dataset_request_body.target_id = target_id
        return self

    def tag_id(self, tag_id: str) -> "UnbindTagsFromDatasetRequestBodyBuilder":
        self._unbind_tags_from_dataset_request_body.tag_id = tag_id
        return self
