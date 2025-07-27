from typing import Any
from unittest.mock import AsyncMock, Mock

import pytest

from dify_oapi.api.knowledge_base.v1.model.metadata.create_request import CreateRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.create_request_body import CreateRequestBody
from dify_oapi.api.knowledge_base.v1.model.metadata.create_response import CreateResponse
from dify_oapi.api.knowledge_base.v1.model.metadata.delete_request import DeleteRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.delete_response import DeleteResponse
from dify_oapi.api.knowledge_base.v1.model.metadata.list_request import ListRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.list_response import ListResponse
from dify_oapi.api.knowledge_base.v1.model.metadata.metadata_info import MetadataInfo
from dify_oapi.api.knowledge_base.v1.model.metadata.toggle_builtin_request import ToggleBuiltinRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.toggle_builtin_response import ToggleBuiltinResponse
from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_request import UpdateDocumentRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_request_body import (
    DocumentMetadata,
    OperationData,
    UpdateDocumentRequestBody,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_response import UpdateDocumentResponse
from dify_oapi.api.knowledge_base.v1.model.metadata.update_request import UpdateRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.update_request_body import UpdateRequestBody
from dify_oapi.api.knowledge_base.v1.model.metadata.update_response import UpdateResponse
from dify_oapi.api.knowledge_base.v1.resource.metadata import Metadata
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestMetadataAPIIntegration:
    @pytest.fixture
    def config(self) -> Config:
        return Config()

    @pytest.fixture
    def metadata_resource(self, config: Config) -> Metadata:
        return Metadata(config)

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    def test_metadata_management_workflow_sync(
        self,
        metadata_resource: Metadata,
        request_option: RequestOption,
        monkeypatch: Any,
    ) -> None:
        """Test complete metadata management workflow: create → list → update → delete"""
        dataset_id = "test-dataset-id"
        metadata_id = "test-metadata-id"

        # Mock create metadata
        create_response = CreateResponse(id=metadata_id, type="string", name="Test Metadata")

        # Mock list metadata
        metadata_list = [MetadataInfo(id=metadata_id, name="Test Metadata", type="string", use_count=0)]
        list_response = ListResponse(doc_metadata=metadata_list, built_in_field_enabled=True)

        # Mock update metadata
        update_response = UpdateResponse(id=metadata_id, type="string", name="Updated Metadata")

        # Mock delete metadata
        delete_response = DeleteResponse()

        # Set up mocks
        mock_execute = Mock()
        mock_execute.side_effect = [
            create_response,
            list_response,
            update_response,
            delete_response,
        ]
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # 1. Create metadata
        create_request_body = CreateRequestBody.builder().type("string").name("Test Metadata").build()
        create_request = CreateRequest.builder().dataset_id(dataset_id).request_body(create_request_body).build()
        created = metadata_resource.create(create_request, request_option)
        assert created.id == metadata_id
        assert created.name == "Test Metadata"
        assert created.type == "string"

        # 2. List metadata
        list_request = ListRequest.builder().dataset_id(dataset_id).build()
        metadata_list_result = metadata_resource.list(list_request, request_option)
        assert len(metadata_list_result.doc_metadata) == 1
        assert metadata_list_result.doc_metadata[0].id == metadata_id
        assert metadata_list_result.built_in_field_enabled is True

        # 3. Update metadata
        update_request_body = UpdateRequestBody.builder().name("Updated Metadata").build()
        update_request = (
            UpdateRequest.builder()
            .dataset_id(dataset_id)
            .metadata_id(metadata_id)
            .request_body(update_request_body)
            .build()
        )
        updated = metadata_resource.update(update_request, request_option)
        assert updated.id == metadata_id
        assert updated.name == "Updated Metadata"

        # 4. Delete metadata
        delete_request = DeleteRequest.builder().dataset_id(dataset_id).metadata_id(metadata_id).build()
        metadata_resource.delete(delete_request, request_option)

        # Verify all calls were made
        assert mock_execute.call_count == 4

    @pytest.mark.asyncio
    async def test_metadata_management_workflow_async(
        self,
        metadata_resource: Metadata,
        request_option: RequestOption,
        monkeypatch: Any,
    ) -> None:
        """Test metadata management workflow with async methods"""
        dataset_id = "async-dataset-id"
        metadata_id = "async-metadata-id"

        # Mock responses
        create_response = CreateResponse(id=metadata_id, type="number", name="Async Metadata")
        list_response = ListResponse(
            doc_metadata=[MetadataInfo(id=metadata_id, name="Async Metadata", type="number", use_count=0)],
            built_in_field_enabled=False,
        )
        update_response = UpdateResponse(id=metadata_id, type="number", name="Updated Async Metadata")
        delete_response = DeleteResponse()

        mock_aexecute = AsyncMock()
        mock_aexecute.side_effect = [
            create_response,
            list_response,
            update_response,
            delete_response,
        ]
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        # Execute async workflow
        create_request_body = CreateRequestBody.builder().type("number").name("Async Metadata").build()
        create_request = CreateRequest.builder().dataset_id(dataset_id).request_body(create_request_body).build()
        created = await metadata_resource.acreate(create_request, request_option)
        assert created.id == metadata_id

        list_request = ListRequest.builder().dataset_id(dataset_id).build()
        listed = await metadata_resource.alist(list_request, request_option)
        assert len(listed.doc_metadata) == 1

        update_request_body = UpdateRequestBody.builder().name("Updated Async Metadata").build()
        update_request = (
            UpdateRequest.builder()
            .dataset_id(dataset_id)
            .metadata_id(metadata_id)
            .request_body(update_request_body)
            .build()
        )
        updated = await metadata_resource.aupdate(update_request, request_option)
        assert updated.name == "Updated Async Metadata"

        delete_request = DeleteRequest.builder().dataset_id(dataset_id).metadata_id(metadata_id).build()
        await metadata_resource.adelete(delete_request, request_option)

        assert mock_aexecute.call_count == 4

    def test_builtin_metadata_operations(
        self,
        metadata_resource: Metadata,
        request_option: RequestOption,
        monkeypatch: Any,
    ) -> None:
        """Test built-in metadata enable/disable operations"""
        dataset_id = "builtin-test-dataset"

        # Mock enable built-in metadata
        enable_response = ToggleBuiltinResponse(result="success")
        mock_execute = Mock(return_value=enable_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Test enable built-in metadata
        enable_request = ToggleBuiltinRequest.builder().dataset_id(dataset_id).action("enable").build()
        enable_result = metadata_resource.toggle_builtin(enable_request, request_option)
        assert enable_result.result == "success"

        # Test disable built-in metadata
        disable_response = ToggleBuiltinResponse(result="success")
        mock_execute.return_value = disable_response

        disable_request = ToggleBuiltinRequest.builder().dataset_id(dataset_id).action("disable").build()
        disable_result = metadata_resource.toggle_builtin(disable_request, request_option)
        assert disable_result.result == "success"

        assert mock_execute.call_count == 2

    @pytest.mark.asyncio
    async def test_builtin_metadata_operations_async(
        self,
        metadata_resource: Metadata,
        request_option: RequestOption,
        monkeypatch: Any,
    ) -> None:
        """Test built-in metadata operations with async methods"""
        dataset_id = "async-builtin-dataset"

        enable_response = ToggleBuiltinResponse(result="success")
        mock_aexecute = AsyncMock(return_value=enable_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        enable_request = ToggleBuiltinRequest.builder().dataset_id(dataset_id).action("enable").build()
        result = await metadata_resource.atoggle_builtin(enable_request, request_option)
        assert result.result == "success"

    def test_document_metadata_update(
        self,
        metadata_resource: Metadata,
        request_option: RequestOption,
        monkeypatch: Any,
    ) -> None:
        """Test document metadata update operations"""
        dataset_id = "doc-metadata-dataset"

        # Mock document metadata update
        metadata_item = DocumentMetadata(id="meta1", value="test value", name="Test Field")
        operation_data = OperationData(document_id="doc1", metadata_list=[metadata_item])

        update_response = UpdateDocumentResponse(result="success")
        mock_execute = Mock(return_value=update_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        update_request_body = UpdateDocumentRequestBody.builder().operation_data([operation_data]).build()
        update_request = (
            UpdateDocumentRequest.builder().dataset_id(dataset_id).request_body(update_request_body).build()
        )
        result = metadata_resource.update_document(update_request, request_option)
        assert result.result == "success"

    @pytest.mark.asyncio
    async def test_document_metadata_update_async(
        self,
        metadata_resource: Metadata,
        request_option: RequestOption,
        monkeypatch: Any,
    ) -> None:
        """Test document metadata update with async methods"""
        dataset_id = "async-doc-metadata-dataset"

        metadata_item = DocumentMetadata(id="meta1", value="async value", name="Async Field")
        operation_data = OperationData(document_id="doc1", metadata_list=[metadata_item])

        update_response = UpdateDocumentResponse(result="success")
        mock_aexecute = AsyncMock(return_value=update_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        update_request_body = UpdateDocumentRequestBody.builder().operation_data([operation_data]).build()
        update_request = (
            UpdateDocumentRequest.builder().dataset_id(dataset_id).request_body(update_request_body).build()
        )
        result = await metadata_resource.aupdate_document(update_request, request_option)
        assert result.result == "success"

    def test_metadata_types_and_validation(
        self,
        metadata_resource: Metadata,
        request_option: RequestOption,
        monkeypatch: Any,
    ) -> None:
        """Test different metadata types and validation scenarios"""
        dataset_id = "validation-dataset"

        # Test different metadata types
        metadata_types = ["string", "number", "date", "boolean"]

        for metadata_type in metadata_types:
            create_response = CreateResponse(
                id=f"meta-{metadata_type}",
                type=metadata_type,
                name=f"Test {metadata_type.title()} Field",
            )
            mock_execute = Mock(return_value=create_response)
            monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

            create_request_body = (
                CreateRequestBody.builder().type(metadata_type).name(f"Test {metadata_type.title()} Field").build()
            )
            create_request = CreateRequest.builder().dataset_id(dataset_id).request_body(create_request_body).build()
            result = metadata_resource.create(create_request, request_option)

            assert result.type == metadata_type
            assert result.name == f"Test {metadata_type.title()} Field"

    def test_error_scenarios(
        self,
        metadata_resource: Metadata,
        request_option: RequestOption,
        monkeypatch: Any,
    ) -> None:
        """Test error handling scenarios"""
        # Mock error response
        mock_execute = Mock(side_effect=Exception("Metadata API Error"))
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        create_request_body = CreateRequestBody.builder().type("string").name("Error Field").build()
        create_request = CreateRequest.builder().dataset_id("error-dataset").request_body(create_request_body).build()

        with pytest.raises(Exception) as exc_info:
            metadata_resource.create(create_request, request_option)

        assert str(exc_info.value) == "Metadata API Error"

    def test_edge_cases(
        self,
        metadata_resource: Metadata,
        request_option: RequestOption,
        monkeypatch: Any,
    ) -> None:
        """Test edge cases and boundary conditions"""
        dataset_id = "edge-case-dataset"

        # Test empty metadata list
        empty_list_response = ListResponse(doc_metadata=[], built_in_field_enabled=False)
        mock_execute = Mock(return_value=empty_list_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        list_request = ListRequest.builder().dataset_id(dataset_id).build()
        result = metadata_resource.list(list_request, request_option)

        assert len(result.doc_metadata) == 0
        assert result.built_in_field_enabled is False

        # Test metadata with high use count
        high_use_metadata = MetadataInfo(id="high-use", name="Popular Field", type="string", use_count=1000)
        high_use_list_response = ListResponse(doc_metadata=[high_use_metadata], built_in_field_enabled=True)
        mock_execute.return_value = high_use_list_response

        result = metadata_resource.list(list_request, request_option)
        assert result.doc_metadata[0].use_count == 1000
