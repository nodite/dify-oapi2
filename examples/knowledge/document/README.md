# Document Management Examples

This directory contains examples demonstrating how to use the Dify Knowledge Base Document Management API.

## Prerequisites

Before running these examples, set up the following environment variables:

```bash
# Required for all examples
export API_KEY="your-api-key"
export DATASET_ID="your-dataset-id"
export DOMAIN="https://api.dify.ai"  # or your custom domain

# Required for specific examples
export DOCUMENT_ID="existing-document-id"  # For update and get operations
export BATCH_ID="batch-id"  # For indexing status check
export DOCUMENT_IDS="id1,id2,id3"  # For batch status updates (comma-separated)
export ACTION="enable"  # For update_status.py (values: enable, disable, archive)
```

## Basic Examples

### 1. Create Document by Text

Demonstrates how to create a document using text content.

```bash
python create_by_text.py
```

### 2. Create Document by File

Demonstrates how to create a document using file upload.

```bash
python create_by_file.py
```

### 3. List Documents

Demonstrates how to list documents in a dataset with pagination and filtering.

```bash
python list.py
```

### 4. Get Document

Retrieves detailed information about a specific document.

```bash
python get.py
```

### 5. Delete Document

Demonstrates how to delete a document from a dataset.

```bash
python delete.py
```

## Advanced Examples

### 1. Update Document by Text

Updates an existing document using text content.

```bash
python update_by_text.py
```

### 2. Update Document by File

Updates an existing document using file upload.

```bash
python update_by_file.py
```

### 3. Check Indexing Status

Checks the indexing status of a document batch.

```bash
python indexing_status.py
```

### 4. Update Document Status

Batch updates document status (enable, disable, or archive).

```bash
python update_status.py
```

### 5. Get Upload File Information

Retrieves information about the original uploaded file for a document.

```bash
python get_upload_file.py
```

## Common Operations

Each example demonstrates both synchronous and asynchronous API usage:

- Synchronous: Uses standard function calls like `client.knowledge.v1.document.create_by_text()`
- Asynchronous: Uses async functions like `client.knowledge.v1.document.acreate_by_text()`

## Error Handling

All examples include proper error handling with try/except blocks to gracefully handle API errors.
