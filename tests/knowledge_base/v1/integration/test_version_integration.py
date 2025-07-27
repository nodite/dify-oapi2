"""Integration tests for knowledge_base V1 version class."""

from dify_oapi.api.knowledge_base.v1.resource.dataset import Dataset
from dify_oapi.api.knowledge_base.v1.resource.document import Document
from dify_oapi.api.knowledge_base.v1.resource.metadata import Metadata
from dify_oapi.api.knowledge_base.v1.resource.segment import Segment
from dify_oapi.api.knowledge_base.v1.resource.tag import Tag
from dify_oapi.api.knowledge_base.v1.version import V1
from dify_oapi.core.model.config import Config


class TestV1Integration:
    """Test V1 version integration."""

    def test_v1_initialization(self) -> None:
        """Test V1 class initialization with all resources."""
        config = Config()
        v1 = V1(config)

        # Test all resources are properly initialized
        assert isinstance(v1.dataset, Dataset)
        assert isinstance(v1.document, Document)
        assert isinstance(v1.metadata, Metadata)
        assert isinstance(v1.segment, Segment)
        assert isinstance(v1.tag, Tag)

    def test_v1_resources_have_config(self) -> None:
        """Test all resources have config properly configured."""
        config = Config()
        v1 = V1(config)

        # Test all resources have config
        assert hasattr(v1.dataset, "config")
        assert hasattr(v1.document, "config")
        assert hasattr(v1.metadata, "config")
        assert hasattr(v1.segment, "config")
        assert hasattr(v1.tag, "config")

    def test_v1_resource_methods_exist(self) -> None:
        """Test all resources have expected methods."""
        config = Config()
        v1 = V1(config)

        # Test dataset resource methods
        assert hasattr(v1.dataset, "create")
        assert hasattr(v1.dataset, "list")
        assert hasattr(v1.dataset, "get")
        assert hasattr(v1.dataset, "update")
        assert hasattr(v1.dataset, "delete")
        assert hasattr(v1.dataset, "retrieve")

        # Test metadata resource methods
        assert hasattr(v1.metadata, "create")
        assert hasattr(v1.metadata, "list")
        assert hasattr(v1.metadata, "update")
        assert hasattr(v1.metadata, "delete")
        assert hasattr(v1.metadata, "toggle_builtin")
        assert hasattr(v1.metadata, "update_document")

        # Test tag resource methods
        assert hasattr(v1.tag, "create")
        assert hasattr(v1.tag, "list")
        assert hasattr(v1.tag, "update")
        assert hasattr(v1.tag, "delete")
        assert hasattr(v1.tag, "bind_tags")
        assert hasattr(v1.tag, "unbind_tag")
        assert hasattr(v1.tag, "query_bound")

    def test_v1_async_methods_exist(self) -> None:
        """Test all resources have async method variants."""
        config = Config()
        v1 = V1(config)

        # Test dataset async methods
        assert hasattr(v1.dataset, "acreate")
        assert hasattr(v1.dataset, "alist")
        assert hasattr(v1.dataset, "aget")
        assert hasattr(v1.dataset, "aupdate")
        assert hasattr(v1.dataset, "adelete")
        assert hasattr(v1.dataset, "aretrieve")

        # Test metadata async methods
        assert hasattr(v1.metadata, "acreate")
        assert hasattr(v1.metadata, "alist")
        assert hasattr(v1.metadata, "aupdate")
        assert hasattr(v1.metadata, "adelete")
        assert hasattr(v1.metadata, "atoggle_builtin")
        assert hasattr(v1.metadata, "aupdate_document")

        # Test tag async methods
        assert hasattr(v1.tag, "acreate")
        assert hasattr(v1.tag, "alist")
        assert hasattr(v1.tag, "aupdate")
        assert hasattr(v1.tag, "adelete")
        assert hasattr(v1.tag, "abind_tags")
        assert hasattr(v1.tag, "aunbind_tag")
        assert hasattr(v1.tag, "aquery_bound")

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
        """Test config is properly propagated to all resources."""
        config = Config()
        v1 = V1(config)

        # All resources should have the same config reference
        # (This tests that config is properly passed during initialization)
        assert v1.dataset.config is config
        assert v1.document.config is config
        assert v1.metadata.config is config
        assert v1.segment.config is config
        assert v1.tag.config is config
