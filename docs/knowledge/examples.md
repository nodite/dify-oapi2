# Knowledge Base API Examples

This document provides practical examples for using all 33 Knowledge Base APIs in real-world scenarios.

## Table of Contents

- [Setup and Configuration](#setup-and-configuration)
- [Dataset Management Examples](#dataset-management-examples)
- [Document Processing Examples](#document-processing-examples)
- [Content Segmentation Examples](#content-segmentation-examples)
- [Child Chunks Management Examples](#child-chunks-management-examples)
- [Tag Management Examples](#tag-management-examples)
- [Model Management Examples](#model-management-examples)
- [Complete Workflow Examples](#complete-workflow-examples)
- [Error Handling Examples](#error-handling-examples)
- [Async Examples](#async-examples)

## Setup and Configuration

```python
import os
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption

# Environment setup
API_KEY = os.getenv("DIFY_API_KEY")
if not API_KEY:
    raise ValueError("DIFY_API_KEY environment variable is required")

DOMAIN = os.getenv("DIFY_DOMAIN", "https://api.dify.ai")

# Initialize client
client = Client.builder().domain(DOMAIN).build()
request_option = RequestOption.builder().api_key(API_KEY).build()

# Access knowledge resources
knowledge = client.knowledge.v1
```

## Dataset Management Examples

### Creating a Knowledge Base

```python
from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.retrieval_model import RetrievalModel

def create_product_knowledge_base():
    """Create a knowledge base for product documentation."""
    
    # Configure retrieval model for hybrid search
    retrieval_model = (
        RetrievalModel.builder()
        .search_method("hybrid_search")
        .reranking_enable(True)
        .top_k(10)
        .score_threshold_enabled(True)
        .score_threshold(0.7)
        .weights(0.5)
        .build()
    )
    
    # Build request body
    request_body = (
        CreateDatasetRequestBody.builder()
        .name("[Example] Product Documentation")
        .description("Comprehensive product documentation and user guides")
        .indexing_technique("high_quality")
        .permission("all_team_members")
        .provider("vendor")
        .embedding_model("text-embedding-ada-002")
        .embedding_model_provider("openai")
        .retrieval_model(retrieval_model)
        .build()
    )
    
    request = CreateDatasetRequest.builder().request_body(request_body).build()
    
    try:
        response = knowledge.dataset.create(request, request_option)
        print(f"✅ Created dataset: {response.name} (ID: {response.id})")
        return response.id
    except Exception as e:
        print(f"❌ Failed to create dataset: {e}")
        return None

# Usage
dataset_id = create_product_knowledge_base()
```

### Listing and Filtering Datasets

```python
from dify_oapi.api.knowledge.v1.model.list_datasets_request import ListDatasetsRequest

def list_example_datasets():
    """List all example datasets with pagination."""
    
    page = 1
    all_datasets = []
    
    while True:
        request = (
            ListDatasetsRequest.builder()
            .page(page)
            .limit(20)
            .build()
        )
        
        response = knowledge.dataset.list(request, request_option)
        
        # Filter example datasets
        example_datasets = [
            dataset for dataset in response.data 
            if dataset.name and "[Example]" in dataset.name
        ]
        
        all_datasets.extend(example_datasets)
        
        if not response.has_more:
            break
            
        page += 1
    
    print(f"Found {len(all_datasets)} example datasets:")
    for dataset in all_datasets:
        print(f"  - {dataset.name} ({dataset.document_count} documents)")
    
    return all_datasets

# Usage
datasets = list_example_datasets()
```

### Searching Content in Dataset

```python
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request import RetrieveFromDatasetRequest
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request_body import RetrieveFromDatasetRequestBody

def search_knowledge_base(dataset_id: str, query: str):
    """Search for relevant content in a knowledge base."""
    
    request_body = (
        RetrieveFromDatasetRequestBody.builder()
        .query(query)
        .top_k(5)
        .score_threshold(0.6)
        .build()
    )
    
    request = (
        RetrieveFromDatasetRequest.builder()
        .dataset_id(dataset_id)
        .request_body(request_body)
        .build()
    )
    
    try:
        response = knowledge.dataset.retrieve(request, request_option)
        
        print(f"🔍 Search results for: '{query}'")
        print(f"Found {len(response.records)} relevant segments:")
        
        for i, record in enumerate(response.records, 1):
            segment = record.segment
            score = record.score
            print(f"\n{i}. Score: {score:.3f}")
            print(f"   Content: {segment.content[:200]}...")
            print(f"   Document: {segment.document.name}")
        
        return response.records
        
    except Exception as e:
        print(f"❌ Search failed: {e}")
        return []

# Usage
if dataset_id:
    results = search_knowledge_base(dataset_id, "How to install the product?")
```

## Document Processing Examples

### Uploading Documents from Files

```python
from dify_oapi.api.knowledge.v1.model.create_document_by_file_request import CreateDocumentByFileRequest
from dify_oapi.api.knowledge.v1.model.create_document_by_file_request_body import CreateDocumentByFileRequestBody
from dify_oapi.api.knowledge.v1.model.process_rule import ProcessRule
from io import BytesIO

def upload_document_file(dataset_id: str, file_path: str):
    """Upload a document file to the knowledge base."""
    
    try:
        # Read file content
        with open(file_path, 'rb') as f:
            file_content = BytesIO(f.read())
        
        # Configure processing rules
        process_rule = (
            ProcessRule.builder()
            .mode("automatic")
            .build()
        )
        
        # Build request body
        request_body = (
            CreateDocumentByFileRequestBody.builder()
            .indexing_technique("high_quality")
            .doc_form("text_model")
            .doc_language("English")
            .process_rule(process_rule)
            .build()
        )
        
        # Build request
        request = (
            CreateDocumentByFileRequest.builder()
            .dataset_id(dataset_id)
            .request_body(request_body)
            .file(file_content, os.path.basename(file_path))
            .build()
        )
        
        response = knowledge.document.create_by_file(request, request_option)
        
        print(f"✅ Document uploaded: {response.document.name}")
        print(f"   Document ID: {response.document.id}")
        print(f"   Batch ID: {response.batch}")
        
        return response.document.id, response.batch
        
    except Exception as e:
        print(f"❌ File upload failed: {e}")
        return None, None

# Usage
if dataset_id:
    doc_id, batch_id = upload_document_file(dataset_id, "manual.pdf")
```

### Creating Documents from Text

```python
from dify_oapi.api.knowledge.v1.model.create_document_by_text_request import CreateDocumentByTextRequest
from dify_oapi.api.knowledge.v1.model.create_document_by_text_request_body import CreateDocumentByTextRequestBody

def create_text_document(dataset_id: str, title: str, content: str):
    """Create a document from text content."""
    
    request_body = (
        CreateDocumentByTextRequestBody.builder()
        .name(f"[Example] {title}")
        .text(content)
        .indexing_technique("high_quality")
        .doc_form("text_model")
        .doc_language("English")
        .build()
    )
    
    request = (
        CreateDocumentByTextRequest.builder()
        .dataset_id(dataset_id)
        .request_body(request_body)
        .build()
    )
    
    try:
        response = knowledge.document.create_by_text(request, request_option)
        
        print(f"✅ Text document created: {response.document.name}")
        print(f"   Document ID: {response.document.id}")
        print(f"   Status: {response.document.indexing_status}")
        
        return response.document.id, response.batch
        
    except Exception as e:
        print(f"❌ Text document creation failed: {e}")
        return None, None

# Usage
sample_content = """
# Product Installation Guide

## Prerequisites
- System requirements: Windows 10 or later
- Memory: 4GB RAM minimum
- Storage: 2GB available space

## Installation Steps
1. Download the installer from our website
2. Run the installer as administrator
3. Follow the setup wizard
4. Restart your computer when prompted

## Troubleshooting
If you encounter issues during installation:
- Check system requirements
- Disable antivirus temporarily
- Contact support if problems persist
"""

if dataset_id:
    text_doc_id, text_batch_id = create_text_document(
        dataset_id, 
        "Installation Guide", 
        sample_content
    )
```

### Monitoring Document Processing

```python
from dify_oapi.api.knowledge.v1.model.get_batch_indexing_status_request import GetBatchIndexingStatusRequest
import time

def monitor_document_processing(dataset_id: str, batch_id: str, timeout: int = 300):
    """Monitor document processing status with timeout."""
    
    request = (
        GetBatchIndexingStatusRequest.builder()
        .dataset_id(dataset_id)
        .batch(batch_id)
        .build()
    )
    
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            response = knowledge.document.get_batch_status(request, request_option)
            
            status = response.indexing_status
            completed = response.completed_segments or 0
            total = response.total_segments or 0
            
            print(f"📊 Processing status: {status}")
            if total > 0:
                progress = (completed / total) * 100
                print(f"   Progress: {completed}/{total} segments ({progress:.1f}%)")
            
            if status in ["completed", "error", "paused"]:
                if status == "completed":
                    print("✅ Document processing completed!")
                elif status == "error":
                    print(f"❌ Processing failed: {response.error}")
                else:
                    print(f"⏸️ Processing paused")
                break
            
            time.sleep(5)  # Wait 5 seconds before next check
            
        except Exception as e:
            print(f"❌ Status check failed: {e}")
            break
    else:
        print(f"⏰ Timeout after {timeout} seconds")

# Usage
if batch_id:
    monitor_document_processing(dataset_id, batch_id)
```

### Batch Document Status Management

```python
from dify_oapi.api.knowledge.v1.model.update_document_status_request import UpdateDocumentStatusRequest
from dify_oapi.api.knowledge.v1.model.update_document_status_request_body import UpdateDocumentStatusRequestBody
from dify_oapi.api.knowledge.v1.model.list_documents_request import ListDocumentsRequest

def manage_example_documents(dataset_id: str, action: str):
    """Enable, disable, archive, or unarchive example documents."""
    
    # First, list all example documents
    list_request = (
        ListDocumentsRequest.builder()
        .dataset_id(dataset_id)
        .limit(100)
        .build()
    )
    
    list_response = knowledge.document.list(list_request, request_option)
    
    # Filter example documents
    example_docs = [
        doc for doc in list_response.data 
        if doc.name and "[Example]" in doc.name
    ]
    
    if not example_docs:
        print("No example documents found")
        return
    
    document_ids = [doc.id for doc in example_docs]
    
    # Update status
    request_body = (
        UpdateDocumentStatusRequestBody.builder()
        .document_ids(document_ids)
        .build()
    )
    
    request = (
        UpdateDocumentStatusRequest.builder()
        .dataset_id(dataset_id)
        .action(action)
        .request_body(request_body)
        .build()
    )
    
    try:
        response = knowledge.document.update_status(request, request_option)
        print(f"✅ {action.title()}d {len(document_ids)} example documents")
        
    except Exception as e:
        print(f"❌ Status update failed: {e}")

# Usage
if dataset_id:
    # Enable all example documents
    manage_example_documents(dataset_id, "enable")
```

## Content Segmentation Examples

### Creating Custom Segments

```python
from dify_oapi.api.knowledge.v1.model.create_segment_request import CreateSegmentRequest
from dify_oapi.api.knowledge.v1.model.create_segment_request_body import CreateSegmentRequestBody
from dify_oapi.api.knowledge.v1.model.segment_info import SegmentInfo

def create_custom_segments(dataset_id: str, document_id: str):
    """Create custom segments for better content organization."""
    
    segments = [
        SegmentInfo.builder()
        .content("System Requirements: Windows 10 or later, 4GB RAM, 2GB storage")
        .keywords(["requirements", "system", "windows", "ram", "storage"])
        .build(),
        
        SegmentInfo.builder()
        .content("Installation Process: Download installer, run as admin, follow wizard")
        .keywords(["installation", "download", "admin", "wizard"])
        .build(),
        
        SegmentInfo.builder()
        .content("Troubleshooting: Check requirements, disable antivirus, contact support")
        .keywords(["troubleshooting", "antivirus", "support", "help"])
        .build()
    ]
    
    request_body = CreateSegmentRequestBody.builder().segments(segments).build()
    
    request = (
        CreateSegmentRequest.builder()
        .dataset_id(dataset_id)
        .document_id(document_id)
        .request_body(request_body)
        .build()
    )
    
    try:
        response = knowledge.segment.create(request, request_option)
        print(f"✅ Created {len(segments)} custom segments")
        return response.data
        
    except Exception as e:
        print(f"❌ Segment creation failed: {e}")
        return []

# Usage
if dataset_id and text_doc_id:
    segments = create_custom_segments(dataset_id, text_doc_id)
```

### Listing and Filtering Segments

```python
from dify_oapi.api.knowledge.v1.model.list_segments_request import ListSegmentsRequest

def analyze_document_segments(dataset_id: str, document_id: str):
    """Analyze segments in a document with filtering."""
    
    # List all segments
    request = (
        ListSegmentsRequest.builder()
        .dataset_id(dataset_id)
        .document_id(document_id)
        .status("completed")
        .build()
    )
    
    try:
        response = knowledge.segment.list(request, request_option)
        
        print(f"📄 Document segments analysis:")
        print(f"   Total segments: {len(response.data)}")
        
        # Analyze segment characteristics
        total_words = sum(seg.word_count or 0 for seg in response.data)
        total_tokens = sum(seg.tokens or 0 for seg in response.data)
        
        print(f"   Total words: {total_words}")
        print(f"   Total tokens: {total_tokens}")
        print(f"   Average words per segment: {total_words / len(response.data):.1f}")
        
        # Show segments with keywords
        segments_with_keywords = [seg for seg in response.data if seg.keywords]
        print(f"   Segments with keywords: {len(segments_with_keywords)}")
        
        for i, segment in enumerate(response.data[:3], 1):
            print(f"\n   Segment {i}:")
            print(f"     Content: {segment.content[:100]}...")
            print(f"     Words: {segment.word_count}, Tokens: {segment.tokens}")
            if segment.keywords:
                print(f"     Keywords: {', '.join(segment.keywords)}")
        
        return response.data
        
    except Exception as e:
        print(f"❌ Segment analysis failed: {e}")
        return []

# Usage
if dataset_id and text_doc_id:
    segments = analyze_document_segments(dataset_id, text_doc_id)
```

### Updating Segment Content

```python
from dify_oapi.api.knowledge.v1.model.update_segment_request import UpdateSegmentRequest
from dify_oapi.api.knowledge.v1.model.update_segment_request_body import UpdateSegmentRequestBody
from dify_oapi.api.knowledge.v1.model.segment_data import SegmentData

def enhance_segment_with_qa(dataset_id: str, document_id: str, segment_id: str):
    """Enhance a segment with Q&A format content."""
    
    segment_data = (
        SegmentData.builder()
        .content("""
Q: What are the system requirements for installation?
A: The system requirements are:
- Windows 10 or later operating system
- Minimum 4GB RAM (8GB recommended)
- 2GB available storage space
- Administrator privileges for installation
        """.strip())
        .answer("Windows 10+, 4GB RAM, 2GB storage, admin privileges required")
        .keywords(["requirements", "system", "windows", "ram", "storage", "admin"])
        .build()
    )
    
    request_body = UpdateSegmentRequestBody.builder().segment(segment_data).build()
    
    request = (
        UpdateSegmentRequest.builder()
        .dataset_id(dataset_id)
        .document_id(document_id)
        .segment_id(segment_id)
        .request_body(request_body)
        .build()
    )
    
    try:
        response = knowledge.segment.update(request, request_option)
        print("✅ Enhanced segment with Q&A format")
        return response
        
    except Exception as e:
        print(f"❌ Segment update failed: {e}")
        return None

# Usage
if segments and len(segments) > 0:
    first_segment_id = segments[0].id
    enhance_segment_with_qa(dataset_id, text_doc_id, first_segment_id)
```

## Child Chunks Management Examples

### Creating Sub-segments

```python
from dify_oapi.api.knowledge.v1.model.create_child_chunk_request import CreateChildChunkRequest
from dify_oapi.api.knowledge.v1.model.create_child_chunk_request_body import CreateChildChunkRequestBody

def create_detailed_chunks(dataset_id: str, document_id: str, segment_id: str):
    """Create detailed child chunks for granular content access."""
    
    chunks = [
        {
            "content": "Windows 10 or later is required for compatibility",
            "keywords": ["windows", "compatibility", "os"]
        },
        {
            "content": "4GB RAM minimum, 8GB recommended for optimal performance",
            "keywords": ["ram", "memory", "performance"]
        },
        {
            "content": "2GB storage space needed for installation files",
            "keywords": ["storage", "space", "installation"]
        },
        {
            "content": "Administrator privileges required for system-level installation",
            "keywords": ["admin", "privileges", "system"]
        }
    ]
    
    request_body = CreateChildChunkRequestBody.builder().chunks(chunks).build()
    
    request = (
        CreateChildChunkRequest.builder()
        .dataset_id(dataset_id)
        .document_id(document_id)
        .segment_id(segment_id)
        .request_body(request_body)
        .build()
    )
    
    try:
        response = knowledge.chunk.create(request, request_option)
        print(f"✅ Created {len(chunks)} child chunks")
        return response.data
        
    except Exception as e:
        print(f"❌ Child chunk creation failed: {e}")
        return []

# Usage
if segments and len(segments) > 0:
    first_segment_id = segments[0].id
    chunks = create_detailed_chunks(dataset_id, text_doc_id, first_segment_id)
```

### Managing Child Chunks

```python
from dify_oapi.api.knowledge.v1.model.list_child_chunks_request import ListChildChunksRequest
from dify_oapi.api.knowledge.v1.model.update_child_chunk_request import UpdateChildChunkRequest
from dify_oapi.api.knowledge.v1.model.update_child_chunk_request_body import UpdateChildChunkRequestBody

def manage_child_chunks(dataset_id: str, document_id: str, segment_id: str):
    """List and update child chunks."""
    
    # List existing child chunks
    list_request = (
        ListChildChunksRequest.builder()
        .dataset_id(dataset_id)
        .document_id(document_id)
        .segment_id(segment_id)
        .build()
    )
    
    try:
        list_response = knowledge.chunk.list(list_request, request_option)
        
        print(f"📋 Found {len(list_response.data)} child chunks:")
        
        for i, chunk in enumerate(list_response.data, 1):
            print(f"   {i}. {chunk.content[:50]}...")
            if chunk.keywords:
                print(f"      Keywords: {', '.join(chunk.keywords)}")
        
        # Update first chunk if exists
        if list_response.data:
            first_chunk = list_response.data[0]
            
            update_body = (
                UpdateChildChunkRequestBody.builder()
                .content(f"[Updated] {first_chunk.content}")
                .keywords(first_chunk.keywords + ["updated"] if first_chunk.keywords else ["updated"])
                .build()
            )
            
            update_request = (
                UpdateChildChunkRequest.builder()
                .dataset_id(dataset_id)
                .document_id(document_id)
                .segment_id(segment_id)
                .child_chunk_id(first_chunk.id)
                .request_body(update_body)
                .build()
            )
            
            update_response = knowledge.chunk.update(update_request, request_option)
            print("✅ Updated first child chunk")
        
        return list_response.data
        
    except Exception as e:
        print(f"❌ Child chunk management failed: {e}")
        return []

# Usage
if segments and len(segments) > 0:
    managed_chunks = manage_child_chunks(dataset_id, text_doc_id, first_segment_id)
```

## Tag Management Examples

### Creating and Organizing Tags

```python
from dify_oapi.api.knowledge.v1.model.create_tag_request import CreateTagRequest
from dify_oapi.api.knowledge.v1.model.create_tag_request_body import CreateTagRequestBody
from dify_oapi.api.knowledge.v1.model.list_tags_request import ListTagsRequest

def setup_knowledge_tags():
    """Create a comprehensive tagging system."""
    
    tags_to_create = [
        {"name": "[Example] Product Documentation", "type": "knowledge_type"},
        {"name": "[Example] User Guides", "type": "knowledge_type"},
        {"name": "[Example] Technical Specs", "type": "knowledge_type"},
        {"name": "[Example] Troubleshooting", "type": "custom"},
        {"name": "[Example] Installation", "type": "custom"},
        {"name": "[Example] Configuration", "type": "custom"}
    ]
    
    created_tags = []
    
    for tag_info in tags_to_create:
        request_body = (
            CreateTagRequestBody.builder()
            .name(tag_info["name"])
            .type(tag_info["type"])
            .build()
        )
        
        request = CreateTagRequest.builder().request_body(request_body).build()
        
        try:
            response = knowledge.tag.create(request, request_option)
            created_tags.append(response)
            print(f"✅ Created tag: {response.name} ({response.type})")
            
        except Exception as e:
            print(f"❌ Failed to create tag '{tag_info['name']}': {e}")
    
    return created_tags

def list_all_tags():
    """List all available tags by type."""
    
    for tag_type in ["knowledge_type", "custom"]:
        request = (
            ListTagsRequest.builder()
            .type(tag_type)
            .build()
        )
        
        try:
            response = knowledge.tag.list(request, request_option)
            
            print(f"\n🏷️ {tag_type.replace('_', ' ').title()} Tags:")
            for tag in response.data:
                if "[Example]" in tag.name:
                    print(f"   - {tag.name} (used by {tag.binding_count} datasets)")
            
        except Exception as e:
            print(f"❌ Failed to list {tag_type} tags: {e}")

# Usage
created_tags = setup_knowledge_tags()
list_all_tags()
```

### Binding Tags to Datasets

```python
from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request import BindTagsToDatasetRequest
from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request_body import BindTagsToDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.get_dataset_tags_request import GetDatasetTagsRequest

def organize_dataset_with_tags(dataset_id: str, tag_ids: list):
    """Bind relevant tags to a dataset."""
    
    request_body = (
        BindTagsToDatasetRequestBody.builder()
        .dataset_id(dataset_id)
        .tag_ids(tag_ids)
        .build()
    )
    
    request = BindTagsToDatasetRequest.builder().request_body(request_body).build()
    
    try:
        response = knowledge.tag.bind(request, request_option)
        print(f"✅ Bound {len(tag_ids)} tags to dataset")
        
        # Verify tags were bound
        verify_request = GetDatasetTagsRequest.builder().dataset_id(dataset_id).build()
        verify_response = knowledge.tag.get_dataset_tags(verify_request, request_option)
        
        print("📋 Dataset tags:")
        for tag in verify_response.data:
            print(f"   - {tag.name} ({tag.type})")
        
        return verify_response.data
        
    except Exception as e:
        print(f"❌ Tag binding failed: {e}")
        return []

# Usage
if dataset_id and created_tags:
    # Bind first 3 tags to the dataset
    tag_ids = [tag.id for tag in created_tags[:3]]
    bound_tags = organize_dataset_with_tags(dataset_id, tag_ids)
```

## Model Management Examples

### Exploring Available Models

```python
from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_request import GetTextEmbeddingModelsRequest

def explore_embedding_models():
    """Explore available text embedding models."""
    
    request = GetTextEmbeddingModelsRequest.builder().build()
    
    try:
        response = knowledge.model.embedding_models(request, request_option)
        
        print("🤖 Available Embedding Models:")
        print(f"   Total providers: {len(response.data)}")
        
        for provider in response.data:
            print(f"\n   Provider: {provider.provider}")
            print(f"   Status: {provider.status}")
            print(f"   Models: {len(provider.models)}")
            
            for model in provider.models[:3]:  # Show first 3 models
                print(f"     - {model.model}")
                print(f"       Type: {model.model_type}")
                print(f"       Status: {model.status}")
                if model.model_properties and hasattr(model.model_properties, 'context_size'):
                    print(f"       Context Size: {model.model_properties.context_size}")
                if model.deprecated:
                    print(f"       ⚠️ Deprecated")
        
        return response.data
        
    except Exception as e:
        print(f"❌ Failed to get embedding models: {e}")
        return []

# Usage
available_models = explore_embedding_models()
```

## Complete Workflow Examples

### End-to-End Knowledge Base Setup

```python
def complete_knowledge_base_workflow():
    """Complete workflow: Create dataset, upload documents, organize content."""
    
    print("🚀 Starting complete knowledge base workflow...")
    
    # Step 1: Create dataset
    print("\n1️⃣ Creating dataset...")
    dataset_id = create_product_knowledge_base()
    if not dataset_id:
        return
    
    # Step 2: Create tags
    print("\n2️⃣ Setting up tags...")
    tags = setup_knowledge_tags()
    
    # Step 3: Bind tags to dataset
    if tags:
        print("\n3️⃣ Organizing with tags...")
        tag_ids = [tag.id for tag in tags[:2]]
        organize_dataset_with_tags(dataset_id, tag_ids)
    
    # Step 4: Create text document
    print("\n4️⃣ Creating documentation...")
    doc_id, batch_id = create_text_document(
        dataset_id, 
        "Complete User Guide", 
        sample_content
    )
    
    # Step 5: Monitor processing
    if batch_id:
        print("\n5️⃣ Monitoring processing...")
        monitor_document_processing(dataset_id, batch_id, timeout=60)
    
    # Step 6: Create custom segments
    if doc_id:
        print("\n6️⃣ Creating custom segments...")
        segments = create_custom_segments(dataset_id, doc_id)
        
        # Step 7: Create child chunks
        if segments:
            print("\n7️⃣ Creating detailed chunks...")
            first_segment_id = segments[0].id
            create_detailed_chunks(dataset_id, doc_id, first_segment_id)
    
    # Step 8: Test search functionality
    print("\n8️⃣ Testing search...")
    search_knowledge_base(dataset_id, "installation requirements")
    
    print("\n✅ Complete workflow finished!")
    return dataset_id

# Run complete workflow
workflow_dataset_id = complete_knowledge_base_workflow()
```

### Cleanup Example Resources

```python
from dify_oapi.api.knowledge.v1.model.delete_dataset_request import DeleteDatasetRequest
from dify_oapi.api.knowledge.v1.model.delete_tag_request import DeleteTagRequest
from dify_oapi.api.knowledge.v1.model.delete_tag_request_body import DeleteTagRequestBody

def cleanup_example_resources():
    """Clean up all example resources."""
    
    print("🧹 Cleaning up example resources...")
    
    # Clean up datasets
    datasets = list_example_datasets()
    for dataset in datasets:
        try:
            request = DeleteDatasetRequest.builder().dataset_id(dataset.id).build()
            knowledge.dataset.delete(request, request_option)
            print(f"✅ Deleted dataset: {dataset.name}")
        except Exception as e:
            print(f"❌ Failed to delete dataset {dataset.name}: {e}")
    
    # Clean up tags
    for tag_type in ["knowledge_type", "custom"]:
        try:
            list_request = ListTagsRequest.builder().type(tag_type).build()
            list_response = knowledge.tag.list(list_request, request_option)
            
            for tag in list_response.data:
                if "[Example]" in tag.name:
                    delete_body = DeleteTagRequestBody.builder().tag_id(tag.id).build()
                    delete_request = DeleteTagRequest.builder().request_body(delete_body).build()
                    knowledge.tag.delete(delete_request, request_option)
                    print(f"✅ Deleted tag: {tag.name}")
                    
        except Exception as e:
            print(f"❌ Failed to clean up {tag_type} tags: {e}")
    
    print("✅ Cleanup completed!")

# Uncomment to run cleanup
# cleanup_example_resources()
```

## Error Handling Examples

### Robust Error Handling

```python
from dify_oapi.core.model.base_response import BaseResponse

def robust_dataset_operation(operation_name: str, operation_func):
    """Execute dataset operation with comprehensive error handling."""
    
    max_retries = 3
    retry_delay = 2
    
    for attempt in range(max_retries):
        try:
            print(f"🔄 Attempting {operation_name} (attempt {attempt + 1}/{max_retries})")
            
            result = operation_func()
            
            # Check if result is a BaseResponse
            if isinstance(result, BaseResponse):
                if hasattr(result, 'success') and not result.success:
                    print(f"❌ Operation failed: {result.code} - {result.msg}")
                    if attempt < max_retries - 1:
                        time.sleep(retry_delay)
                        continue
                    return None
            
            print(f"✅ {operation_name} completed successfully")
            return result
            
        except Exception as e:
            print(f"❌ {operation_name} failed: {str(e)}")
            
            if attempt < max_retries - 1:
                print(f"⏳ Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff
            else:
                print(f"💥 {operation_name} failed after {max_retries} attempts")
                return None
    
    return None

# Usage example
def safe_create_dataset():
    return create_product_knowledge_base()

result = robust_dataset_operation("Dataset Creation", safe_create_dataset)
```

### Validation and Preprocessing

```python
def validate_and_process_content(content: str, max_length: int = 10000):
    """Validate and preprocess content before upload."""
    
    if not content or not content.strip():
        raise ValueError("Content cannot be empty")
    
    content = content.strip()
    
    if len(content) > max_length:
        print(f"⚠️ Content truncated from {len(content)} to {max_length} characters")
        content = content[:max_length] + "..."
    
    # Remove excessive whitespace
    import re
    content = re.sub(r'\s+', ' ', content)
    
    # Validate encoding
    try:
        content.encode('utf-8')
    except UnicodeEncodeError:
        raise ValueError("Content contains invalid characters")
    
    return content

def safe_create_text_document(dataset_id: str, title: str, content: str):
    """Safely create text document with validation."""
    
    try:
        # Validate inputs
        if not dataset_id:
            raise ValueError("Dataset ID is required")
        
        if not title or len(title.strip()) < 3:
            raise ValueError("Title must be at least 3 characters long")
        
        # Process content
        processed_content = validate_and_process_content(content)
        
        # Create document
        return create_text_document(dataset_id, title, processed_content)
        
    except ValueError as e:
        print(f"❌ Validation error: {e}")
        return None, None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None, None

# Usage
if dataset_id:
    safe_doc_id, safe_batch_id = safe_create_text_document(
        dataset_id,
        "Validated Document",
        "This is validated content that meets all requirements."
    )
```

## Async Examples

### Concurrent Operations

```python
import asyncio
from typing import List, Tuple

async def async_create_multiple_documents(
    dataset_id: str, 
    documents: List[Tuple[str, str]]
) -> List[Tuple[str, str]]:
    """Create multiple documents concurrently."""
    
    async def create_single_doc(title: str, content: str):
        """Create a single document asynchronously."""
        try:
            request_body = (
                CreateDocumentByTextRequestBody.builder()
                .name(f"[Example] {title}")
                .text(content)
                .indexing_technique("high_quality")
                .doc_form("text_model")
                .doc_language("English")
                .build()
            )
            
            request = (
                CreateDocumentByTextRequest.builder()
                .dataset_id(dataset_id)
                .request_body(request_body)
                .build()
            )
            
            response = await knowledge.document.acreate_by_text(request, request_option)
            return response.document.id, response.batch
            
        except Exception as e:
            print(f"❌ Failed to create document '{title}': {e}")
            return None, None
    
    # Create all documents concurrently
    tasks = [create_single_doc(title, content) for title, content in documents]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Filter successful results
    successful_results = [
        result for result in results 
        if not isinstance(result, Exception) and result[0] is not None
    ]
    
    print(f"✅ Created {len(successful_results)} documents concurrently")
    return successful_results

async def async_workflow_example():
    """Example of async workflow."""
    
    if not dataset_id:
        print("❌ No dataset available for async example")
        return
    
    # Prepare multiple documents
    documents = [
        ("Quick Start Guide", "Quick start instructions for new users..."),
        ("Advanced Configuration", "Advanced configuration options and settings..."),
        ("API Reference", "Complete API reference documentation..."),
        ("Troubleshooting FAQ", "Frequently asked questions and solutions...")
    ]
    
    # Create documents concurrently
    results = await async_create_multiple_documents(dataset_id, documents)
    
    # Monitor all batches concurrently
    if results:
        batch_ids = [batch_id for _, batch_id in results if batch_id]
        
        async def monitor_batch(batch_id: str):
            """Monitor a single batch asynchronously."""
            request = (
                GetBatchIndexingStatusRequest.builder()
                .dataset_id(dataset_id)
                .batch(batch_id)
                .build()
            )
            
            while True:
                try:
                    response = await knowledge.document.aget_batch_status(request, request_option)
                    
                    if response.indexing_status in ["completed", "error", "paused"]:
                        return response.indexing_status
                    
                    await asyncio.sleep(2)
                    
                except Exception as e:
                    print(f"❌ Batch monitoring failed: {e}")
                    return "error"
        
        # Monitor all batches concurrently
        monitoring_tasks = [monitor_batch(batch_id) for batch_id in batch_ids]
        statuses = await asyncio.gather(*monitoring_tasks)
        
        completed_count = sum(1 for status in statuses if status == "completed")
        print(f"✅ {completed_count}/{len(batch_ids)} batches completed successfully")

# Run async example
if dataset_id:
    asyncio.run(async_workflow_example())
```

### Async Search and Analysis

```python
async def async_comprehensive_search(dataset_id: str, queries: List[str]):
    """Perform comprehensive search analysis asynchronously."""
    
    async def search_single_query(query: str):
        """Search for a single query asynchronously."""
        try:
            request_body = (
                RetrieveFromDatasetRequestBody.builder()
                .query(query)
                .top_k(3)
                .score_threshold(0.5)
                .build()
            )
            
            request = (
                RetrieveFromDatasetRequest.builder()
                .dataset_id(dataset_id)
                .request_body(request_body)
                .build()
            )
            
            response = await knowledge.dataset.aretrieve(request, request_option)
            return query, response.records
            
        except Exception as e:
            print(f"❌ Search failed for '{query}': {e}")
            return query, []
    
    # Perform all searches concurrently
    search_tasks = [search_single_query(query) for query in queries]
    results = await asyncio.gather(*search_tasks)
    
    # Analyze results
    print("🔍 Comprehensive Search Results:")
    total_results = 0
    
    for query, records in results:
        print(f"\n   Query: '{query}'")
        print(f"   Results: {len(records)}")
        total_results += len(records)
        
        for i, record in enumerate(records[:2], 1):
            print(f"     {i}. Score: {record.score:.3f}")
            print(f"        Content: {record.segment.content[:80]}...")
    
    print(f"\n✅ Total search results: {total_results}")
    return results

# Example usage
search_queries = [
    "installation requirements",
    "troubleshooting steps",
    "configuration options",
    "system compatibility"
]

if dataset_id:
    asyncio.run(async_comprehensive_search(dataset_id, search_queries))
```

## Summary

These examples demonstrate the comprehensive capabilities of the Knowledge Base API module:

1. **Dataset Management**: Creating, organizing, and managing knowledge bases
2. **Document Processing**: Uploading files, creating text documents, monitoring processing
3. **Content Segmentation**: Creating custom segments for better organization
4. **Child Chunks**: Managing granular content pieces
5. **Tag Management**: Organizing datasets with metadata tags
6. **Model Management**: Exploring available embedding models
7. **Error Handling**: Robust error handling and validation
8. **Async Operations**: Concurrent processing for better performance

The examples follow best practices including:
- ✅ Environment variable validation
- ✅ "[Example]" prefix for safety
- ✅ Comprehensive error handling
- ✅ Resource cleanup procedures
- ✅ Type safety with builder patterns
- ✅ Both sync and async support
- ✅ Real-world usage scenarios

Use these examples as templates for building your own knowledge management applications with the Dify Knowledge Base API.