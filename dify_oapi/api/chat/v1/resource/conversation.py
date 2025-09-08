from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.delete_conversation_request import DeleteConversationRequest
from ..model.delete_conversation_response import DeleteConversationResponse
from ..model.get_conversation_list_request import GetConversationsRequest
from ..model.get_conversation_list_response import GetConversationsResponse
from ..model.get_conversation_variables_request import GetConversationVariablesRequest
from ..model.get_conversation_variables_response import GetConversationVariablesResponse
from ..model.message_history_request import GetMessageHistoryRequest
from ..model.message_history_response import GetMessageHistoryResponse
from ..model.rename_conversation_request import RenameConversationRequest
from ..model.rename_conversation_response import RenameConversationResponse


class Conversation:
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def list(self, request: GetConversationsRequest, option: RequestOption | None = None) -> GetConversationsResponse:
        # Send request
        return Transport.execute(
            self.config,
            request,
            unmarshal_as=GetConversationsResponse,
            option=option,
        )

    async def alist(
        self, request: GetConversationsRequest, option: RequestOption | None = None
    ) -> GetConversationsResponse:
        # Send request
        return await ATransport.aexecute(
            self.config,
            request,
            unmarshal_as=GetConversationsResponse,
            option=option,
        )

    def history(
        self, request: GetMessageHistoryRequest, option: RequestOption | None = None
    ) -> GetMessageHistoryResponse:
        # Send request
        return Transport.execute(
            self.config,
            request,
            unmarshal_as=GetMessageHistoryResponse,
            option=option,
        )

    async def ahistory(
        self, request: GetMessageHistoryRequest, option: RequestOption | None = None
    ) -> GetMessageHistoryResponse:
        # Send request
        return await ATransport.aexecute(
            self.config,
            request,
            unmarshal_as=GetMessageHistoryResponse,
            option=option,
        )

    def variables(
        self, request: GetConversationVariablesRequest, option: RequestOption | None = None
    ) -> GetConversationVariablesResponse:
        # Send request
        return Transport.execute(
            self.config,
            request,
            unmarshal_as=GetConversationVariablesResponse,
            option=option,
        )

    async def avariables(
        self, request: GetConversationVariablesRequest, option: RequestOption | None = None
    ) -> GetConversationVariablesResponse:
        # Send request
        return await ATransport.aexecute(
            self.config,
            request,
            unmarshal_as=GetConversationVariablesResponse,
            option=option,
        )

    def delete(
        self, request: DeleteConversationRequest, option: RequestOption | None = None
    ) -> DeleteConversationResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteConversationResponse, option=option)

    async def adelete(
        self, request: DeleteConversationRequest, option: RequestOption | None = None
    ) -> DeleteConversationResponse:
        # Send request
        return await ATransport.aexecute(self.config, request, unmarshal_as=DeleteConversationResponse, option=option)

    def rename(
        self, request: RenameConversationRequest, option: RequestOption | None = None
    ) -> RenameConversationResponse:
        return Transport.execute(self.config, request, unmarshal_as=RenameConversationResponse, option=option)

    async def arename(
        self, request: RenameConversationRequest, option: RequestOption | None = None
    ) -> RenameConversationResponse:
        # Send request
        return await ATransport.aexecute(self.config, request, unmarshal_as=RenameConversationResponse, option=option)
