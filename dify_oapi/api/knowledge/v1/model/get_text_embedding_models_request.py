from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetTextEmbeddingModelsRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> "GetTextEmbeddingModelsRequestBuilder":
        return GetTextEmbeddingModelsRequestBuilder()


class GetTextEmbeddingModelsRequestBuilder:
    def __init__(self):
        get_text_embedding_models_request = GetTextEmbeddingModelsRequest()
        get_text_embedding_models_request.http_method = HttpMethod.GET
        get_text_embedding_models_request.uri = "/v1/workspaces/current/models/model-types/text-embedding"
        self._get_text_embedding_models_request = get_text_embedding_models_request

    def build(self) -> GetTextEmbeddingModelsRequest:
        return self._get_text_embedding_models_request
