import os

from dify_oapi.api.chat.v1.model.get_conversations_request import GetConversationsRequest
from dify_oapi.api.chat.v1.model.message_history_request import GetMessageHistoryRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def main():
    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
    api_key = os.getenv("CHAT_KEY")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")
    req_option = RequestOption.builder().api_key(api_key).build()

    # Get conversation list
    conv_req = GetConversationsRequest.builder().build()
    conv_response = client.chat.v1.conversation.list(conv_req, req_option)

    if conv_response.data and len(conv_response.data) > 0:
        conversation_id = conv_response.data[0].id

        # Get message history for a conversation
        history_req = GetMessageHistoryRequest.builder().conversation_id(conversation_id).build()
        history_response = client.chat.v1.conversation.history(history_req, req_option)

        for message in history_response.data:
            print(f"Role: {message.role}, Content: {message.content}")


if __name__ == "__main__":
    main()
