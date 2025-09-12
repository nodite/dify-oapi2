# Knowledge Child Chunk Management Examples

This directory contains examples for managing child chunks in the Knowledge Base API. Child chunks are sub-segments that provide fine-grained content organization.

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

- **Fine-grained Content**: Break down segments into smaller chunks
- **Hierarchical Organization**: Dataset → Document → Segment → Child Chunk
- **Content Management**: Full CRUD operations on child chunks