#!/usr/bin/env python3
"""
Tag Create Example

This example demonstrates how to create knowledge type tags using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.tag.create_request import CreateTagRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_tag_sync() -> None:
    """Create tag synchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build create tag request
        request = (
            CreateTagRequest.builder()
            .name("Technical Documentation")
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Create tag
        response = client.knowledge_base.v1.tag.create(request, request_option)
        
        print(f"Tag created successfully!")
        print(f"ID: {response.id}")
        print(f"Name: {response.name}")
        print(f"Type: {response.type}")
        print(f"Binding count: {response.binding_count}")
        
    except Exception as e:
        print(f"Error creating tag: {e}")


async def create_tag_async() -> None:
    """Create tag asynchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build create tag request
        request = (
            CreateTagRequest.builder()
            .name("User Guides")
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Create tag asynchronously
        response = await client.knowledge_base.v1.tag.acreate(request, request_option)
        
        print(f"Tag created successfully (async)!")
        print(f"ID: {response.id}")
        print(f"Name: {response.name}")
        print(f"Type: {response.type}")
        print(f"Binding count: {response.binding_count}")
        
    except Exception as e:
        print(f"Error creating tag (async): {e}")


def create_multiple_tags() -> None:
    """Create multiple tags."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Define tags to create
        tag_names = [
            "API Reference",
            "Tutorials",
            "FAQ",
            "Best Practices",
            "Troubleshooting",
            "Getting Started"
        ]
        
        created_tags = []
        
        print(f"Creating {len(tag_names)} tags...")
        
        for tag_name in tag_names:
            try:
                request = CreateTagRequest.builder().name(tag_name).build()
                response = client.knowledge_base.v1.tag.create(request, request_option)
                created_tags.append(response)
                print(f"✓ Created tag: {tag_name} (ID: {response.id})")
                
            except Exception as e:
                print(f"✗ Failed to create tag '{tag_name}': {e}")
        
        print(f"\nSummary:")
        print(f"Successfully created {len(created_tags)} tags:")
        for tag in created_tags:
            print(f"  - {tag.name} (ID: {tag.id})")
        
    except Exception as e:
        print(f"Error creating multiple tags: {e}")


def create_tag_with_validation() -> None:
    """Create tag with name validation."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Get tag name from user input
        print("Enter tag name (max 50 characters): ", end="")
        tag_name = input().strip()
        
        # Validate tag name
        if not tag_name:
            print("Error: Tag name cannot be empty")
            return
        
        if len(tag_name) > 50:
            print("Error: Tag name is too long (max 50 characters)")
            return
        
        # Check for special characters (basic validation)
        if not all(c.isalnum() or c.isspace() or c in '-_' for c in tag_name):
            print("Error: Tag name contains invalid characters")
            return
        
        # Build request
        request = CreateTagRequest.builder().name(tag_name).build()
        
        # Create tag
        response = client.knowledge_base.v1.tag.create(request, request_option)
        
        print(f"\nTag created successfully with validation!")
        print(f"ID: {response.id}")
        print(f"Name: {response.name}")
        print(f"Type: {response.type}")
        print(f"Binding count: {response.binding_count}")
        
    except Exception as e:
        print(f"Error creating tag with validation: {e}")


def create_categorized_tags() -> None:
    """Create tags organized by categories."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Define categorized tags
        tag_categories = {
            "Content Type": [
                "Documentation",
                "Tutorial",
                "Reference",
                "Example"
            ],
            "Difficulty Level": [
                "Beginner",
                "Intermediate", 
                "Advanced",
                "Expert"
            ],
            "Topic Area": [
                "API",
                "SDK",
                "Integration",
                "Configuration"
            ]
        }
        
        all_created_tags = {}
        
        for category, tag_names in tag_categories.items():
            print(f"\nCreating {category} tags...")
            created_tags = []
            
            for tag_name in tag_names:
                try:
                    request = CreateTagRequest.builder().name(tag_name).build()
                    response = client.knowledge_base.v1.tag.create(request, request_option)
                    created_tags.append(response)
                    print(f"  ✓ {tag_name}")
                    
                except Exception as e:
                    print(f"  ✗ {tag_name}: {e}")
            
            all_created_tags[category] = created_tags
        
        # Summary
        print(f"\n=== Creation Summary ===")
        total_created = 0
        for category, tags in all_created_tags.items():
            print(f"\n{category} ({len(tags)} tags):")
            for tag in tags:
                print(f"  • {tag.name} (ID: {tag.id})")
                total_created += 1
        
        print(f"\nTotal tags created: {total_created}")
        
    except Exception as e:
        print(f"Error creating categorized tags: {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Tag Create Examples ===\n")
    
    # Check for required environment variables
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    print("1. Creating tag synchronously...")
    create_tag_sync()
    
    print("\n2. Creating tag asynchronously...")
    asyncio.run(create_tag_async())
    
    print("\n3. Creating multiple tags...")
    create_multiple_tags()
    
    print("\n4. Creating tag with validation...")
    create_tag_with_validation()
    
    print("\n5. Creating categorized tags...")
    create_categorized_tags()


if __name__ == "__main__":
    main()