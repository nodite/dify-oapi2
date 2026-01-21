# Knowledge Dataset Management Examples

This directory contains examples for managing datasets in the Knowledge Base API (6 APIs). Datasets are the top-level containers for organizing knowledge content and serve as the foundation for all knowledge management operations.

## 📋 Available Examples

### Core Operations
- **`create_dataset.py`** - Create new datasets with configuration
- **`get_dataset.py`** - Retrieve dataset information and settings
- **`list_datasets.py`** - List all datasets with pagination and filtering
- **`update_dataset.py`** - Update dataset configuration and metadata
- **`delete_dataset.py`** - Delete datasets and all contained content

### Query Operations
- **`retrieve_from_dataset.py`** - Query and retrieve information from datasets

## 🚀 Quick Start

### Create a Dataset

```python
from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody

req_body = (
    CreateDatasetRequestBody.builder()
    .name("Product Documentation")
    .description("Comprehensive product documentation and FAQs")
    .permission("only_me")  # or "all_team_members"
    .build()
)

req = CreateDatasetRequest.builder().request_body(req_body).build()
response = client.knowledge.v1.dataset.create_dataset(req, req_option)

print(f"Dataset created with ID: {response.id}")
```

### List Datasets

```python
from dify_oapi.api.knowledge.v1.model.list_datasets_request import ListDatasetsRequest

req = ListDatasetsRequest.builder()
    .page(1)
    .limit(20)
    .build()

response = client.knowledge.v1.dataset.list_datasets(req, req_option)
for dataset in response.data:
    print(f"ID: {dataset.id}, Name: {dataset.name}")
```

### Query Dataset

```python
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request import RetrieveFromDatasetRequest
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request_body import RetrieveFromDatasetRequestBody

req_body = (
    RetrieveFromDatasetRequestBody.builder()
    .query("How to install the product?")
    .retrieval_model({
        "search_method": "semantic_search",
        "reranking_enable": True,
        "reranking_model": {"reranking_provider_name": "cohere"},
        "top_k": 5,
        "score_threshold": 0.5
    })
    .build()
)

req = RetrieveFromDatasetRequest.builder()
    .dataset_id("your-dataset-id")
    .request_body(req_body)
    .build()

response = client.knowledge.v1.dataset.retrieve_from_dataset(req, req_option)
for record in response.query_result:
    print(f"Score: {record.score}, Content: {record.content}")
```

## 🔧 Features

### Dataset Management APIs (6 APIs)
- **Create Dataset**: Initialize new knowledge containers with configuration
- **Get Dataset**: Retrieve detailed dataset information and settings
- **List Datasets**: Browse all datasets with pagination and filtering
- **Update Dataset**: Modify dataset configuration and metadata
- **Delete Dataset**: Remove datasets and all contained content
- **Retrieve from Dataset**: Query and search dataset content

### Dataset Configuration
- **Access Control**: Granular permissions ("only_me" or "all_team_members")
- **Rich Metadata**: Comprehensive description and categorization
- **Indexing Settings**: Advanced indexing and retrieval configuration
- **Tag Integration**: Organize datasets with hierarchical tagging
- **Performance Tuning**: Optimize for specific use cases

### Advanced Retrieval
- **Multiple Search Methods**: Semantic, keyword, and hybrid search
- **Intelligent Reranking**: Improve result quality with ML models
- **Flexible Filtering**: Score thresholds, result limits, and custom criteria
- **Scoring Strategies**: Custom weighting and ranking algorithms
- **Real-time Queries**: Low-latency search with caching optimization

### Enterprise Features
- **Bulk Operations**: Efficient handling of multiple datasets
- **Version Control**: Track dataset changes and rollback capabilities
- **Analytics**: Monitor usage patterns and performance metrics
- **API Integration**: Seamless connection with Chat, Completion, and Workflow APIs
- **Scalability**: Handle large-scale knowledge bases efficiently

## 📖 Retrieval Models

### Search Methods
- **`semantic_search`**: Vector-based semantic similarity
- **`full_text_search`**: Traditional keyword-based search
- **`hybrid_search`**: Combination of semantic and keyword search

### Reranking Options
```python
reranking_model = {
    "reranking_provider_name": "cohere",  # or other providers
    "reranking_model_name": "rerank-english-v2.0"
}
```

### Advanced Parameters
```python
retrieval_model = {
    "search_method": "hybrid_search",
    "reranking_enable": True,
    "reranking_model": reranking_model,
    "top_k": 10,
    "score_threshold": 0.3,
    "reranking_free_mode": False
}
```

## 📚 Best Practices

1. **Descriptive Names**: Use clear, descriptive dataset names
2. **Proper Permissions**: Set appropriate access permissions
3. **Regular Updates**: Keep dataset content current
4. **Optimal Configuration**: Tune retrieval settings for your use case
5. **Monitor Performance**: Track query performance and accuracy
6. **Organize with Tags**: Use tags for better organization
7. **Clean Up**: Remove unused datasets to maintain performance

## 🔗 Related Examples

- [Document Management](../document/) - Add content to datasets
- [Tag Management](../tag/) - Organize datasets with tags
- [Segment Management](../segment/) - Fine-grained content management
