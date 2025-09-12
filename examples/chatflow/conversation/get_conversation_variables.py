#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.get_conversation_variables_request import GetConversationVariablesRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_conversation_variables_sync():
    """Get conversation variables synchronously."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_KEY")
    if not api_key:
        raise ValueError("CHATFLOW_KEY environment variable is required")

    conversation_id = os.getenv("CONVERSATION_ID")
    if not conversation_id:
        print("Note: CONVERSATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real conversation id to execute.")
        print("Set CONVERSATION_ID environment variable with a valid ID to test this functionality.")
        return

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request
    request = (
        GetConversationVariablesRequest.builder().conversation_id(conversation_id).user("user-123").limit(20).build()
    )

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.conversation.variables(request, request_option)

        if response.success:
            print(f"Retrieved {len(response.data)} variables")
            print(f"Has more: {response.has_more}")
            print(f"Limit: {response.limit}")

            for variable in response.data:
                print(f"Variable ID: {variable.id}")
                print(f"Name: {variable.name}")
                print(f"Value Type: {variable.value_type}")
                print(f"Value: {variable.value}")
                if variable.description:
                    print(f"Description: {variable.description}")
                print(f"Created at: {variable.created_at}")
                print(f"Updated at: {variable.updated_at}")
                print("---")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


async def get_conversation_variables_async():
    """Get conversation variables asynchronously."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_KEY")
    if not api_key:
        raise ValueError("CHATFLOW_KEY environment variable is required")

    conversation_id = os.getenv("CONVERSATION_ID")
    if not conversation_id:
        print("Note: CONVERSATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real conversation id to execute.")
        print("Set CONVERSATION_ID environment variable with a valid ID to test this functionality.")
        return

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request
    request = (
        GetConversationVariablesRequest.builder().conversation_id(conversation_id).user("user-123").limit(10).build()
    )

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute async request
        response = await client.chatflow.v1.conversation.avariables(request, request_option)

        if response.success:
            print(f"Retrieved {len(response.data)} variables (async)")
            print(f"Has more: {response.has_more}")

            for variable in response.data:
                print(f"Variable: {variable.name} = {variable.value}")
                print(f"Type: {variable.value_type}")
                print("---")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def get_conversation_variables_with_filter():
    """Get conversation variables with name filter."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_KEY")
    if not api_key:
        raise ValueError("CHATFLOW_KEY environment variable is required")

    conversation_id = os.getenv("CONVERSATION_ID")
    if not conversation_id:
        print("Note: CONVERSATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real conversation id to execute.")
        print("Set CONVERSATION_ID environment variable with a valid ID to test this functionality.")
        return

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request with variable name filter
    request = (
        GetConversationVariablesRequest.builder()
        .conversation_id(conversation_id)
        .user("user-123")
        .variable_name("user_name")
        .limit(10)
        .build()
    )

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.conversation.variables(request, request_option)

        if response.success:
            print(f"Retrieved {len(response.data)} variables with name filter")

            for variable in response.data:
                print(f"Variable: {variable.name}")
                print(f"Value: {variable.value}")
                print(f"Type: {variable.value_type}")
                if variable.description:
                    print(f"Description: {variable.description}")
                print("---")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def get_conversation_variables_with_pagination():
    """Get conversation variables with pagination."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_KEY")
    if not api_key:
        raise ValueError("CHATFLOW_KEY environment variable is required")

    conversation_id = os.getenv("CONVERSATION_ID")
    if not conversation_id:
        print("Note: CONVERSATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real conversation id to execute.")
        print("Set CONVERSATION_ID environment variable with a valid ID to test this functionality.")
        return

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        last_id = None
        page = 1

        while True:
            # Build request with pagination
            request_builder = (
                GetConversationVariablesRequest.builder().conversation_id(conversation_id).user("user-123").limit(5)
            )

            if last_id:
                request_builder.last_id(last_id)

            request = request_builder.build()

            # Execute request
            response = client.chatflow.v1.conversation.variables(request, request_option)

            if response.success:
                print(f"Page {page}: Retrieved {len(response.data)} variables")

                if not response.data:
                    print("No more variables")
                    break

                for variable in response.data:
                    print(f"  - {variable.name}: {variable.value} ({variable.value_type})")

                if not response.has_more:
                    print("Reached end of variables")
                    break

                # Set last_id for next page
                last_id = response.data[-1].id
                page += 1

            else:
                print(f"Error: {response.msg}")
                break

    except Exception as e:
        print(f"Exception occurred: {e}")


def get_conversation_variables_by_type():
    """Get conversation variables and group by type."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_KEY")
    if not api_key:
        raise ValueError("CHATFLOW_KEY environment variable is required")

    conversation_id = os.getenv("CONVERSATION_ID")
    if not conversation_id:
        print("Note: CONVERSATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real conversation id to execute.")
        print("Set CONVERSATION_ID environment variable with a valid ID to test this functionality.")
        return

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request
    request = (
        GetConversationVariablesRequest.builder().conversation_id(conversation_id).user("user-123").limit(50).build()
    )

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.conversation.variables(request, request_option)

        if response.success:
            # Group variables by type
            variables_by_type = {}

            for variable in response.data:
                var_type = variable.value_type
                if var_type not in variables_by_type:
                    variables_by_type[var_type] = []
                variables_by_type[var_type].append(variable)

            print(f"Retrieved {len(response.data)} variables grouped by type:")

            for var_type, variables in variables_by_type.items():
                print(f"\n{var_type.upper()} Variables ({len(variables)}):")
                for variable in variables:
                    print(f"  - {variable.name}: {variable.value}")

        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


if __name__ == "__main__":
    print("=== Get Conversation Variables Examples ===")

    print("\n1. Sync Example:")
    get_conversation_variables_sync()

    print("\n2. Async Example:")
    asyncio.run(get_conversation_variables_async())

    print("\n3. Filter Example:")
    get_conversation_variables_with_filter()

    print("\n4. Pagination Example:")
    get_conversation_variables_with_pagination()

    print("\n5. Group by Type Example:")
    get_conversation_variables_by_type()
