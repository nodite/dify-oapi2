"""Integration tests for Knowledge service class."""

from dify_oapi.api.knowledge.service import Knowledge
from dify_oapi.api.knowledge.v1.version import V1
from dify_oapi.core.model.config import Config


class TestKnowledgeServiceIntegration:
    """Test Knowledge service integration."""

    def test_knowledge_service_initialization(self) -> None:
        """Test Knowledge service initialization."""
        config = Config()
        knowledge = Knowledge(config)

        # Test V1 is properly initialized
        assert isinstance(knowledge.v1, V1)
        assert knowledge.v1 is not None

    def test_knowledge_service_v1_access(self) -> None:
        """Test Knowledge service V1 access."""
        config = Config()
        knowledge = Knowledge(config)

        # Test V1 can be accessed
        v1 = knowledge.v1
        assert isinstance(v1, V1)

        # Test all 6 resources are accessible through V1
        assert hasattr(v1, "dataset")
        assert hasattr(v1, "document")
        assert hasattr(v1, "segment")
        assert hasattr(v1, "chunk")
        assert hasattr(v1, "tag")
        assert hasattr(v1, "model")

    def test_knowledge_service_config_propagation(self) -> None:
        """Test config is properly propagated through service layers."""
        config = Config()
        knowledge = Knowledge(config)

        # Test config propagation through service -> V1 -> resources
        assert knowledge.v1.dataset.config is config
        assert knowledge.v1.document.config is config
        assert knowledge.v1.segment.config is config
        assert knowledge.v1.chunk.config is config
        assert knowledge.v1.tag.config is config
        assert knowledge.v1.model.config is config

    def test_knowledge_service_resource_methods(self) -> None:
        """Test all resources have expected methods through service."""
        config = Config()
        knowledge = Knowledge(config)

        # Test dataset resource methods (6 APIs)
        dataset = knowledge.v1.dataset
        assert hasattr(dataset, "create")
        assert hasattr(dataset, "list")
        assert hasattr(dataset, "get")
        assert hasattr(dataset, "update")
        assert hasattr(dataset, "delete")
        assert hasattr(dataset, "retrieve")

        # Test document resource methods (10 APIs)
        document = knowledge.v1.document
        assert hasattr(document, "create_by_file")
        assert hasattr(document, "create_by_text")
        assert hasattr(document, "list")
        assert hasattr(document, "get")
        assert hasattr(document, "update_by_file")
        assert hasattr(document, "update_by_text")
        assert hasattr(document, "delete")
        assert hasattr(document, "update_status")
        assert hasattr(document, "get_batch_status")
        assert hasattr(document, "file_info")

        # Test segment resource methods (5 APIs)
        segment = knowledge.v1.segment
        assert hasattr(segment, "list")
        assert hasattr(segment, "create")
        assert hasattr(segment, "get")
        assert hasattr(segment, "update")
        assert hasattr(segment, "delete")

        # Test chunk resource methods (4 APIs)
        chunk = knowledge.v1.chunk
        assert hasattr(chunk, "list")
        assert hasattr(chunk, "create")
        assert hasattr(chunk, "update")
        assert hasattr(chunk, "delete")

        # Test tag resource methods (7 APIs)
        tag = knowledge.v1.tag
        assert hasattr(tag, "list")
        assert hasattr(tag, "create")
        assert hasattr(tag, "update")
        assert hasattr(tag, "delete")
        assert hasattr(tag, "bind")
        assert hasattr(tag, "unbind")
        assert hasattr(tag, "get_dataset_tags")

        # Test model resource methods (1 API)
        model = knowledge.v1.model
        assert hasattr(model, "embedding_models")

    def test_knowledge_service_async_methods(self) -> None:
        """Test all resources have async method variants through service."""
        config = Config()
        knowledge = Knowledge(config)

        # Test dataset async methods
        dataset = knowledge.v1.dataset
        assert hasattr(dataset, "acreate")
        assert hasattr(dataset, "alist")
        assert hasattr(dataset, "aget")
        assert hasattr(dataset, "aupdate")
        assert hasattr(dataset, "adelete")
        assert hasattr(dataset, "aretrieve")

        # Test document async methods
        document = knowledge.v1.document
        assert hasattr(document, "acreate_by_file")
        assert hasattr(document, "acreate_by_text")
        assert hasattr(document, "alist")
        assert hasattr(document, "aget")
        assert hasattr(document, "aupdate_by_file")
        assert hasattr(document, "aupdate_by_text")
        assert hasattr(document, "adelete")
        assert hasattr(document, "aupdate_status")
        assert hasattr(document, "aget_batch_status")
        assert hasattr(document, "afile_info")

        # Test segment async methods
        segment = knowledge.v1.segment
        assert hasattr(segment, "alist")
        assert hasattr(segment, "acreate")
        assert hasattr(segment, "aget")
        assert hasattr(segment, "aupdate")
        assert hasattr(segment, "adelete")

        # Test chunk async methods
        chunk = knowledge.v1.chunk
        assert hasattr(chunk, "alist")
        assert hasattr(chunk, "acreate")
        assert hasattr(chunk, "aupdate")
        assert hasattr(chunk, "adelete")

        # Test tag async methods
        tag = knowledge.v1.tag
        assert hasattr(tag, "alist")
        assert hasattr(tag, "acreate")
        assert hasattr(tag, "aupdate")
        assert hasattr(tag, "adelete")
        assert hasattr(tag, "abind")
        assert hasattr(tag, "aunbind")
        assert hasattr(tag, "aget_dataset_tags")

        # Test model async methods
        model = knowledge.v1.model
        assert hasattr(model, "aembedding_models")
