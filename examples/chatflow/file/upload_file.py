#!/usr/bin/env python3
"""
Upload File Example

This example demonstrates how to upload files using the Chatflow File API
with both sync and async operations, supporting various file types.
Files are uploaded using multipart/form-data encoding.
"""

import asyncio
import os
from io import BytesIO

from dify_oapi.api.chatflow.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def validate_environment():
    """Validate required environment variables."""
    api_key = os.getenv("API_KEY")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")
    return api_key, domain


def create_sample_text_file():
    """Create a sample text file for upload."""
    content = """[Example] Sample Document

This is a sample document for testing file upload functionality.
It contains some text content that can be processed by the AI system.

Key points:
- This is a test document
- It demonstrates file upload capabilities
- The content is safe for testing purposes
"""
    return BytesIO(content.encode("utf-8"))


def create_sample_json_file():
    """Create a sample JSON file for upload."""
    content = """{
    "title": "[Example] Sample Data",
    "description": "This is sample JSON data for testing",
    "data": {
        "items": [
            {"id": 1, "name": "Test Item 1", "value": 100},
            {"id": 2, "name": "Test Item 2", "value": 200}
        ],
        "metadata": {
            "created": "2024-01-01",
            "version": "1.0"
        }
    }
}"""
    return BytesIO(content.encode("utf-8"))


def create_sample_csv_file():
    """Create a sample CSV file for upload."""
    content = """Name,Age,City,Score
[Example] Alice,25,New York,95
[Example] Bob,30,San Francisco,87
[Example] Charlie,28,Chicago,92
[Example] Diana,35,Boston,89
[Example] Eve,27,Seattle,94"""
    return BytesIO(content.encode("utf-8"))


def upload_text_file():
    """Upload a text file (sync)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Create sample text file
    file_data = create_sample_text_file()

    # Build request
    req = UploadFileRequest.builder().file(file_data, "[Example]_sample_document.txt").user("user-123").build()

    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute request
    response = client.chatflow.v1.file.upload(req, req_option)

    if response.success:
        print("✅ Text file uploaded successfully!")
        print(f"File ID: {response.id}")
        print(f"File Name: {response.name}")
        print(f"File Size: {response.size} bytes")
        print(f"File Extension: {response.extension}")
        print(f"MIME Type: {response.mime_type}")
    else:
        print(f"❌ Error: {response.msg}")


def upload_json_file():
    """Upload a JSON file (sync)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Create sample JSON file
    file_data = create_sample_json_file()

    # Build request
    req = UploadFileRequest.builder().file(file_data, "[Example]_sample_data.json").user("user-123").build()

    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute request
    response = client.chatflow.v1.file.upload(req, req_option)

    if response.success:
        print("✅ JSON file uploaded successfully!")
        print(f"File ID: {response.id}")
        print(f"File Name: {response.name}")
        print(f"File Size: {response.size} bytes")
        print(f"MIME Type: {response.mime_type}")
    else:
        print(f"❌ Error: {response.msg}")


def upload_csv_file():
    """Upload a CSV file (sync)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Create sample CSV file
    file_data = create_sample_csv_file()

    # Build request
    req = UploadFileRequest.builder().file(file_data, "[Example]_sample_data.csv").user("user-123").build()

    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute request
    response = client.chatflow.v1.file.upload(req, req_option)

    if response.success:
        print("✅ CSV file uploaded successfully!")
        print(f"File ID: {response.id}")
        print(f"File Name: {response.name}")
        print(f"File Size: {response.size} bytes")
        print(f"MIME Type: {response.mime_type}")
    else:
        print(f"❌ Error: {response.msg}")


async def upload_file_async():
    """Upload a file (async)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Create sample text file
    file_data = create_sample_text_file()

    # Build request
    req = UploadFileRequest.builder().file(file_data, "[Example]_async_document.txt").user("user-123").build()

    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute async request
    response = await client.chatflow.v1.file.aupload(req, req_option)

    if response.success:
        print("✅ Async file upload successful!")
        print(f"File ID: {response.id}")
        print(f"File Name: {response.name}")
        print(f"File Size: {response.size} bytes")
        print(f"MIME Type: {response.mime_type}")
    else:
        print(f"❌ Error: {response.msg}")


def upload_multiple_files():
    """Upload multiple files sequentially."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Define files to upload
    files_to_upload = [
        (create_sample_text_file(), "[Example]_doc1.txt", "text"),
        (create_sample_json_file(), "[Example]_data1.json", "json"),
        (create_sample_csv_file(), "[Example]_data1.csv", "csv"),
    ]

    uploaded_files = []

    for file_data, filename, file_type in files_to_upload:
        print(f"📤 Uploading {file_type} file: {filename}")

        # Build request
        req = UploadFileRequest.builder().file(file_data, filename).user("user-123").build()

        req_option = RequestOption.builder().api_key(api_key).build()

        # Execute request
        response = client.chatflow.v1.file.upload(req, req_option)

        if response.success:
            print(f"  ✅ {filename} uploaded successfully!")
            print(f"  File ID: {response.id}")
            uploaded_files.append({"id": response.id, "name": response.name, "type": file_type, "size": response.size})
        else:
            print(f"  ❌ Failed to upload {filename}: {response.msg}")
        print()

    # Summary
    print("📊 Upload Summary:")
    print(f"Total files uploaded: {len(uploaded_files)}")
    for file_info in uploaded_files:
        print(f"  - {file_info['name']} ({file_info['type']}): {file_info['size']} bytes")


def upload_file_with_error_handling():
    """Upload file with comprehensive error handling."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    try:
        # Create sample file
        file_data = create_sample_text_file()

        # Build request
        req = UploadFileRequest.builder().file(file_data, "[Example]_error_test.txt").user("user-123").build()

        req_option = RequestOption.builder().api_key(api_key).build()

        # Execute request
        response = client.chatflow.v1.file.upload(req, req_option)

        if response.success:
            print("✅ File uploaded with error handling!")
            print(f"File ID: {response.id}")
            print(f"File Name: {response.name}")
            print("Upload successful - file ready for use")
        else:
            # Handle different types of errors
            if "413" in str(response.code):
                print("❌ Error: File is too large")
                print("Suggestion: Try uploading a smaller file")
            elif "415" in str(response.code):
                print("❌ Error: Unsupported file type")
                print("Suggestion: Check supported file formats")
            elif "400" in str(response.code):
                print("❌ Error: Bad request")
                print("Suggestion: Check file format and request parameters")
            else:
                print(f"❌ Upload failed: {response.msg}")
                print(f"Error code: {response.code}")

    except Exception as e:
        print(f"❌ Unexpected error during upload: {e}")
        print("Please check your network connection and API configuration")


def demonstrate_file_usage_workflow():
    """Demonstrate complete file upload and usage workflow."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    print("🔄 Demonstrating complete file upload workflow:")
    print("1. Upload file")
    print("2. Get file ID")
    print("3. Use file ID in chat message")
    print()

    # Step 1: Upload file
    file_data = create_sample_text_file()

    req = UploadFileRequest.builder().file(file_data, "[Example]_workflow_demo.txt").user("user-123").build()

    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.chatflow.v1.file.upload(req, req_option)

    if response.success:
        print("✅ Step 1 Complete - File uploaded!")
        print(f"File ID: {response.id}")
        print()

        # Step 2: File ID is now available
        file_id = response.id
        print(f"✅ Step 2 Complete - File ID obtained: {file_id}")
        print()

        # Step 3: Show how to use file ID in chat
        print("✅ Step 3 - File ready for use in chat messages:")
        print("You can now use this file_id in ChatFile objects:")
        print(f'ChatFile.builder().type("document").transfer_method("local_file").upload_file_id("{file_id}").build()')
        print()
        print("Complete workflow successful! 🎉")
    else:
        print(f"❌ Workflow failed at Step 1: {response.msg}")


def main():
    """Run all file upload examples."""
    print("=== File Upload Examples ===\n")

    try:
        print("1. Upload Text File")
        upload_text_file()
        print()

        print("2. Upload JSON File")
        upload_json_file()
        print()

        print("3. Upload CSV File")
        upload_csv_file()
        print()

        print("4. Upload File (Async)")
        asyncio.run(upload_file_async())
        print()

        print("5. Upload Multiple Files")
        upload_multiple_files()
        print()

        print("6. Upload with Error Handling")
        upload_file_with_error_handling()
        print()

        print("7. Complete File Usage Workflow")
        demonstrate_file_usage_workflow()
        print()

    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")


if __name__ == "__main__":
    main()
