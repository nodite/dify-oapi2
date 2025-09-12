import os

from dify_oapi.api.chat.v1.model.chat_file import ChatFile
from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def main():
    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
    req_file = (
        ChatFile.builder()
        .type("image")
        .transfer_method("remote_url")
        .url("https://cloud.dify.ai/logo/logo-site.png")
        .build()
    )
    req_body = (
        ChatRequestBody.builder()
        .inputs({})
        .query(
            "What are the key specs of the iPhone 13 Pro Max? Keep it brief. Please answer within 10 words. No thinking process."
        )
        .response_mode("streaming")
        .conversation_id("")
        .user("abc-123")
        .files([req_file])
        .build()
    )
    req = ChatRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(os.getenv("CHAT_KEY")).build()
    response = client.chat.v1.chat.chat(req, req_option, True)
    # response = await client.chat.v1.chat.achat(req, req_option, True)
    for chunk in response:
        print(chunk.decode("utf-8"), end="", flush=True)


if __name__ == "__main__":
    main()
