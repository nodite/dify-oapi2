#!/usr/bin/env python3
"""
Dataset Get Example

This example demonstrates how to get detailed information about a specific dataset using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.dataset.get_request import GetRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_dataset_sync() -> None:
    """Get dataset details synchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build get request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = GetRequest.builder().dataset_id(dataset_id).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Get dataset details
        response = client.knowledge_base.v1.dataset.get(request, request_option)
        
        print(f"Dataset Details:")
        print(f"  ID: {response.id}")
        print(f"  Name: {response.name}")
        print(f"  Description: {response.description}")
        print(f"  Provider: {response.provider}")
        print(f"  Permission: {response.permission}")
        print(f"  Data source type: {response.data_source_type}")
        print(f"  Indexing technique: {response.indexing_technique}")
        print(f"  App count: {response.app_count}")
        print(f"  Document count: {response.document_count}")
        print(f"  Word count: {response.word_count}")
        print(f"  Created by: {response.created_by}")
        print(f"  Created at: {response.created_at}")
        print(f"  Updated by: {response.updated_by}")
        print(f"  Updated at: {response.updated_at}")
        print(f"  Embedding model: {response.embedding_model}")
        print(f"  Embedding model provider: {response.embedding_model_provider}")
        print(f"  Embedding available: {response.embedding_available}")
        
        # Display retrieval model configuration
        if response.retrieval_model_dict:
            print(f"\nRetrieval Model Configuration:")
            retrieval = response.retrieval_model_dict
            print(f"  Search method: {retrieval.search_method}")
            print(f"  Reranking enabled: {retrieval.reranking_enable}")
            print(f"  Top K: {retrieval.top_k}")
            print(f"  Score threshold enabled: {retrieval.score_threshold_enabled}")
            if retrieval.score_threshold is not None:
                print(f"  Score threshold: {retrieval.score_threshold}")
        
        # Display tags
        if response.tags:
            print(f"\nTags:")
            for tag in response.tags:
                print(f"  - {tag.name} (ID: {tag.id})")
        
        # Display external knowledge info
        if response.external_knowledge_info:
            ext_info = response.external_knowledge_info
            print(f"\nExternal Knowledge Info:")
            print(f"  External knowledge ID: {ext_info.external_knowledge_id}")
            print(f"  External knowledge API ID: {ext_info.external_knowledge_api_id}")
        
    except Exception as e:
        print(f"Error getting dataset: {e}")


async def get_dataset_async() -> None:
    """Get dataset details asynchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build get request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = GetRequest.builder().dataset_id(dataset_id).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Get dataset details asynchronously
        response = await client.knowledge_base.v1.dataset.aget(request, request_option)
        
        print(f"Dataset Details (Async):")
        print(f"  Name: {response.name}")
        print(f"  ID: {response.id}")
        print(f"  Permission: {response.permission}")
        print(f"  Document count: {response.document_count}")
        print(f"  Word count: {response.word_count}")
        
        # Show embedding configuration
        if response.embedding_model and response.embedding_model_provider:
            print(f"\nEmbedding Configuration:")
            print(f"  Model: {response.embedding_model}")
            print(f"  Provider: {response.embedding_model_provider}")
            print(f"  Available: {response.embedding_available}")
        
        # Show external retrieval model if available
        if response.external_retrieval_model:
            ext_retrieval = response.external_retrieval_model
            print(f"\nExternal Retrieval Model:")
            print(f"  Top K: {ext_retrieval.top_k}")
            print(f"  Score threshold: {ext_retrieval.score_threshold}")
            print(f"  Score threshold enabled: {ext_retrieval.score_threshold_enabled}")
        
    except Exception as e:
        print(f"Error getting dataset (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Dataset Get Examples ===\n")
    
    # Check for required environment variables
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    if not os.getenv("DATASET_ID"):
        print("Please set the DATASET_ID environment variable")
        return
    
    print("1. Getting dataset details synchronously...")
    get_dataset_sync()
    
    print("\n2. Getting dataset details asynchronously...")
    asyncio.run(get_dataset_async())


if __name__ == "__main__":
    main()