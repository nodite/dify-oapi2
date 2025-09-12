# Knowledge Child Chunk Management Examples

This directory contains examples for managing child chunks in the Knowledge Base API (4 APIs). Child chunks are sub-segments that provide the finest level of content granularity, enabling precise content organization and retrieval within the hierarchical knowledge structure.

## 📋 Available Examples

- **`create_child_chunk.py`** - Create new child chunks within segments
- **`list_child_chunks.py`** - List all child chunks in a segment
- **`update_child_chunk.py`** - Update child chunk content
- **`delete_child_chunk.py`** - Delete child chunks

## 🚀 Quick Start

### Create Child Chunk

```python
from dify_oapi.api.knowledge.v1.model.create_child_chunk_request import CreateChildChunkRequest
from dify_oapi.api.knowledge.v1.model.create_child_chunk_request_body import CreateChildChunkRequestBody

req_body = (
    CreateChildChunkRequestBody.builder()
    .content("This is a child chunk content")
    .build()
)

req = CreateChildChunkRequest.builder()
    .dataset_id("dataset-id")
    .document_id("document-id")
    .segment_id("segment-id")
    .request_body(req_body)
    .build()

response = client.knowledge.v1.chunk.create_child_chunk(req, req_option)
```

## 🔧 Features

### Child Chunk Management APIs (4 APIs)
- **Create Child Chunk**: Add new sub-segments within existing segments
- **List Child Chunks**: Retrieve all child chunks within a segment with pagination
- **Update Child Chunk**: Modify child chunk content and metadata
- **Delete Child Chunk**: Remove child chunks from segments

### Content Organization
- **Hierarchical Structure**: Dataset → Document → Segment → Child Chunk (4-level hierarchy)
- **Fine-grained Control**: Precise content segmentation for optimal retrieval
- **Content Granularity**: Break down large segments into manageable pieces
- **Flexible Sizing**: Customize chunk sizes based on content type and use case
- **Metadata Preservation**: Maintain content relationships and context

### Advanced Capabilities
- **Batch Operations**: Efficient handling of multiple child chunks
- **Content Validation**: Ensure content quality and consistency
- **Search Optimization**: Improve search accuracy with granular content
- **Performance Tuning**: Optimize retrieval speed with appropriate chunk sizes
- **Context Preservation**: Maintain semantic relationships between chunks

### Use Cases
- **Large Document Processing**: Break down lengthy documents into searchable pieces
- **Precise Retrieval**: Enable exact content matching for specific queries
- **Content Versioning**: Track changes at the most granular level
- **Performance Optimization**: Balance content granularity with search performance
- **Semantic Chunking**: Organize content by semantic meaning and context