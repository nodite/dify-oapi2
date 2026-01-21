# Knowledge Tag Management Examples

This directory contains examples for managing tags in the Knowledge Base API (7 APIs). Tags provide a flexible way to organize, categorize, and filter datasets and their content, enabling better knowledge organization and retrieval.

## 📋 Available Examples

### Core Tag Operations
- **`create_tag.py`** - Create new tags with descriptions and metadata
- **`list_tags.py`** - List all available tags with pagination
- **`update_tag.py`** - Update tag information and descriptions
- **`delete_tag.py`** - Delete tags from the system

### Dataset Tag Management
- **`bind_tags_to_dataset.py`** - Associate tags with datasets
- **`unbind_tags_from_dataset.py`** - Remove tag associations from datasets
- **`get_dataset_tags.py`** - Retrieve all tags associated with a dataset

## 🚀 Quick Start

### Create Tag

```python
from dify_oapi.api.knowledge.v1.model.create_tag_request import CreateTagRequest
from dify_oapi.api.knowledge.v1.model.create_tag_request_body import CreateTagRequestBody

req_body = (
    CreateTagRequestBody.builder()
    .name("Technical Documentation")
    .description("Tag for technical documentation and API references")
    .build()
)

req = CreateTagRequest.builder().request_body(req_body).build()
response = client.knowledge.v1.tag.create_tag(req, req_option)
print(f"Tag created with ID: {response.id}")
```

### Bind Tags to Dataset

```python
from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request import BindTagsToDatasetRequest
from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request_body import BindTagsToDatasetRequestBody

req_body = (
    BindTagsToDatasetRequestBody.builder()
    .tag_ids(["tag-id-1", "tag-id-2", "tag-id-3"])
    .build()
)

req = BindTagsToDatasetRequest.builder()
    .dataset_id("your-dataset-id")
    .request_body(req_body)
    .build()

response = client.knowledge.v1.tag.bind_tags_to_dataset(req, req_option)
```

### List Dataset Tags

```python
from dify_oapi.api.knowledge.v1.model.get_dataset_tags_request import GetDatasetTagsRequest

req = GetDatasetTagsRequest.builder()
    .dataset_id("your-dataset-id")
    .build()

response = client.knowledge.v1.tag.get_dataset_tags(req, req_option)
for tag in response.data:
    print(f"Tag: {tag.name} - {tag.description}")
```

## 🔧 Features

### Tag Management APIs (7 APIs)
- **Create Tag**: Add new tags with custom names and descriptions
- **List Tags**: Browse all available tags with pagination support
- **Update Tag**: Modify tag information and metadata
- **Delete Tag**: Remove tags and their associations
- **Bind Tags to Dataset**: Associate multiple tags with datasets
- **Unbind Tags from Dataset**: Remove tag associations
- **Get Dataset Tags**: Retrieve all tags for a specific dataset

### Organization Features
- **Flexible Categorization**: Create custom tag hierarchies and categories
- **Multi-tag Support**: Associate multiple tags with single datasets
- **Descriptive Metadata**: Rich descriptions for better tag understanding
- **Batch Operations**: Efficiently manage multiple tag associations
- **Search Integration**: Use tags to filter and organize search results

### Advanced Capabilities
- **Tag Hierarchies**: Create parent-child tag relationships
- **Usage Analytics**: Track tag usage and popularity
- **Auto-suggestions**: Get tag recommendations based on content
- **Bulk Management**: Handle large-scale tag operations efficiently
- **Integration**: Seamless integration with dataset and document management

## 📖 Use Cases

### Content Organization
- **Topic Classification**: Organize content by subject matter
- **Department Tagging**: Categorize by organizational departments
- **Priority Levels**: Tag content by importance or urgency
- **Content Types**: Distinguish between documentation, FAQs, tutorials
- **Language Tags**: Organize multilingual content

### Search Enhancement
- **Filtered Search**: Enable tag-based content filtering
- **Faceted Navigation**: Provide tag-based browsing interfaces
- **Content Discovery**: Help users find related content through tags
- **Recommendation Systems**: Suggest content based on tag similarities
- **Analytics**: Track content usage patterns by tags

## 📚 Best Practices

### Tag Design
1. **Consistent Naming**: Use clear, consistent tag naming conventions
2. **Descriptive Tags**: Provide meaningful descriptions for all tags
3. **Hierarchical Structure**: Organize tags in logical hierarchies
4. **Avoid Duplication**: Prevent similar or duplicate tags
5. **Regular Maintenance**: Periodically review and clean up unused tags

### Tag Usage
1. **Multiple Tags**: Use multiple relevant tags per dataset
2. **Specific Tags**: Prefer specific over generic tags
3. **User-Friendly**: Choose tags that users will understand
4. **Searchable**: Use tags that align with user search patterns
5. **Scalable**: Design tag systems that can grow with content

## 🔗 Integration Examples

### With Dataset Management
```python
# Create dataset with immediate tag binding
dataset_response = client.knowledge.v1.dataset.create_dataset(dataset_req, req_option)
tag_bind_req = BindTagsToDatasetRequest.builder()
    .dataset_id(dataset_response.id)
    .request_body(BindTagsToDatasetRequestBody.builder()
        .tag_ids(["documentation", "api-reference"])
        .build())
    .build()
client.knowledge.v1.tag.bind_tags_to_dataset(tag_bind_req, req_option)
```

### With Search and Retrieval
```python
# Filter datasets by tags during search
filtered_datasets = client.knowledge.v1.dataset.list_datasets(
    ListDatasetsRequest.builder()
        .tag_ids(["technical", "public"])
        .build(),
    req_option
)
```

## 📚 Environment Variables

```bash
export DOMAIN="https://api.dify.ai"
export KNOWLEDGE_KEY="your-knowledge-api-key"
export DATASET_ID="your-dataset-id"
```

## 🔗 Related Examples

- [Dataset Management](../dataset/) - Organize datasets with tags
- [Document Management](../document/) - Tag-based document organization
- [Model Management](../model/) - Tag embedding models and configurations
