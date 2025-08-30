import os

from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_request import GetTextEmbeddingModelsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_embedding_models_sync():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetTextEmbeddingModelsRequest.builder().build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.model.embedding_models(req, req_option)

    if not response.success:
        print(f"API Error: {response.code} - {response.msg}")
        return

    print(f"Found {len(response.data or [])} embedding model providers")
    for provider in response.data or []:
        print(f"Provider: {provider.provider} (Status: {provider.status})")
        if provider.models:
            for model in provider.models:
                print(f"  - Model: {model.model} (Type: {model.model_type}, Status: {model.status})")
        else:
            print("  - No models available")


async def get_embedding_models_async():
    """Get embedding models asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        req = GetTextEmbeddingModelsRequest.builder().build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge.v1.model.aembedding_models(req, req_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print(f"Found {len(response.data or [])} embedding model providers (async)")
        for provider in response.data or []:
            print(f"Provider: {provider.provider} (Status: {provider.status})")
            if provider.models:
                for model in provider.models:
                    print(f"  - Model: {model.model} (Type: {model.model_type}, Status: {model.status})")
            else:
                print("  - No models available")

    except Exception as e:
        print(f"Error getting embedding models (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Text Embedding Models Examples ===\n")

    print("1. Getting embedding models synchronously...")
    get_embedding_models_sync()

    print("\n2. Getting embedding models asynchronously...")
    import asyncio

    asyncio.run(get_embedding_models_async())


if __name__ == "__main__":
    main()
