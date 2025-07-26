import pytest
from typing import List

from dify_oapi.api.knowledge_base.v1.model.metadata.create_request import CreateMetadataRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.create_response import CreateMetadataResponse
from dify_oapi.api.knowledge_base.v1.model.metadata.list_request import ListMetadataRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.list_response import ListMetadataResponse
from dify_oapi.api.knowledge_base.v1.model.metadata.update_request import UpdateMetadataRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.update_response import UpdateMetadataResponse
from dify_oapi.api.knowledge_base.v1.model.metadata.delete_request import DeleteMetadataRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.delete_response import DeleteMetadataResponse
from dify_oapi.api.knowledge_base.v1.model.metadata.toggle_builtin_request import ToggleBuiltinMetadataRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.toggle_builtin_response import ToggleBuiltinMetadataResponse
from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_request import (
    UpdateDocumentMetadataRequest,
    OperationData,
    DocumentMetadata
)
from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_response import UpdateDocumentMetadataResponse
from dify_oapi.api.knowledge_base.v1.model.dataset.metadata_info import MetadataInfo


class TestCreateMetadataRequest:
    def test_builder_pattern(self):
        request = (
            CreateMetadataRequest.builder()
            .dataset_id("dataset-123")
            .type("string")
            .name("test-metadata")
            .build()
        )
        
        assert request.dataset_id == "dataset-123"
        assert request.type == "string"
        assert request.name == "test-metadata"

    def test_required_fields(self):
        request = CreateMetadataRequest(dataset_id="dataset-123", type="string", name="test-metadata")
        assert request.dataset_id == "dataset-123"
        assert request.type == "string"
        assert request.name == "test-metadata"


class TestCreateMetadataResponse:
    def test_builder_pattern(self):
        response = (
            CreateMetadataResponse.builder()
            .id("meta-123")
            .type("string")
            .name("test-metadata")
            .build()
        )
        
        assert response.id == "meta-123"
        assert response.type == "string"
        assert response.name == "test-metadata"

    def test_to_metadata_info(self):
        response = CreateMetadataResponse(id="meta-123", type="string", name="test-metadata")
        metadata_info = response.to_metadata_info()
        
        assert isinstance(metadata_info, MetadataInfo)
        assert metadata_info.id == "meta-123"
        assert metadata_info.type == "string"
        assert metadata_info.name == "test-metadata"


class TestListMetadataRequest:
    def test_builder_pattern(self):
        request = (
            ListMetadataRequest.builder()
            .dataset_id("dataset-123")
            .build()
        )
        
        assert request.dataset_id == "dataset-123"

    def test_required_field(self):
        request = ListMetadataRequest(dataset_id="dataset-123")
        assert request.dataset_id == "dataset-123"


class TestListMetadataResponse:
    def test_builder_pattern(self):
        metadata_info = MetadataInfo(id="meta-123", type="string", name="test-metadata")
        response = (
            ListMetadataResponse.builder()
            .doc_metadata([metadata_info])
            .built_in_field_enabled(True)
            .build()
        )
        
        assert len(response.doc_metadata) == 1
        assert response.doc_metadata[0].id == "meta-123"
        assert response.built_in_field_enabled is True

    def test_empty_metadata_list(self):
        response = ListMetadataResponse(doc_metadata=[], built_in_field_enabled=False)
        assert response.doc_metadata == []
        assert response.built_in_field_enabled is False


class TestUpdateMetadataRequest:
    def test_builder_pattern(self):
        request = (
            UpdateMetadataRequest.builder()
            .dataset_id("dataset-123")
            .metadata_id("meta-123")
            .name("updated-name")
            .build()
        )
        
        assert request.dataset_id == "dataset-123"
        assert request.metadata_id == "meta-123"
        assert request.name == "updated-name"

    def test_required_fields(self):
        request = UpdateMetadataRequest(
            dataset_id="dataset-123",
            metadata_id="meta-123",
            name="updated-name"
        )
        assert request.dataset_id == "dataset-123"
        assert request.metadata_id == "meta-123"
        assert request.name == "updated-name"


class TestUpdateMetadataResponse:
    def test_builder_pattern(self):
        response = (
            UpdateMetadataResponse.builder()
            .id("meta-123")
            .type("string")
            .name("updated-name")
            .build()
        )
        
        assert response.id == "meta-123"
        assert response.type == "string"
        assert response.name == "updated-name"

    def test_to_metadata_info(self):
        response = UpdateMetadataResponse(id="meta-123", type="string", name="updated-name")
        metadata_info = response.to_metadata_info()
        
        assert isinstance(metadata_info, MetadataInfo)
        assert metadata_info.id == "meta-123"
        assert metadata_info.type == "string"
        assert metadata_info.name == "updated-name"


class TestDeleteMetadataRequest:
    def test_builder_pattern(self):
        request = (
            DeleteMetadataRequest.builder()
            .dataset_id("dataset-123")
            .metadata_id("meta-123")
            .build()
        )
        
        assert request.dataset_id == "dataset-123"
        assert request.metadata_id == "meta-123"

    def test_required_fields(self):
        request = DeleteMetadataRequest(dataset_id="dataset-123", metadata_id="meta-123")
        assert request.dataset_id == "dataset-123"
        assert request.metadata_id == "meta-123"


class TestDeleteMetadataResponse:
    def test_empty_response(self):
        response = DeleteMetadataResponse.builder().build()
        assert isinstance(response, DeleteMetadataResponse)

    def test_builder_pattern(self):
        response = DeleteMetadataResponse.builder().build()
        assert isinstance(response, DeleteMetadataResponse)


class TestToggleBuiltinMetadataRequest:
    def test_builder_pattern(self):
        request = (
            ToggleBuiltinMetadataRequest.builder()
            .dataset_id("dataset-123")
            .action("enable")
            .build()
        )
        
        assert request.dataset_id == "dataset-123"
        assert request.action == "enable"

    def test_disable_action(self):
        request = (
            ToggleBuiltinMetadataRequest.builder()
            .dataset_id("dataset-123")
            .action("disable")
            .build()
        )
        
        assert request.dataset_id == "dataset-123"
        assert request.action == "disable"


class TestToggleBuiltinMetadataResponse:
    def test_builder_pattern(self):
        response = (
            ToggleBuiltinMetadataResponse.builder()
            .result("success")
            .build()
        )
        
        assert response.result == "success"

    def test_result_field(self):
        response = ToggleBuiltinMetadataResponse(result="success")
        assert response.result == "success"


class TestDocumentMetadata:
    def test_builder_pattern(self):
        metadata = (
            DocumentMetadata.builder()
            .id("meta-123")
            .value("test-value")
            .name("test-name")
            .build()
        )
        
        assert metadata.id == "meta-123"
        assert metadata.value == "test-value"
        assert metadata.name == "test-name"

    def test_required_fields(self):
        metadata = DocumentMetadata(id="meta-123", value="test-value", name="test-name")
        assert metadata.id == "meta-123"
        assert metadata.value == "test-value"
        assert metadata.name == "test-name"


class TestOperationData:
    def test_builder_pattern(self):
        metadata = DocumentMetadata(id="meta-123", value="test-value", name="test-name")
        operation_data = (
            OperationData.builder()
            .document_id("doc-123")
            .metadata_list([metadata])
            .build()
        )
        
        assert operation_data.document_id == "doc-123"
        assert len(operation_data.metadata_list) == 1
        assert operation_data.metadata_list[0].id == "meta-123"

    def test_empty_metadata_list(self):
        operation_data = OperationData(document_id="doc-123", metadata_list=[])
        assert operation_data.document_id == "doc-123"
        assert operation_data.metadata_list == []


class TestUpdateDocumentMetadataRequest:
    def test_builder_pattern(self):
        metadata = DocumentMetadata(id="meta-123", value="test-value", name="test-name")
        operation_data = OperationData(document_id="doc-123", metadata_list=[metadata])
        
        request = (
            UpdateDocumentMetadataRequest.builder()
            .dataset_id("dataset-123")
            .operation_data([operation_data])
            .build()
        )
        
        assert request.dataset_id == "dataset-123"
        assert len(request.operation_data) == 1
        assert request.operation_data[0].document_id == "doc-123"

    def test_complex_nested_structure(self):
        metadata1 = DocumentMetadata(id="meta-1", value="value-1", name="name-1")
        metadata2 = DocumentMetadata(id="meta-2", value="value-2", name="name-2")
        
        operation_data1 = OperationData(document_id="doc-1", metadata_list=[metadata1])
        operation_data2 = OperationData(document_id="doc-2", metadata_list=[metadata2])
        
        request = UpdateDocumentMetadataRequest(
            dataset_id="dataset-123",
            operation_data=[operation_data1, operation_data2]
        )
        
        assert request.dataset_id == "dataset-123"
        assert len(request.operation_data) == 2
        assert request.operation_data[0].document_id == "doc-1"
        assert request.operation_data[1].document_id == "doc-2"

    def test_empty_operation_data(self):
        request = UpdateDocumentMetadataRequest(dataset_id="dataset-123", operation_data=[])
        assert request.dataset_id == "dataset-123"
        assert request.operation_data == []


class TestUpdateDocumentMetadataResponse:
    def test_builder_pattern(self):
        response = (
            UpdateDocumentMetadataResponse.builder()
            .result("success")
            .build()
        )
        
        assert response.result == "success"

    def test_result_field(self):
        response = UpdateDocumentMetadataResponse(result="success")
        assert response.result == "success"


class TestMetadataModelsIntegration:
    def test_create_to_list_integration(self):
        # Test that create response can be used in list response
        create_response = CreateMetadataResponse(id="meta-123", type="string", name="test-metadata")
        metadata_info = create_response.to_metadata_info()
        
        list_response = ListMetadataResponse(doc_metadata=[metadata_info], built_in_field_enabled=True)
        
        assert len(list_response.doc_metadata) == 1
        assert list_response.doc_metadata[0].id == "meta-123"
        assert list_response.doc_metadata[0].name == "test-metadata"

    def test_update_to_metadata_info_integration(self):
        # Test that update response can be converted to metadata info
        update_response = UpdateMetadataResponse(id="meta-123", type="string", name="updated-name")
        metadata_info = update_response.to_metadata_info()
        
        assert isinstance(metadata_info, MetadataInfo)
        assert metadata_info.id == "meta-123"
        assert metadata_info.name == "updated-name"

    def test_document_metadata_nested_builders(self):
        # Test complex nested builder pattern usage
        metadata = (
            DocumentMetadata.builder()
            .id("meta-123")
            .value("test-value")
            .name("test-name")
            .build()
        )
        
        operation_data = (
            OperationData.builder()
            .document_id("doc-123")
            .metadata_list([metadata])
            .build()
        )
        
        request = (
            UpdateDocumentMetadataRequest.builder()
            .dataset_id("dataset-123")
            .operation_data([operation_data])
            .build()
        )
        
        assert request.dataset_id == "dataset-123"
        assert len(request.operation_data) == 1
        assert request.operation_data[0].document_id == "doc-123"
        assert len(request.operation_data[0].metadata_list) == 1
        assert request.operation_data[0].metadata_list[0].id == "meta-123"