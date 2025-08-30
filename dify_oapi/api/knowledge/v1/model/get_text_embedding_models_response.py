from dify_oapi.core.model.base_response import BaseResponse

from .model_info import ModelInfo


class GetTextEmbeddingModelsResponse(BaseResponse):
    data: list[ModelInfo] | None = None
