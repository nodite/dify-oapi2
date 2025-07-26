#!/usr/bin/env python3
"""
Dataset Creation Example

This example demonstrates how to create a new dataset (knowledge base) using the Dify API.
"""

import asyncio
import os
from typing import Optional

from dify_oapi.api.knowledge_base.v1.model.dataset.create_request import CreateRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.create_request_body import CreateRequestBody
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieval_model import RetrievalModel
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_dataset_sync() -> None:
    """Create a dataset synchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build retrieval model configuration
        retrieval_model = (
            RetrievalModel.builder()
            .search_method("semantic_search")
            .reranking_enable(False)
            .top_k(3)
            .score_threshold_enabled(False)
            .build()
        )
        
        # Build request body
        request_body = (
            CreateRequestBody.builder()
            .name("My Test Dataset")
            .description("A test dataset created via API")
            .indexing_technique("high_quality")
            .permission("only_me")
            .provider("vendor")
            .embedding_model("text-embedding-3-small")
            .embedding_model_provider("openai")
            .retrieval_model(retrieval_model)
            .build()
        )
        
        # Build create request
        request = (
            CreateRequest.builder()
            .request_body(request_body)
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Create dataset
        response = client.knowledge_base.v1.dataset.create(request, request_option)
        
        print(f"Dataset created successfully!")
        print(f"ID: {response.id}")
        print(f"Name: {response.name}")
        print(f"Description: {response.description}")
        print(f"Created at: {response.created_at}")
        
    except Exception as e:
        print(f"Error creating dataset: {e}")


async def create_dataset_async() -> None:
    """Create a dataset asynchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build retrieval model configuration
        retrieval_model = (
            RetrievalModel.builder()
            .search_method("hybrid_search")
            .reranking_enable(True)
            .top_k(5)
            .score_threshold_enabled(True)
            .score_threshold(0.7)
            .build()
        )
        
        # Build request body
        request_body = (
            CreateRequestBody.builder()
            .name("My Async Dataset")
            .description("A test dataset created via async API")
            .indexing_technique("economy")
            .permission("all_team_members")
            .provider("vendor")
            .retrieval_model(retrieval_model)
            .build()
        )
        
        # Build create request
        request = (
            CreateRequest.builder()
            .request_body(request_body)
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Create dataset asynchronously
        response = await client.knowledge_base.v1.dataset.acreate(request, request_option)
        
        print(f"Dataset created successfully (async)!")
        print(f"ID: {response.id}")
        print(f"Name: {response.name}")
        print(f"Description: {response.description}")
        print(f"Indexing technique: {response.indexing_technique}")
        print(f"Permission: {response.permission}")
        
    except Exception as e:
        print(f"Error creating dataset (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Dataset Creation Examples ===\n")
    
    # Check for required environment variables
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    print("1. Creating dataset synchronously...")
    create_dataset_sync()
    
    print("\n2. Creating dataset asynchronously...")
    asyncio.run(create_dataset_async())


if __name__ == "__main__":
    main()