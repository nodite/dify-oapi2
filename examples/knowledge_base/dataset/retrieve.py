#!/usr/bin/env python3
"""
Dataset Retrieve Example

This example demonstrates how to perform retrieval search in a dataset using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_request import RetrieveDatasetRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieval_model import RetrievalModel
from dify_oapi.api.knowledge_base.v1.model.dataset.reranking_model import RerankingModel
from dify_oapi.api.knowledge_base.v1.model.dataset.metadata_filtering_conditions import MetadataFilteringConditions
from dify_oapi.api.knowledge_base.v1.model.dataset.filter_condition import FilterCondition
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def retrieve_basic_sync() -> None:
    """Perform basic retrieval synchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build basic retrieval model
        retrieval_model = (
            RetrievalModel.builder()
            .search_method("semantic_search")
            .reranking_enable(False)
            .top_k(5)
            .score_threshold_enabled(True)
            .score_threshold(0.5)
            .build()
        )
        
        # Build retrieve request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = (
            RetrieveDatasetRequest.builder()
            .dataset_id(dataset_id)
            .query("What is artificial intelligence?")
            .retrieval_model(retrieval_model)
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Perform retrieval
        response = client.knowledge_base.v1.dataset.retrieve(request, request_option)
        
        print(f"Retrieval Results:")
        print(f"Query: {response.query.content}")
        print(f"Found {len(response.records)} records\n")
        
        for i, record in enumerate(response.records, 1):
            segment = record.segment
            print(f"Result {i}:")
            print(f"  Score: {record.score}")
            print(f"  Segment ID: {segment.id}")
            print(f"  Document: {segment.document.name}")
            print(f"  Content: {segment.content[:200]}...")
            print(f"  Word count: {segment.word_count}")
            print(f"  Keywords: {', '.join(segment.keywords[:5]) if segment.keywords else 'None'}")
            print()
        
    except Exception as e:
        print(f"Error performing retrieval: {e}")


async def retrieve_with_reranking_async() -> None:
    """Perform retrieval with reranking asynchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build reranking model
        reranking_model = (
            RerankingModel.builder()
            .reranking_provider_name("cohere")
            .reranking_model_name("rerank-english-v2.0")
            .build()
        )
        
        # Build retrieval model with reranking
        retrieval_model = (
            RetrievalModel.builder()
            .search_method("hybrid_search")
            .reranking_enable(True)
            .reranking_model(reranking_model)
            .top_k(10)
            .score_threshold_enabled(True)
            .score_threshold(0.7)
            .build()
        )
        
        # Build retrieve request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = (
            RetrieveDatasetRequest.builder()
            .dataset_id(dataset_id)
            .query("machine learning algorithms")
            .retrieval_model(retrieval_model)
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Perform retrieval asynchronously
        response = await client.knowledge_base.v1.dataset.aretrieve(request, request_option)
        
        print(f"Retrieval with Reranking (Async):")
        print(f"Query: {response.query.content}")
        print(f"Found {len(response.records)} records\n")
        
        for i, record in enumerate(response.records, 1):
            segment = record.segment
            print(f"Reranked Result {i}:")
            print(f"  Score: {record.score:.6f}")
            print(f"  Document: {segment.document.name}")
            print(f"  Position: {segment.position}")
            print(f"  Content preview: {segment.content[:150]}...")
            print()
        
    except Exception as e:
        print(f"Error performing retrieval with reranking (async): {e}")


def retrieve_with_metadata_filtering() -> None:
    """Perform retrieval with metadata filtering."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build metadata filtering conditions
        conditions = [
            FilterCondition.builder()
            .name("category")
            .comparison_operator("is")
            .value("technical")
            .build(),
            FilterCondition.builder()
            .name("priority")
            .comparison_operator(">=")
            .value(5)
            .build()
        ]
        
        metadata_filtering = (
            MetadataFilteringConditions.builder()
            .logical_operator("and")
            .conditions(conditions)
            .build()
        )
        
        # Build retrieval model with metadata filtering
        retrieval_model = (
            RetrievalModel.builder()
            .search_method("full_text_search")
            .top_k(3)
            .score_threshold_enabled(False)
            .metadata_filtering_conditions(metadata_filtering)
            .build()
        )
        
        # Build retrieve request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = (
            RetrieveDatasetRequest.builder()
            .dataset_id(dataset_id)
            .query("API documentation")
            .retrieval_model(retrieval_model)
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Perform retrieval
        response = client.knowledge_base.v1.dataset.retrieve(request, request_option)
        
        print(f"Retrieval with Metadata Filtering:")
        print(f"Query: {response.query.content}")
        print(f"Filters: category='technical' AND priority>=5")
        print(f"Found {len(response.records)} records\n")
        
        for i, record in enumerate(response.records, 1):
            segment = record.segment
            print(f"Filtered Result {i}:")
            print(f"  Score: {record.score}")
            print(f"  Document: {segment.document.name}")
            print(f"  Content: {segment.content[:100]}...")
            print(f"  Status: {segment.status}")
            print()
        
    except Exception as e:
        print(f"Error performing retrieval with metadata filtering: {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Dataset Retrieve Examples ===\n")
    
    # Check for required environment variables
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    if not os.getenv("DATASET_ID"):
        print("Please set the DATASET_ID environment variable")
        return
    
    print("1. Basic retrieval synchronously...")
    retrieve_basic_sync()
    
    print("\n2. Retrieval with reranking asynchronously...")
    asyncio.run(retrieve_with_reranking_async())
    
    print("\n3. Retrieval with metadata filtering...")
    retrieve_with_metadata_filtering()


if __name__ == "__main__":
    main()