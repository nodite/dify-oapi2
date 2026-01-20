# Knowledge Segment Management Examples

This directory contains examples for managing segments in the Knowledge Base API (5 APIs). Segments are content divisions within documents that provide structured organization and enable precise content retrieval and management.

## 📋 Available Examples

### Core Operations
- **`create_segment.py`** - Create new segments within documents
- **`get_segment.py`** - Retrieve detailed segment information
- **`list_segments.py`** - List all segments in a document with pagination
- **`update_segment.py`** - Update segment content and metadata
- **`delete_segment.py`** - Delete segments from documents

## 🚀 Quick Start

### Create Segment

```python
from dify_oapi.api.knowledge.v1.model.create_segment_request import CreateSegmentRequest
from dify_oapi.api.knowledge.v1.model.create_segment_request_body import CreateSegmentRequestBody

req_body = (
    CreateSegmentRequestBody.builder()
    .content("This is the segment content that will be indexed and searchable.")
    .answer("This is the answer or summary for this segment.")
    .keywords(["keyword1", "keyword2", "keyword3"])
    .build()
)

req = CreateSegmentRequest.builder()
    .dataset_id("your-dataset-id")
    .document_id("your-document-id")
    .request_body(req_body)
    .build()

response = client.knowledge.v1.segment.create_segment(req, req_option)
print(f"Segment created with ID: {response.id}")
```

### List Segments

```python
from dify_oapi.api.knowledge.v1.model.list_segments_request import ListSegmentsRequest

req = ListSegmentsRequest.builder()
    .dataset_id("your-dataset-id")
    .document_id("your-document-id")
    .page(1)
    .limit(20)
    .build()

response = client.knowledge.v1.segment.list_segments(req, req_option)
for segment in response.data:
    print(f"ID: {segment.id}, Content: {segment.content[:100]}...")
```

### Update Segment

```python
from dify_oapi.api.knowledge.v1.model.update_segment_request import UpdateSegmentRequest
from dify_oapi.api.knowledge.v1.model.update_segment_request_body import UpdateSegmentRequestBody

req_body = (
    UpdateSegmentRequestBody.builder()
    .content("Updated segment content with new information.")
    .answer("Updated answer or summary.")
    .keywords(["updated", "keywords", "list"])
    .enabled(True)
    .build()
)

req = UpdateSegmentRequest.builder()
    .dataset_id("your-dataset-id")
    .document_id("your-document-id")
    .segment_id("your-segment-id")
    .request_body(req_body)
    .build()

response = client.knowledge.v1.segment.update_segment(req, req_option)
```

## 🔧 Features

### Segment Management APIs (5 APIs)
- **Create Segment**: Add new content segments with metadata and keywords
- **Get Segment**: Retrieve detailed segment information and statistics
- **List Segments**: Browse document segments with filtering and pagination
- **Update Segment**: Modify segment content, answers, and keywords
- **Delete Segment**: Remove segments and associated child chunks

### Content Organization
- **Structured Content**: Organize document content into logical segments
- **Hierarchical Structure**: Dataset → Document → Segment → Child Chunk
- **Flexible Segmentation**: Custom segment sizes and boundaries
- **Content Relationships**: Maintain context between related segments
- **Metadata Management**: Rich metadata including keywords and answers

### Search Optimization
- **Keyword Indexing**: Enhanced search with custom keywords
- **Answer Extraction**: Provide direct answers for common queries
- **Content Chunking**: Optimize content for retrieval accuracy
- **Semantic Segmentation**: Maintain semantic coherence within segments
- **Performance Tuning**: Balance segment size with search performance

### Advanced Features
- **Batch Operations**: Efficient handling of multiple segments
- **Status Management**: Enable/disable segments for search
- **Content Validation**: Ensure content quality and consistency
- **Version Control**: Track segment changes and updates
- **Analytics**: Monitor segment usage and performance metrics

## 📖 Content Structure

### Segment Components
- **Content**: Main text content of the segment
- **Answer**: Optional direct answer or summary
- **Keywords**: List of relevant keywords for enhanced search
- **Metadata**: Additional information like creation time, status, etc.
- **Position**: Segment position within the document

### Best Practices
1. **Optimal Size**: Keep segments focused but comprehensive (100-500 words)
2. **Clear Boundaries**: Ensure segments have logical start and end points
3. **Relevant Keywords**: Use specific, searchable keywords
4. **Meaningful Answers**: Provide concise, accurate answers when applicable
5. **Regular Updates**: Keep segment content current and accurate

## 🔗 Integration

### With Other APIs
- **Child Chunks**: Further divide segments into smaller chunks
- **Document Management**: Segments belong to documents
- **Dataset Queries**: Segments are searchable through dataset retrieval
- **Chat/Completion**: Segments provide context for AI responses

### Use Cases
- **FAQ Systems**: Create segments for frequently asked questions
- **Documentation**: Organize technical documentation into searchable segments
- **Knowledge Bases**: Structure company knowledge for easy retrieval
- **Content Management**: Organize large documents into manageable pieces
- **Search Optimization**: Improve search accuracy with well-structured content

## 📚 Environment Variables

```bash
export DOMAIN="https://api.dify.ai"
export KNOWLEDGE_KEY="your-knowledge-api-key"
export DATASET_ID="your-dataset-id"
export DOCUMENT_ID="your-document-id"
```

## 🔗 Related Examples

- [Document Management](../document/) - Manage parent documents
- [Child Chunk Management](../chunk/) - Create sub-segments
- [Dataset Management](../dataset/) - Query segmented content
- [Tag Management](../tag/) - Organize segments with tags
