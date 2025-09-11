#!/usr/bin/env python3
"""
Connection Pool Configuration Example

This example demonstrates how to configure HTTP connection pools
to optimize TCP connection usage and reduce resource overhead.
"""

import asyncio
import os

from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def optimized_client_example():
    """Example of creating a client with optimized connection pool settings."""

    # Get API key from environment
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Create client with optimized connection pool settings
    client = (
        Client.builder()
        .domain(os.getenv("DOMAIN", "https://api.dify.ai"))
        .max_keepalive_connections(10)  # Reduce keepalive connections for lower memory usage
        .max_connections(50)  # Reduce total connections for resource efficiency
        .keepalive_expiry(60.0)  # Increase keepalive time for better reuse
        .build()
    )

    try:
        # Create request
        req_body = (
            ChatRequestBody.builder()
            .inputs({})
            .query("[Example] Test connection pool optimization")
            .response_mode("blocking")
            .user("[Example] user-123")
            .build()
        )

        req = ChatRequest.builder().request_body(req_body).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Make multiple requests to test connection reuse
        print("Making multiple requests to test connection pool...")
        for i in range(5):
            response = client.chat.v1.chat.chat(req, req_option, False)
            if response.success:
                print(f"Request {i + 1}: Success - {response.answer[:50]}...")
            else:
                print(f"Request {i + 1}: Error - {response.msg}")

        print("Connection pool optimization test completed!")

    finally:
        # Important: Close connections when done
        client.close()


async def async_optimized_client_example():
    """Async example of using optimized connection pools."""

    # Get API key from environment
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Create client with conservative connection pool settings
    client = (
        Client.builder()
        .domain(os.getenv("DOMAIN", "https://api.dify.ai"))
        .max_keepalive_connections(5)  # Very conservative for async usage
        .max_connections(25)  # Lower limit for async
        .keepalive_expiry(45.0)  # Moderate keepalive time
        .build()
    )

    try:
        # Create request
        req_body = (
            ChatRequestBody.builder()
            .inputs({})
            .query("[Example] Async connection pool test")
            .response_mode("blocking")
            .user("[Example] async-user-456")
            .build()
        )

        req = ChatRequest.builder().request_body(req_body).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Make concurrent requests to test async connection handling
        print("Making concurrent async requests...")
        tasks = []
        for _i in range(3):
            task = client.chat.v1.chat.achat(req, req_option, False)
            tasks.append(task)

        responses = await asyncio.gather(*tasks, return_exceptions=True)

        for i, response in enumerate(responses):
            if isinstance(response, Exception):
                print(f"Async request {i + 1}: Exception - {response}")
            elif response.success:
                print(f"Async request {i + 1}: Success - {response.answer[:50]}...")
            else:
                print(f"Async request {i + 1}: Error - {response.msg}")

        print("Async connection pool test completed!")

    finally:
        # Important: Close async connections properly
        await client.aclose()


def high_throughput_example():
    """Example configuration for high-throughput scenarios."""

    # Get API key from environment
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # High-throughput configuration
    client = (
        Client.builder()
        .domain(os.getenv("DOMAIN", "https://api.dify.ai"))
        .max_keepalive_connections(50)  # Higher for throughput
        .max_connections(200)  # Higher total connections
        .keepalive_expiry(120.0)  # Longer keepalive for efficiency
        .build()
    )

    try:
        print("High-throughput configuration example")
        print("Max keepalive connections: 50")
        print("Max total connections: 200")
        print("Keepalive expiry: 120 seconds")
        print("This configuration is suitable for high-volume API usage")

    finally:
        client.close()


def low_resource_example():
    """Example configuration for resource-constrained environments."""

    # Get API key from environment
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Low-resource configuration
    client = (
        Client.builder()
        .domain(os.getenv("DOMAIN", "https://api.dify.ai"))
        .max_keepalive_connections(2)  # Minimal keepalive connections
        .max_connections(10)  # Low total connections
        .keepalive_expiry(15.0)  # Short keepalive time
        .build()
    )

    try:
        print("Low-resource configuration example")
        print("Max keepalive connections: 2")
        print("Max total connections: 10")
        print("Keepalive expiry: 15 seconds")
        print("This configuration minimizes memory and TCP resource usage")

    finally:
        client.close()


def main():
    """Run all connection pool examples."""
    try:
        print("=== Connection Pool Optimization Examples ===\n")

        print("1. Optimized Client Example:")
        optimized_client_example()
        print()

        print("2. Async Optimized Client Example:")
        asyncio.run(async_optimized_client_example())
        print()

        print("3. High-Throughput Configuration:")
        high_throughput_example()
        print()

        print("4. Low-Resource Configuration:")
        low_resource_example()
        print()

        print("=== Connection Pool Examples Completed ===")

    except ValueError as e:
        print(f"Configuration Error: {e}")
        print("Please set the required environment variables:")
        print("- API_KEY: Your Dify API key")
        print("- DOMAIN: Dify API domain (optional, defaults to https://api.dify.ai)")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
