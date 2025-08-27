"""Unit tests for metadata API models."""

from __future__ import annotations

from dify_oapi.api.knowledge_base.v1.model.metadata.create_request import CreateRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.create_request_body import CreateRequestBody
from dify_oapi.api.knowledge_base.v1.model.metadata.create_response import CreateResponse
from dify_oapi.api.knowledge_base.v1.model.metadata.delete_request import DeleteRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.delete_response import DeleteResponse
from dify_oapi.api.knowledge_base.v1.model.metadata.list_request import ListRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.list_response import ListResponse
from dify_oapi.api.knowledge_base.v1.model.metadata.toggle_builtin_request import ToggleBuiltinRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.toggle_builtin_response import ToggleBuiltinResponse
from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_request import UpdateDocumentRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_request_body import UpdateDocumentRequestBody
from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_response import UpdateDocumentResponse
from dify_oapi.api.knowledge_base.v1.model.metadata.update_request import UpdateRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.update_request_body import UpdateRequestBody
from dify_oapi.api.knowledge_base.v1.model.metadata.update_response import UpdateResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestCreateModels:
    """Test Create API models."""

    def test_request_builder(self) -> None:
        """Test CreateRequest builder pattern."""
        request_body = CreateRequestBody.builder().type("string").name("test-metadata").build()
        request = CreateRequest.builder().dataset_id("dataset-123").request_body(request_body).build()
        assert request.dataset_id == "dataset-123"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.request_body is not None
        assert request.request_body.type == "string"
        assert request.request_body.name == "test-metadata"

    def test_request_validation(self) -> None:
        """Test CreateRequest validation."""
        request = CreateRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/:dataset_id/metadata"

    def test_request_body_builder(self) -> None:
        """Test CreateRequestBody builder pattern."""
        request_body = CreateRequestBody.builder().type("string").name("test-metadata").build()
        assert request_body.type == "string"
        assert request_body.name == "test-metadata"

    def test_request_body_validation(self) -> None:
        """Test CreateRequestBody validation."""
        request_body = CreateRequestBody(type="string", name="test-metadata")
        assert request_body.type == "string"
        assert request_body.name == "test-metadata"

    def test_response_inheritance(self) -> None:
        """Test CreateResponse inherits from BaseResponse."""
        response = CreateResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test CreateResponse data access."""
        response = CreateResponse(id="meta-123", type="string", name="test-metadata")
        assert response.id == "meta-123"
        assert response.type == "string"
        assert response.name == "test-metadata"


class TestListModels:
    """Test List API models."""

    def test_request_builder(self) -> None:
        """Test ListRequest builder pattern."""
        request = ListRequest.builder().dataset_id("dataset-123").build()
        assert request.dataset_id == "dataset-123"
        assert request.paths["dataset_id"] == "dataset-123"

    def test_request_validation(self) -> None:
        """Test ListRequest validation."""
        request = ListRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/:dataset_id/metadata"

    def test_response_inheritance(self) -> None:
        """Test ListResponse inherits from BaseResponse."""
        response = ListResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test ListResponse data access."""
        response = ListResponse(doc_metadata=[], built_in_field_enabled=False)
        assert response.doc_metadata == []
        assert response.built_in_field_enabled is False


class TestUpdateModels:
    """Test Update API models."""

    def test_request_builder(self) -> None:
        """Test UpdateRequest builder pattern."""
        request_body = UpdateRequestBody.builder().name("updated-name").build()
        request = (
            UpdateRequest.builder().dataset_id("dataset-123").metadata_id("meta-123").request_body(request_body).build()
        )
        assert request.dataset_id == "dataset-123"
        assert request.metadata_id == "meta-123"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["metadata_id"] == "meta-123"
        assert request.request_body is not None

    def test_request_validation(self) -> None:
        """Test UpdateRequest validation."""
        request = UpdateRequest.builder().build()
        assert request.http_method == HttpMethod.PATCH
        assert request.uri == "/v1/datasets/:dataset_id/metadata/:metadata_id"

    def test_request_body_builder(self) -> None:
        """Test UpdateRequestBody builder pattern."""
        request_body = UpdateRequestBody.builder().name("updated-name").build()
        assert request_body.name == "updated-name"

    def test_request_body_validation(self) -> None:
        """Test UpdateRequestBody validation."""
        request_body = UpdateRequestBody(name="updated-name")
        assert request_body.name == "updated-name"

    def test_response_inheritance(self) -> None:
        """Test UpdateResponse inherits from BaseResponse."""
        response = UpdateResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test UpdateResponse data access."""
        response = UpdateResponse(id="meta-123", type="string", name="updated-name")
        assert response.id == "meta-123"
        assert response.type == "string"
        assert response.name == "updated-name"


class TestDeleteModels:
    """Test Delete API models."""

    def test_request_builder(self) -> None:
        """Test DeleteRequest builder pattern."""
        request = DeleteRequest.builder().dataset_id("dataset-123").metadata_id("meta-123").build()
        assert request.dataset_id == "dataset-123"
        assert request.metadata_id == "meta-123"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["metadata_id"] == "meta-123"

    def test_request_validation(self) -> None:
        """Test DeleteRequest validation."""
        request = DeleteRequest.builder().build()
        assert request.http_method == HttpMethod.DELETE
        assert request.uri == "/v1/datasets/:dataset_id/metadata/:metadata_id"

    def test_response_inheritance(self) -> None:
        """Test DeleteResponse inherits from BaseResponse."""
        response = DeleteResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test DeleteResponse data access."""
        response = DeleteResponse()
        assert isinstance(response, DeleteResponse)


class TestToggleBuiltinModels:
    """Test ToggleBuiltin API models."""

    def test_request_builder(self) -> None:
        """Test ToggleBuiltinRequest builder pattern."""
        request = ToggleBuiltinRequest.builder().dataset_id("dataset-123").action("enable").build()
        assert request.dataset_id == "dataset-123"
        assert request.action == "enable"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["action"] == "enable"

    def test_request_validation(self) -> None:
        """Test ToggleBuiltinRequest validation."""
        request = ToggleBuiltinRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/:dataset_id/metadata/built-in/:action"

    def test_response_inheritance(self) -> None:
        """Test ToggleBuiltinResponse inherits from BaseResponse."""
        response = ToggleBuiltinResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test ToggleBuiltinResponse data access."""
        response = ToggleBuiltinResponse(result="success")
        assert response.result == "success"


class TestUpdateDocumentModels:
    """Test UpdateDocument API models."""

    def test_request_builder(self) -> None:
        """Test UpdateDocumentRequest builder pattern."""
        from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_request_body import (
            DocumentMetadata,
            OperationData,
        )

        metadata = DocumentMetadata(id="meta-123", value="test-value", name="test-name")
        operation_data = OperationData(document_id="doc-123", metadata_list=[metadata])
        request_body = UpdateDocumentRequestBody.builder().operation_data([operation_data]).build()
        request = UpdateDocumentRequest.builder().dataset_id("dataset-123").request_body(request_body).build()
        assert request.dataset_id == "dataset-123"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.request_body is not None

    def test_request_validation(self) -> None:
        """Test UpdateDocumentRequest validation."""
        request = UpdateDocumentRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/:dataset_id/documents/metadata"

    def test_request_body_builder(self) -> None:
        """Test UpdateDocumentRequestBody builder pattern."""
        from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_request_body import (
            DocumentMetadata,
            OperationData,
        )

        metadata = DocumentMetadata(id="meta-123", value="test-value", name="test-name")
        operation_data = OperationData(document_id="doc-123", metadata_list=[metadata])
        request_body = UpdateDocumentRequestBody.builder().operation_data([operation_data]).build()
        assert request_body.operation_data is not None
        assert len(request_body.operation_data) == 1

    def test_request_body_validation(self) -> None:
        """Test UpdateDocumentRequestBody validation."""
        from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_request_body import (
            DocumentMetadata,
            OperationData,
        )

        metadata = DocumentMetadata(id="meta-123", value="test-value", name="test-name")
        operation_data = OperationData(document_id="doc-123", metadata_list=[metadata])
        request_body = UpdateDocumentRequestBody(operation_data=[operation_data])
        assert request_body.operation_data is not None

    def test_response_inheritance(self) -> None:
        """Test UpdateDocumentResponse inherits from BaseResponse."""
        response = UpdateDocumentResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test UpdateDocumentResponse data access."""
        response = UpdateDocumentResponse(result="success")
        assert response.result == "success"
