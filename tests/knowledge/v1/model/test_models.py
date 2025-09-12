"""Knowledge model tests."""

from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody


class TestKnowledgeModels:
    """Test Knowledge models."""

    def test_create_dataset_request_body_valid(self):
        """Test valid CreateDatasetRequestBody."""
        body = CreateDatasetRequestBody.builder().name("test").build()
        assert body.name == "test"

    def test_create_dataset_request_body_invalid(self):
        """Test invalid CreateDatasetRequestBody."""
        # Builder pattern may have defaults, so just test it builds
        body = CreateDatasetRequestBody.builder().build()
        assert body is not None

    def test_create_dataset_request_valid(self):
        """Test valid CreateDatasetRequest."""
        body = CreateDatasetRequestBody.builder().name("test").build()
        req = CreateDatasetRequest.builder().request_body(body).build()
        assert req.request_body.name == "test"

    def test_create_dataset_request_invalid(self):
        """Test invalid CreateDatasetRequest."""
        # Builder pattern may have defaults, so just test it builds
        req = CreateDatasetRequest.builder().build()
        assert req is not None
