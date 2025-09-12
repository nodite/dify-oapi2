# Document Management Examples

This directory contains examples demonstrating how to use the Dify Knowledge Base Document Management API (10 APIs). Documents are the primary content units within datasets, supporting various file formats and processing methods.

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

## 🔧 API Features

### Document Creation (2 APIs)
- **Create by Text**: Direct text content upload with custom processing
- **Create by File**: File upload with automatic format detection and parsing

### Document Management (4 APIs)
- **Get Document**: Retrieve detailed document information and metadata
- **List Documents**: Browse documents with pagination, filtering, and sorting
- **Update by Text**: Modify document content using text input
- **Update by File**: Replace document content with new file upload

### Document Operations (4 APIs)
- **Delete Document**: Remove documents and associated content
- **Update Status**: Batch status updates (enable, disable, archive)
- **Get Indexing Status**: Monitor batch processing and indexing progress
- **Get Upload File Info**: Retrieve original file metadata and processing details

### Advanced Capabilities
- **Multi-format Support**: PDF, DOCX, TXT, Markdown, HTML, and more
- **Batch Processing**: Efficient handling of multiple documents
- **Status Management**: Granular control over document lifecycle
- **Indexing Control**: Monitor and manage content processing
- **Metadata Extraction**: Automatic extraction of file properties
- **Version Tracking**: Track document updates and changes

## 🚀 Processing Features

### Indexing Techniques
- **High Quality**: Advanced processing with better accuracy
- **Economy**: Faster processing with standard quality
- **Custom**: Configurable processing parameters

### File Processing
- **Automatic Parsing**: Intelligent content extraction
- **Custom Rules**: Define processing and segmentation rules
- **Quality Control**: Validation and error handling
- **Progress Tracking**: Real-time processing status updates

## 📊 Monitoring & Analytics

### Status Tracking
- **Processing States**: queuing, indexing, completed, error
- **Batch Operations**: Monitor multiple document processing
- **Error Reporting**: Detailed error messages and recovery options
- **Performance Metrics**: Processing time and resource usage

## 🔧 Common Operations

Each example demonstrates both synchronous and asynchronous API usage:

- **Synchronous**: Standard function calls like `client.knowledge.v1.document.create_document_by_text()`
- **Asynchronous**: Async functions like `client.knowledge.v1.document.acreate_document_by_text()`

## ⚠️ Error Handling

All examples include comprehensive error handling:
- API error responses with detailed messages
- Network timeout and retry logic
- File validation and format checking
- Graceful degradation for partial failures
