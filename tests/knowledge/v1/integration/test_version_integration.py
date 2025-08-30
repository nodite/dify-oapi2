"""Integration tests for knowledge V1 version class."""

from dify_oapi.api.knowledge.v1.resource.chunk import Chunk
from dify_oapi.api.knowledge.v1.resource.dataset import Dataset
from dify_oapi.api.knowledge.v1.resource.document import Document
from dify_oapi.api.knowledge.v1.resource.model import Model
from dify_oapi.api.knowledge.v1.resource.segment import Segment
from dify_oapi.api.knowledge.v1.resource.tag import Tag
from dify_oapi.api.knowledge.v1.version import V1
from dify_oapi.core.model.config import Config


class TestV1Integration:
    """Test V1 version integration."""

    def test_v1_initialization(self) -> None:
        """Test V1 class initialization with all 6 resources."""
        config = Config()
        v1 = V1(config)

        # Test all 6 resources are properly initialized
        assert isinstance(v1.dataset, Dataset)
        assert isinstance(v1.document, Document)
        assert isinstance(v1.segment, Segment)
        assert isinstance(v1.chunk, Chunk)
        assert isinstance(v1.tag, Tag)
        assert isinstance(v1.model, Model)

    def test_v1_resources_have_config(self) -> None:
        """Test all 6 resources have config properly configured."""
        config = Config()
        v1 = V1(config)

        # Test all 6 resources have config
        assert hasattr(v1.dataset, "config")
        assert hasattr(v1.document, "config")
        assert hasattr(v1.segment, "config")
        assert hasattr(v1.chunk, "config")
        assert hasattr(v1.tag, "config")
        assert hasattr(v1.model, "config")

    def test_v1_resource_methods_exist(self) -> None:
        """Test all resources have expected methods for 33 APIs."""
        config = Config()
        v1 = V1(config)

        # Test dataset resource methods (6 APIs)
        assert hasattr(v1.dataset, "create")
        assert hasattr(v1.dataset, "list")
        assert hasattr(v1.dataset, "get")
        assert hasattr(v1.dataset, "update")
        assert hasattr(v1.dataset, "delete")
        assert hasattr(v1.dataset, "retrieve")

        # Test document resource methods (10 APIs)
        assert hasattr(v1.document, "create_by_file")
        assert hasattr(v1.document, "create_by_text")
        assert hasattr(v1.document, "list")
        assert hasattr(v1.document, "get")
        assert hasattr(v1.document, "update_by_file")
        assert hasattr(v1.document, "update_by_text")
        assert hasattr(v1.document, "delete")
        assert hasattr(v1.document, "update_status")
        assert hasattr(v1.document, "get_batch_status")
        assert hasattr(v1.document, "file_info")

        # Test segment resource methods (5 APIs)
        assert hasattr(v1.segment, "list")
        assert hasattr(v1.segment, "create")
        assert hasattr(v1.segment, "get")
        assert hasattr(v1.segment, "update")
        assert hasattr(v1.segment, "delete")

        # Test chunk resource methods (4 APIs)
        assert hasattr(v1.chunk, "list")
        assert hasattr(v1.chunk, "create")
        assert hasattr(v1.chunk, "update")
        assert hasattr(v1.chunk, "delete")

        # Test tag resource methods (7 APIs)
        assert hasattr(v1.tag, "list")
        assert hasattr(v1.tag, "create")
        assert hasattr(v1.tag, "update")
        assert hasattr(v1.tag, "delete")
        assert hasattr(v1.tag, "bind")
        assert hasattr(v1.tag, "unbind")
        assert hasattr(v1.tag, "get_dataset_tags")

        # Test model resource methods (1 API)
        assert hasattr(v1.model, "embedding_models")

    def test_v1_async_methods_exist(self) -> None:
        """Test all resources have async method variants for 33 APIs."""
        config = Config()
        v1 = V1(config)

        # Test dataset async methods (6 APIs)
        assert hasattr(v1.dataset, "acreate")
        assert hasattr(v1.dataset, "alist")
        assert hasattr(v1.dataset, "aget")
        assert hasattr(v1.dataset, "aupdate")
        assert hasattr(v1.dataset, "adelete")
        assert hasattr(v1.dataset, "aretrieve")

        # Test document async methods (10 APIs)
        assert hasattr(v1.document, "acreate_by_file")
        assert hasattr(v1.document, "acreate_by_text")
        assert hasattr(v1.document, "alist")
        assert hasattr(v1.document, "aget")
        assert hasattr(v1.document, "aupdate_by_file")
        assert hasattr(v1.document, "aupdate_by_text")
        assert hasattr(v1.document, "adelete")
        assert hasattr(v1.document, "aupdate_status")
        assert hasattr(v1.document, "aget_batch_status")
        assert hasattr(v1.document, "afile_info")

        # Test segment async methods (5 APIs)
        assert hasattr(v1.segment, "alist")
        assert hasattr(v1.segment, "acreate")
        assert hasattr(v1.segment, "aget")
        assert hasattr(v1.segment, "aupdate")
        assert hasattr(v1.segment, "adelete")

        # Test chunk async methods (4 APIs)
        assert hasattr(v1.chunk, "alist")
        assert hasattr(v1.chunk, "acreate")
        assert hasattr(v1.chunk, "aupdate")
        assert hasattr(v1.chunk, "adelete")

        # Test tag async methods (7 APIs)
        assert hasattr(v1.tag, "alist")
        assert hasattr(v1.tag, "acreate")
        assert hasattr(v1.tag, "aupdate")
        assert hasattr(v1.tag, "adelete")
        assert hasattr(v1.tag, "abind")
        assert hasattr(v1.tag, "aunbind")
        assert hasattr(v1.tag, "aget_dataset_tags")

        # Test model async methods (1 API)
        assert hasattr(v1.model, "aembedding_models")

    def test_v1_backward_compatibility(self) -> None:
        """Test backward compatibility with existing resources."""
        config = Config()
        v1 = V1(config)

        # Test existing resources still work
        assert hasattr(v1.document, "create_by_text")
        assert hasattr(v1.segment, "create")

        # Test existing async methods still work
        assert hasattr(v1.document, "acreate_by_text")
        assert hasattr(v1.segment, "acreate")

    def test_v1_config_propagation(self) -> None:
        """Test config is properly propagated to all 6 resources."""
        config = Config()
        v1 = V1(config)

        # All 6 resources should have the same config reference
        # (This tests that config is properly passed during initialization)
        assert v1.dataset.config is config
        assert v1.document.config is config
        assert v1.segment.config is config
        assert v1.chunk.config is config
        assert v1.tag.config is config
        assert v1.model.config is config

    def test_v1_api_count_verification(self) -> None:
        """Test that all 33 APIs are accessible through V1."""
        config = Config()
        v1 = V1(config)

        # Count sync methods across all resources
        dataset_methods = ["create", "list", "get", "update", "delete", "retrieve"]  # 6 APIs
        document_methods = [
            "create_by_file",
            "create_by_text",
            "list",
            "get",
            "update_by_file",
            "update_by_text",
            "delete",
            "update_status",
            "get_batch_status",
            "file_info",
        ]  # 10 APIs
        segment_methods = ["list", "create", "get", "update", "delete"]  # 5 APIs
        chunk_methods = ["list", "create", "update", "delete"]  # 4 APIs
        tag_methods = ["list", "create", "update", "delete", "bind", "unbind", "get_dataset_tags"]  # 7 APIs
        model_methods = ["embedding_models"]  # 1 API

        # Verify all methods exist
        for method in dataset_methods:
            assert hasattr(v1.dataset, method), f"Dataset missing method: {method}"
        for method in document_methods:
            assert hasattr(v1.document, method), f"Document missing method: {method}"
        for method in segment_methods:
            assert hasattr(v1.segment, method), f"Segment missing method: {method}"
        for method in chunk_methods:
            assert hasattr(v1.chunk, method), f"Chunk missing method: {method}"
        for method in tag_methods:
            assert hasattr(v1.tag, method), f"Tag missing method: {method}"
        for method in model_methods:
            assert hasattr(v1.model, method), f"Model missing method: {method}"

        # Total: 6 + 10 + 5 + 4 + 7 + 1 = 33 APIs
        total_apis = (
            len(dataset_methods)
            + len(document_methods)
            + len(segment_methods)
            + len(chunk_methods)
            + len(tag_methods)
            + len(model_methods)
        )
        assert total_apis == 33, f"Expected 33 APIs, found {total_apis}"

    def test_v1_6_resource_architecture(self) -> None:
        """Test that V1 implements the complete 6-resource architecture."""
        config = Config()
        v1 = V1(config)

        # Test all 6 resources are present
        resources = ["dataset", "document", "segment", "chunk", "tag", "model"]
        for resource in resources:
            assert hasattr(v1, resource), f"V1 missing resource: {resource}"
            assert getattr(v1, resource) is not None, f"V1 resource {resource} is None"

        # Test resource types
        assert isinstance(v1.dataset, Dataset)
        assert isinstance(v1.document, Document)
        assert isinstance(v1.segment, Segment)
        assert isinstance(v1.chunk, Chunk)
        assert isinstance(v1.tag, Tag)
        assert isinstance(v1.model, Model)
