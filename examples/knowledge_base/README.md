# Knowledge Base Examples

This directory contains comprehensive examples for using the Dify Knowledge Base API, covering all dataset management, document management, metadata management, and tag management functionality.

## Overview

The Knowledge Base API provides 29 endpoints organized into four main categories:

- **Dataset Management** (6 APIs): Create, list, get, update, delete, and retrieve datasets
- **Document Management** (10 APIs): Create, update, list, delete documents, check indexing status, and manage document files
- **Metadata Management** (7 APIs): Create, list, update, delete metadata, toggle built-in fields, and update document metadata
- **Tag Management** (7 APIs): Create, list, update, delete tags, bind/unbind tags to datasets, and query bound tags

## Directory Structure

```
knowledge_base/
├── dataset/              # Dataset management examples
│   ├── create.py         # Create new datasets
│   ├── list.py           # List existing datasets
│   ├── get.py            # Get dataset details
│   ├── update.py         # Update dataset configuration
│   ├── delete.py         # Delete datasets
│   └── retrieve.py       # Perform retrieval search
├── document/             # Document management examples
│   ├── create_by_text.py # Create document using text content
│   ├── create_by_file.py # Create document using file upload
│   ├── update_by_text.py # Update document using text content
│   ├── update_by_file.py # Update document using file upload
│   ├── list.py           # List documents in a dataset
│   ├── get.py            # Get document details
│   ├── delete.py         # Delete document
│   ├── indexing_status.py # Check document indexing status
│   ├── update_status.py  # Update document status (enable/disable/archive)
│   └── get_upload_file.py # Get upload file information
├── metadata/             # Metadata management examples
│   ├── create.py         # Create metadata fields
│   ├── list.py           # List metadata configuration
│   ├── update.py         # Update metadata fields
│   ├── delete.py         # Delete metadata fields
│   ├── toggle_builtin.py # Enable/disable built-in metadata
│   └── update_document.py # Update document metadata values
├── tag/                  # Tag management examples
│   ├── create.py         # Create knowledge type tags
│   ├── list.py           # List all tags
│   ├── update.py         # Update tag names
│   ├── delete.py         # Delete tags
│   ├── bind.py           # Bind tags to datasets
│   ├── unbind.py         # Unbind tags from datasets
│   └── query_bound.py    # Query tags bound to a dataset
└── README.md             # This file
```

## Prerequisites

### Environment Variables

Set the following environment variables before running the examples:

```bash
# Required for all examples
export API_KEY="your-dify-api-key"
export DOMAIN="https://api.dify.ai"  # or your custom domain

# Required for most examples
export DATASET_ID="your-dataset-id"

# Optional for specific examples
export METADATA_ID="your-metadata-id"
export TAG_ID="your-tag-id"
export DOCUMENT_ID="your-document-id"
export BATCH_ID="your-batch-id"         # For document indexing status
export DOCUMENT_IDS="id1,id2,id3"       # For batch document status updates
export ACTION="enable"                  # For document status updates (enable, disable, archive)
```

### Dependencies

Ensure you have the dify-oapi package installed:

```bash
pip install dify-oapi
```

## Usage Examples

### Dataset Management

#### Create a Dataset
```bash
python examples/knowledge_base/dataset/create.py
```

Creates a new knowledge base with configurable settings including:
- Indexing technique (high_quality/economy)
- Permission levels (only_me/all_team_members/partial_members)
- Embedding model configuration
- Retrieval model settings

#### List Datasets
```bash
python examples/knowledge_base/dataset/list.py
```

Lists all available datasets with pagination and search capabilities.

#### Get Dataset Details
```bash
export DATASET_ID="your-dataset-id"
python examples/knowledge_base/dataset/get.py
```

Retrieves comprehensive dataset information including configuration, statistics, and metadata.

#### Update Dataset
```bash
export DATASET_ID="your-dataset-id"
python examples/knowledge_base/dataset/update.py
```

Updates dataset configuration including name, permissions, embedding models, and retrieval settings.

#### Delete Dataset
```bash
export DATASET_ID="your-dataset-id"
python examples/knowledge_base/dataset/delete.py
```

Deletes a dataset (irreversible operation with confirmation prompts).

#### Retrieve from Dataset
```bash
export DATASET_ID="your-dataset-id"
python examples/knowledge_base/dataset/retrieve.py
```

Performs search and retrieval operations with various configurations:
- Different search methods (semantic, full-text, hybrid)
- Reranking options
- Metadata filtering
- Score thresholds

### Document Management

#### Create Document by Text
```bash
export DATASET_ID="your-dataset-id"
python examples/knowledge_base/document/create_by_text.py
```

Creates a new document using text content with configurable settings:
- Document name and content
- Indexing technique (high_quality/economy)
- Document form (text_model/hierarchical_model/qa_model)
- Processing rules for segmentation

#### Create Document by File
```bash
export DATASET_ID="your-dataset-id"
python examples/knowledge_base/document/create_by_file.py
```

Creates a new document by uploading a file (PDF, DOCX, TXT, etc.) with configurable settings.

#### List Documents
```bash
export DATASET_ID="your-dataset-id"
python examples/knowledge_base/document/list.py
```

Lists all documents in a dataset with pagination, filtering, and sorting options.

#### Get Document Details
```bash
export DATASET_ID="your-dataset-id"
export DOCUMENT_ID="your-document-id"
python examples/knowledge_base/document/get.py
```

Retrieves comprehensive information about a specific document including processing status and metadata.

#### Update Document by Text
```bash
export DATASET_ID="your-dataset-id"
export DOCUMENT_ID="your-document-id"
python examples/knowledge_base/document/update_by_text.py
```

Updates an existing document with new text content while maintaining its configuration.

#### Update Document by File
```bash
export DATASET_ID="your-dataset-id"
export DOCUMENT_ID="your-document-id"
python examples/knowledge_base/document/update_by_file.py
```

Updates an existing document by uploading a new file while maintaining its configuration.

#### Delete Document
```bash
export DATASET_ID="your-dataset-id"
export DOCUMENT_ID="your-document-id"
python examples/knowledge_base/document/delete.py
```

Deletes a document from a dataset (irreversible operation with confirmation prompts).

#### Check Indexing Status
```bash
export DATASET_ID="your-dataset-id"
export BATCH_ID="your-batch-id"
python examples/knowledge_base/document/indexing_status.py
```

Checks the progress and status of document indexing operations.

#### Update Document Status
```bash
export DATASET_ID="your-dataset-id"
export DOCUMENT_IDS="id1,id2,id3"
export ACTION="enable"  # or "disable", "archive"
python examples/knowledge_base/document/update_status.py
```

Batch updates document status (enable, disable, or archive) for multiple documents.

#### Get Upload File Information
```bash
export DATASET_ID="your-dataset-id"
export DOCUMENT_ID="your-document-id"
python examples/knowledge_base/document/get_upload_file.py
```

Retrieves detailed information about the original uploaded file for a document.

### Metadata Management

#### Create Metadata Fields
```bash
export DATASET_ID="your-dataset-id"
python examples/knowledge_base/metadata/create.py
```

Creates custom metadata fields for documents with different data types (string, number, date).

#### List Metadata Configuration
```bash
export DATASET_ID="your-dataset-id"
python examples/knowledge_base/metadata/list.py
```

Lists all metadata fields and their usage statistics.

#### Update Metadata Fields
```bash
export DATASET_ID="your-dataset-id"
export METADATA_ID="your-metadata-id"
python examples/knowledge_base/metadata/update.py
```

Updates metadata field names and configuration.

#### Delete Metadata Fields
```bash
export DATASET_ID="your-dataset-id"
export METADATA_ID="your-metadata-id"
python examples/knowledge_base/metadata/delete.py
```

Deletes metadata fields (affects all documents).

#### Toggle Built-in Metadata
```bash
export DATASET_ID="your-dataset-id"
python examples/knowledge_base/metadata/toggle_builtin.py
```

Enables or disables built-in metadata fields like file name, creation date, etc.

#### Update Document Metadata
```bash
export DATASET_ID="your-dataset-id"
export DOCUMENT_ID="your-document-id"
python examples/knowledge_base/metadata/update_document.py
```

Updates metadata values for specific documents.

### Tag Management

#### Create Tags
```bash
python examples/knowledge_base/tag/create.py
```

Creates knowledge type tags for organizing datasets.

#### List Tags
```bash
python examples/knowledge_base/tag/list.py
```

Lists all available knowledge type tags.

#### Update Tags
```bash
export TAG_ID="your-tag-id"
python examples/knowledge_base/tag/update.py
```

Updates tag names.

#### Delete Tags
```bash
export TAG_ID="your-tag-id"
python examples/knowledge_base/tag/delete.py
```

Deletes tags (irreversible operation).

#### Bind Tags to Datasets
```bash
export DATASET_ID="your-dataset-id"
export TAG_ID_1="tag-id-1"
export TAG_ID_2="tag-id-2"
python examples/knowledge_base/tag/bind.py
```

Binds one or more tags to a dataset.

#### Unbind Tags from Datasets
```bash
export DATASET_ID="your-dataset-id"
export TAG_ID="your-tag-id"
python examples/knowledge_base/tag/unbind.py
```

Unbinds a tag from a dataset.

#### Query Bound Tags
```bash
export DATASET_ID="your-dataset-id"
python examples/knowledge_base/tag/query_bound.py
```

Lists all tags bound to a specific dataset.

## Example Features

### Sync and Async Support
All examples demonstrate both synchronous and asynchronous usage patterns:

```python
# Synchronous
response = client.knowledge_base.v1.dataset.create(request, request_option)

# Asynchronous
response = await client.knowledge_base.v1.dataset.acreate(request, request_option)
```

### Error Handling
Examples include comprehensive error handling:

```python
try:
    response = client.knowledge_base.v1.dataset.create(request, request_option)
    print(f"Success: {response.id}")
except Exception as e:
    print(f"Error: {e}")
```

### Builder Pattern Usage
All examples use the builder pattern for constructing requests:

```python
request = (
    CreateDatasetRequest.builder()
    .name("My Dataset")
    .description("A test dataset")
    .indexing_technique("high_quality")
    .build()
)
```

### Input Validation
Examples include validation for user inputs and environment variables.

### Confirmation Prompts
Destructive operations (delete, unbind) include confirmation prompts for safety.

## Common Patterns

### Client Initialization
```python
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption

client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
```

### Request Building
```python
request = (
    RequestClass.builder()
    .field1(value1)
    .field2(value2)
    .build()
)
```

### Response Handling
```python
response = client.knowledge_base.v1.resource.method(request, request_option)
print(f"Result: {response.field}")
```

## Best Practices

1. **Environment Variables**: Always use environment variables for sensitive data like API keys and IDs
2. **Error Handling**: Wrap API calls in try-catch blocks
3. **Confirmation**: Use confirmation prompts for destructive operations
4. **Validation**: Validate inputs before making API calls
5. **Async Usage**: Use async methods for better performance in concurrent scenarios
6. **Resource Cleanup**: Be mindful of resource limits and clean up unused resources

## Troubleshooting

### Common Issues

1. **Missing API Key**: Ensure `API_KEY` environment variable is set
2. **Invalid Dataset ID**: Verify the dataset exists and you have access
3. **Permission Errors**: Check your API key has the required permissions
4. **Rate Limiting**: Implement appropriate delays between requests
5. **Network Issues**: Handle network timeouts and retries

### Debug Mode

Enable debug logging by setting:
```bash
export DIFY_DEBUG=true
```

## Integration Testing

These examples can serve as integration tests by:
1. Setting appropriate environment variables
2. Running examples in sequence
3. Verifying expected outputs
4. Cleaning up created resources

## Contributing

When adding new examples:
1. Follow the established patterns
2. Include both sync and async variants
3. Add comprehensive error handling
4. Include input validation
5. Add confirmation prompts for destructive operations
6. Update this README with usage instructions

## Support

For issues with the examples or API:
1. Check the [Dify API Documentation](https://docs.dify.ai/)
2. Review the [dify-oapi GitHub repository](https://github.com/nodite/dify-oapi2)
3. Open an issue with detailed error information
