from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.get_text_embedding_models_request import GetTextEmbeddingModelsRequest
from ..model.get_text_embedding_models_response import GetTextEmbeddingModelsResponse


class Model:
    def __init__(self, config: Config):
        self.config = config

    def embedding_models(
        self, request: GetTextEmbeddingModelsRequest, request_option: RequestOption
    ) -> GetTextEmbeddingModelsResponse:
        return Transport.execute(
            self.config, request, unmarshal_as=GetTextEmbeddingModelsResponse, option=request_option
        )

    async def aembedding_models(
        self, request: GetTextEmbeddingModelsRequest, request_option: RequestOption
    ) -> GetTextEmbeddingModelsResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetTextEmbeddingModelsResponse, option=request_option
        )
