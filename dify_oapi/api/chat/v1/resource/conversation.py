from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.delete_conversation_request import DeleteConversationRequest
from ..model.delete_conversation_response import DeleteConversationResponse
from ..model.get_conversation_list_request import GetConversationsListRequest
from ..model.get_conversation_list_response import GetConversationsResponse
from ..model.get_conversation_variables_request import GetConversationVariablesRequest
from ..model.get_conversation_variables_response import GetConversationVariablesResponse
from ..model.message_history_request import GetMessageHistoryRequest
from ..model.message_history_response import GetMessageHistoryResponse
from ..model.rename_conversation_request import RenameConversationRequest
from ..model.rename_conversation_response import RenameConversationResponse


class Conversation:
    def __init__(self, config: Config) -> None:
        self.config = config

    def list(self, request: GetConversationsListRequest, request_option: RequestOption) -> GetConversationsResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetConversationsResponse, option=request_option)

    async def alist(
        self, request: GetConversationsListRequest, request_option: RequestOption
    ) -> GetConversationsResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetConversationsResponse, option=request_option
        )

    def history(self, request: GetMessageHistoryRequest, request_option: RequestOption) -> GetMessageHistoryResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetMessageHistoryResponse, option=request_option)

    async def ahistory(
        self, request: GetMessageHistoryRequest, request_option: RequestOption
    ) -> GetMessageHistoryResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetMessageHistoryResponse, option=request_option
        )

    def variables(
        self, request: GetConversationVariablesRequest, request_option: RequestOption
    ) -> GetConversationVariablesResponse:
        return Transport.execute(
            self.config, request, unmarshal_as=GetConversationVariablesResponse, option=request_option
        )

    async def avariables(
        self, request: GetConversationVariablesRequest, request_option: RequestOption
    ) -> GetConversationVariablesResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetConversationVariablesResponse, option=request_option
        )

    def delete(self, request: DeleteConversationRequest, request_option: RequestOption) -> DeleteConversationResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteConversationResponse, option=request_option)

    async def adelete(
        self, request: DeleteConversationRequest, request_option: RequestOption
    ) -> DeleteConversationResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=DeleteConversationResponse, option=request_option
        )

    def rename(self, request: RenameConversationRequest, request_option: RequestOption) -> RenameConversationResponse:
        return Transport.execute(self.config, request, unmarshal_as=RenameConversationResponse, option=request_option)

    async def arename(
        self, request: RenameConversationRequest, request_option: RequestOption
    ) -> RenameConversationResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=RenameConversationResponse, option=request_option
        )
