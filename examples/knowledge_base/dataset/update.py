#!/usr/bin/env python3
"""
Dataset Update Example

This example demonstrates how to update dataset configuration using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.dataset.update_request import UpdateRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.update_request_body import UpdateRequestBody
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieval_model import RetrievalModel
from dify_oapi.api.knowledge_base.v1.model.dataset.reranking_model import RerankingModel
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_dataset_sync() -> None:
    """Update dataset synchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build retrieval model with reranking
        reranking_model = (
            RerankingModel.builder()
            .reranking_provider_name("cohere")
            .reranking_model_name("rerank-english-v2.0")
            .build()
        )
        
        retrieval_model = (
            RetrievalModel.builder()
            .search_method("hybrid_search")
            .reranking_enable(True)
            .reranking_model(reranking_model)
            .top_k(5)
            .score_threshold_enabled(True)
            .score_threshold(0.8)
            .build()
        )
        
        # Build update request body
        request_body = (
            UpdateRequestBody.builder()
            .name("Updated Dataset Name")
            .indexing_technique("high_quality")
            .permission("all_team_members")
            .embedding_model_provider("openai")
            .embedding_model("text-embedding-3-large")
            .retrieval_model(retrieval_model)
            .build()
        )
        
        # Build update request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = (
            UpdateRequest.builder()
            .dataset_id(dataset_id)
            .request_body(request_body)
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Update dataset
        response = client.knowledge_base.v1.dataset.update(request, request_option)
        
        print(f"Dataset updated successfully!")
        print(f"ID: {response.id}")
        print(f"Name: {response.name}")
        print(f"Indexing technique: {response.indexing_technique}")
        print(f"Permission: {response.permission}")
        print(f"Embedding model: {response.embedding_model}")
        print(f"Embedding provider: {response.embedding_model_provider}")
        print(f"Updated at: {response.updated_at}")
        
        # Display updated retrieval configuration
        if response.retrieval_model_dict:
            retrieval = response.retrieval_model_dict
            print(f"\nUpdated Retrieval Configuration:")
            print(f"  Search method: {retrieval.search_method}")
            print(f"  Reranking enabled: {retrieval.reranking_enable}")
            print(f"  Top K: {retrieval.top_k}")
            print(f"  Score threshold: {retrieval.score_threshold}")
        
    except Exception as e:
        print(f"Error updating dataset: {e}")


async def update_dataset_async() -> None:
    """Update dataset asynchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build simple retrieval model
        retrieval_model = (
            RetrievalModel.builder()
            .search_method("semantic_search")
            .reranking_enable(False)
            .top_k(3)
            .score_threshold_enabled(False)
            .build()
        )
        
        # Build update request body with minimal changes
        request_body = (
            UpdateRequestBody.builder()
            .name("Async Updated Dataset")
            .permission("only_me")
            .retrieval_model(retrieval_model)
            .build()
        )
        
        # Build update request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = (
            UpdateRequest.builder()
            .dataset_id(dataset_id)
            .request_body(request_body)
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Update dataset asynchronously
        response = await client.knowledge_base.v1.dataset.aupdate(request, request_option)
        
        print(f"Dataset updated successfully (async)!")
        print(f"Name: {response.name}")
        print(f"Permission: {response.permission}")
        print(f"Updated by: {response.updated_by}")
        print(f"Updated at: {response.updated_at}")
        
        # Display retrieval model changes
        if response.retrieval_model_dict:
            retrieval = response.retrieval_model_dict
            print(f"\nRetrieval Model:")
            print(f"  Search method: {retrieval.search_method}")
            print(f"  Reranking enabled: {retrieval.reranking_enable}")
            print(f"  Top K: {retrieval.top_k}")
        
    except Exception as e:
        print(f"Error updating dataset (async): {e}")


def update_partial_members() -> None:
    """Update dataset with partial member permissions."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build update request body for partial members
        request_body = (
            UpdateRequestBody.builder()
            .permission("partial_members")
            .partial_member_list(["user-id-1", "user-id-2", "user-id-3"])
            .build()
        )
        
        # Build update request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = (
            UpdateRequest.builder()
            .dataset_id(dataset_id)
            .request_body(request_body)
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Update dataset
        response = client.knowledge_base.v1.dataset.update(request, request_option)
        
        print(f"Dataset permission updated to partial members!")
        print(f"Permission: {response.permission}")
        if hasattr(response, 'partial_member_list') and response.partial_member_list:
            print(f"Partial members: {response.partial_member_list}")
        
    except Exception as e:
        print(f"Error updating partial members: {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Dataset Update Examples ===\n")
    
    # Check for required environment variables
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    if not os.getenv("DATASET_ID"):
        print("Please set the DATASET_ID environment variable")
        return
    
    print("1. Updating dataset synchronously...")
    update_dataset_sync()
    
    print("\n2. Updating dataset asynchronously...")
    asyncio.run(update_dataset_async())
    
    print("\n3. Updating dataset with partial member permissions...")
    update_partial_members()


if __name__ == "__main__":
    main()