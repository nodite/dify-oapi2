from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.delete_conversation_request import DeleteConversationRequest
from ..model.delete_conversation_response import DeleteConversationResponse
from ..model.get_conversation_messages_request import GetConversationMessagesRequest
from ..model.get_conversation_messages_response import GetConversationMessagesResponse
from ..model.get_conversation_variables_request import GetConversationVariablesRequest
from ..model.get_conversation_variables_response import GetConversationVariablesResponse
from ..model.get_conversations_request import GetConversationsRequest
from ..model.get_conversations_response import GetConversationsResponse
from ..model.rename_conversation_request import RenameConversationRequest
from ..model.rename_conversation_response import RenameConversationResponse


class Conversation:
    def __init__(self, config: Config) -> None:
        self.config = config

    def messages(
        self, request: GetConversationMessagesRequest, request_option: RequestOption
    ) -> GetConversationMessagesResponse:
        return Transport.execute(
            self.config, request, unmarshal_as=GetConversationMessagesResponse, option=request_option
        )

    async def amessages(
        self, request: GetConversationMessagesRequest, request_option: RequestOption
    ) -> GetConversationMessagesResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetConversationMessagesResponse, option=request_option
        )

    def list(self, request: GetConversationsRequest, request_option: RequestOption) -> GetConversationsResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetConversationsResponse, option=request_option)

    async def alist(self, request: GetConversationsRequest, request_option: RequestOption) -> GetConversationsResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetConversationsResponse, option=request_option
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
