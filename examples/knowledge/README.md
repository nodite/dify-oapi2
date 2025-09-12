# Knowledge Base API Examples

The Knowledge Base API provides comprehensive knowledge management capabilities with 33 APIs across 6 resource types. This directory contains examples for all knowledge base operations.

## 📁 Resources

### [dataset/](./dataset/) - Dataset Management (6 APIs)
Core dataset operations for knowledge base management.

**Available Examples:**
- `create_dataset.py` - Create new datasets
- `get_dataset.py` - Retrieve dataset information
- `list_datasets.py` - List all datasets with pagination
- `update_dataset.py` - Update dataset configuration
- `delete_dataset.py` - Delete datasets
- `retrieve_from_dataset.py` - Query and retrieve from datasets

### [document/](./document/) - Document Management (10 APIs)
Upload, process, and manage documents within datasets.

**Available Examples:**
- `create_document_by_file.py` - Upload documents from files
- `create_document_by_text.py` - Create documents from text
- `get_document.py` - Retrieve document information
- `list_documents.py` - List documents in a dataset
- `update_document_by_file.py` - Update documents with new files
- `update_document_by_text.py` - Update documents with new text
- `update_document_status.py` - Change document status
- `delete_document.py` - Delete documents
- `get_batch_indexing_status.py` - Check batch processing status
- `get_upload_file_info.py` - Get file upload information

### [segment/](./segment/) - Segment Management (5 APIs)
Fine-grained content segmentation and management.

**Available Examples:**
- `create_segment.py` - Create new segments
- `get_segment.py` - Retrieve segment information
- `list_segments.py` - List segments in a document
- `update_segment.py` - Update segment content
- `delete_segment.py` - Delete segments

### [chunk/](./chunk/) - Child Chunk Management (4 APIs)
Sub-segment management for detailed content organization.

**Available Examples:**
- `create_child_chunk.py` - Create child chunks
- `list_child_chunks.py` - List child chunks
- `update_child_chunk.py` - Update child chunk content
- `delete_child_chunk.py` - Delete child chunks

### [tag/](./tag/) - Tag Management (7 APIs)
Metadata and knowledge type tags for content organization.

**Available Examples:**
- `create_tag.py` - Create new tags
- `list_tags.py` - List all available tags
- `update_tag.py` - Update tag information
- `delete_tag.py` - Delete tags
- `bind_tags_to_dataset.py` - Bind tags to datasets
- `unbind_tags_from_dataset.py` - Remove tags from datasets
- `get_dataset_tags.py` - Get tags associated with a dataset

### [model/](./model/) - Model Management (1 API)
Embedding model information and configuration.

**Available Examples:**
- `get_text_embedding_models.py` - Get available embedding models

## 🚀 Quick Start

### Create a Dataset

```python
from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody

req_body = (
    CreateDatasetRequestBody.builder()
    .name("My Knowledge Base")
    .description("A comprehensive knowledge base")
    .build()
)

req = CreateDatasetRequest.builder().request_body(req_body).build()
response = client.knowledge.v1.dataset.create_dataset(req, req_option)
dataset_id = response.id
```

### Upload a Document

```python
from dify_oapi.api.knowledge.v1.model.create_document_by_text_request import CreateDocumentByTextRequest
from dify_oapi.api.knowledge.v1.model.create_document_by_text_request_body import CreateDocumentByTextRequestBody

req_body = (
    CreateDocumentByTextRequestBody.builder()
    .name("Sample Document")
    .text("This is the content of my document...")
    .indexing_technique("high_quality")
    .build()
)

req = CreateDocumentByTextRequest.builder()
    .dataset_id(dataset_id)
    .request_body(req_body)
    .build()

response = client.knowledge.v1.document.create_document_by_text(req, req_option)
```

### Query the Dataset

```python
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request import RetrieveFromDatasetRequest
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request_body import RetrieveFromDatasetRequestBody

req_body = (
    RetrieveFromDatasetRequestBody.builder()
    .query("What is artificial intelligence?")
    .retrieval_model({"search_method": "semantic_search"})
    .build()
)

req = RetrieveFromDatasetRequest.builder()
    .dataset_id(dataset_id)
    .request_body(req_body)
    .build()

response = client.knowledge.v1.dataset.retrieve_from_dataset(req, req_option)
```

## 🔧 Features

### Dataset Management
- **CRUD Operations**: Complete dataset lifecycle management
- **Retrieval Configuration**: Flexible search and retrieval settings
- **Metadata Management**: Rich metadata and tagging support

### Document Processing
- **Multiple Input Types**: Text, files, and various document formats
- **Batch Processing**: Efficient bulk document handling
- **Status Tracking**: Monitor processing and indexing status
- **Version Control**: Update and manage document versions

### Content Organization
- **Hierarchical Structure**: Dataset → Document → Segment → Chunk
- **Flexible Segmentation**: Customizable content splitting
- **Tag System**: Comprehensive tagging and categorization
- **Search Optimization**: Advanced indexing and retrieval

### Advanced Features
- **Embedding Models**: Multiple embedding model support
- **Retrieval Strategies**: Various search and ranking methods
- **Quality Control**: Content validation and processing rules
- **Performance Optimization**: Efficient indexing and querying

## 📖 Environment Variables

```bash
export DOMAIN="https://api.dify.ai"
export KNOWLEDGE_KEY="your-knowledge-api-key"
```

## 🔗 Integration Examples

The Knowledge Base API integrates seamlessly with other Dify services:

- **Chat API**: Use knowledge bases to enhance chat responses
- **Completion API**: Leverage knowledge for text completion
- **Workflow API**: Incorporate knowledge retrieval in workflows

## 📚 Best Practices

1. **Organize Content Hierarchically**: Use the dataset → document → segment structure effectively
2. **Optimize Segmentation**: Choose appropriate segment sizes for your content
3. **Use Tags Strategically**: Implement a consistent tagging strategy
4. **Monitor Processing Status**: Always check indexing status for large uploads
5. **Choose Appropriate Models**: Select embedding models based on your content type
6. **Implement Error Handling**: Handle API errors gracefully in production code