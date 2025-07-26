import pytest
from unittest.mock import Mock, AsyncMock
from typing import Any
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption
from dify_oapi.api.knowledge_base.v1.resource.metadata import Metadata

# Import metadata models
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
    DocumentMetadata,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_response import UpdateDocumentMetadataResponse


class TestMetadataResource:
    @pytest.fixture
    def config(self) -> Config:
        return Config()

    @pytest.fixture
    def metadata_resource(self, config: Config) -> Metadata:
        return Metadata(config)

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    def test_create_metadata(self, metadata_resource: Metadata, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        mock_response = CreateMetadataResponse(id="test_metadata_id", type="string", name="test_metadata")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = (
            CreateMetadataRequest.builder()
            .dataset_id("test_dataset_id")
            .type("string")
            .name("test_metadata")
            .build()
        )
        response = metadata_resource.create(request, request_option)

        assert response.id == "test_metadata_id"
        assert response.type == "string"
        assert response.name == "test_metadata"
        mock_execute.assert_called_once_with(
            metadata_resource.config, request, unmarshal_as=CreateMetadataResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_acreate_metadata(self, metadata_resource: Metadata, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = CreateMetadataResponse(id="test_metadata_id", type="string", name="test_metadata")
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = (
            CreateMetadataRequest.builder()
            .dataset_id("test_dataset_id")
            .type("string")
            .name("test_metadata")
            .build()
        )
        response = await metadata_resource.acreate(request, request_option)

        assert response.id == "test_metadata_id"
        assert response.type == "string"
        assert response.name == "test_metadata"
        mock_aexecute.assert_called_once_with(
            metadata_resource.config, request, unmarshal_as=CreateMetadataResponse, option=request_option
        )

    def test_list_metadata(self, metadata_resource: Metadata, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        mock_response = ListMetadataResponse.builder().doc_metadata([]).built_in_field_enabled(True).build()
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = ListMetadataRequest.builder().dataset_id("test_dataset_id").build()
        response = metadata_resource.list(request, request_option)

        assert response.doc_metadata == []
        assert response.built_in_field_enabled is True
        mock_execute.assert_called_once_with(
            metadata_resource.config, request, unmarshal_as=ListMetadataResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_alist_metadata(self, metadata_resource: Metadata, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = ListMetadataResponse.builder().doc_metadata([]).built_in_field_enabled(True).build()
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = ListMetadataRequest.builder().dataset_id("test_dataset_id").build()
        response = await metadata_resource.alist(request, request_option)

        assert response.doc_metadata == []
        assert response.built_in_field_enabled is True
        mock_aexecute.assert_called_once_with(
            metadata_resource.config, request, unmarshal_as=ListMetadataResponse, option=request_option
        )

    def test_update_metadata(self, metadata_resource: Metadata, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        mock_response = UpdateMetadataResponse(id="test_metadata_id", type="string", name="updated_metadata")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = (
            UpdateMetadataRequest.builder()
            .dataset_id("test_dataset_id")
            .metadata_id("test_metadata_id")
            .name("updated_metadata")
            .build()
        )
        response = metadata_resource.update(request, request_option)

        assert response.id == "test_metadata_id"
        assert response.type == "string"
        assert response.name == "updated_metadata"
        mock_execute.assert_called_once_with(
            metadata_resource.config, request, unmarshal_as=UpdateMetadataResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_aupdate_metadata(self, metadata_resource: Metadata, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = UpdateMetadataResponse(id="test_metadata_id", type="string", name="updated_metadata")
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = (
            UpdateMetadataRequest.builder()
            .dataset_id("test_dataset_id")
            .metadata_id("test_metadata_id")
            .name("updated_metadata")
            .build()
        )
        response = await metadata_resource.aupdate(request, request_option)

        assert response.id == "test_metadata_id"
        assert response.type == "string"
        assert response.name == "updated_metadata"
        mock_aexecute.assert_called_once_with(
            metadata_resource.config, request, unmarshal_as=UpdateMetadataResponse, option=request_option
        )

    def test_delete_metadata(self, metadata_resource: Metadata, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        mock_response = DeleteMetadataResponse()
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = (
            DeleteMetadataRequest.builder()
            .dataset_id("test_dataset_id")
            .metadata_id("test_metadata_id")
            .build()
        )
        response = metadata_resource.delete(request, request_option)

        assert isinstance(response, DeleteMetadataResponse)
        mock_execute.assert_called_once_with(
            metadata_resource.config, request, unmarshal_as=DeleteMetadataResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_adelete_metadata(self, metadata_resource: Metadata, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = DeleteMetadataResponse()
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = (
            DeleteMetadataRequest.builder()
            .dataset_id("test_dataset_id")
            .metadata_id("test_metadata_id")
            .build()
        )
        response = await metadata_resource.adelete(request, request_option)

        assert isinstance(response, DeleteMetadataResponse)
        mock_aexecute.assert_called_once_with(
            metadata_resource.config, request, unmarshal_as=DeleteMetadataResponse, option=request_option
        )

    def test_toggle_builtin_metadata(self, metadata_resource: Metadata, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        mock_response = ToggleBuiltinMetadataResponse(result="success")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = (
            ToggleBuiltinMetadataRequest.builder()
            .dataset_id("test_dataset_id")
            .action("enable")
            .build()
        )
        response = metadata_resource.toggle_builtin(request, request_option)

        assert response.result == "success"
        mock_execute.assert_called_once_with(
            metadata_resource.config, request, unmarshal_as=ToggleBuiltinMetadataResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_atoggle_builtin_metadata(self, metadata_resource: Metadata, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = ToggleBuiltinMetadataResponse(result="success")
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = (
            ToggleBuiltinMetadataRequest.builder()
            .dataset_id("test_dataset_id")
            .action("disable")
            .build()
        )
        response = await metadata_resource.atoggle_builtin(request, request_option)

        assert response.result == "success"
        mock_aexecute.assert_called_once_with(
            metadata_resource.config, request, unmarshal_as=ToggleBuiltinMetadataResponse, option=request_option
        )

    def test_update_document_metadata(self, metadata_resource: Metadata, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        mock_response = UpdateDocumentMetadataResponse(result="success")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Create test operation data
        metadata = DocumentMetadata.builder().id("meta_id").value("meta_value").name("meta_name").build()
        operation_data = OperationData.builder().document_id("doc_id").metadata_list([metadata]).build()

        request = (
            UpdateDocumentMetadataRequest.builder()
            .dataset_id("test_dataset_id")
            .operation_data([operation_data])
            .build()
        )
        response = metadata_resource.update_document(request, request_option)

        assert response.result == "success"
        mock_execute.assert_called_once_with(
            metadata_resource.config, request, unmarshal_as=UpdateDocumentMetadataResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_aupdate_document_metadata(self, metadata_resource: Metadata, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = UpdateDocumentMetadataResponse(result="success")
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        # Create test operation data
        metadata = DocumentMetadata.builder().id("meta_id").value("meta_value").name("meta_name").build()
        operation_data = OperationData.builder().document_id("doc_id").metadata_list([metadata]).build()

        request = (
            UpdateDocumentMetadataRequest.builder()
            .dataset_id("test_dataset_id")
            .operation_data([operation_data])
            .build()
        )
        response = await metadata_resource.aupdate_document(request, request_option)

        assert response.result == "success"
        mock_aexecute.assert_called_once_with(
            metadata_resource.config, request, unmarshal_as=UpdateDocumentMetadataResponse, option=request_option
        )

    def test_config_initialization(self, config: Config) -> None:
        metadata = Metadata(config)
        assert metadata.config is config

    def test_optional_request_option(self, metadata_resource: Metadata, monkeypatch: Any) -> None:
        # Test that methods work without request_option parameter
        mock_response = CreateMetadataResponse(id="test_metadata_id", type="string", name="test_metadata")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = (
            CreateMetadataRequest.builder()
            .dataset_id("test_dataset_id")
            .type("string")
            .name("test_metadata")
            .build()
        )
        response = metadata_resource.create(request)

        assert response.id == "test_metadata_id"
        mock_execute.assert_called_once_with(
            metadata_resource.config, request, unmarshal_as=CreateMetadataResponse, option=None
        )

    def test_request_url_patterns(self) -> None:
        # Test URL patterns for different endpoints
        create_request = CreateMetadataRequest.builder().dataset_id("dataset123").build()
        assert create_request.uri == "/v1/datasets/:dataset_id/metadata"
        assert create_request.paths["dataset_id"] == "dataset123"

        list_request = ListMetadataRequest.builder().dataset_id("dataset123").build()
        assert list_request.uri == "/v1/datasets/:dataset_id/metadata"
        assert list_request.paths["dataset_id"] == "dataset123"

        update_request = (
            UpdateMetadataRequest.builder()
            .dataset_id("dataset123")
            .metadata_id("meta456")
            .build()
        )
        assert update_request.uri == "/v1/datasets/:dataset_id/metadata/:metadata_id"
        assert update_request.paths["dataset_id"] == "dataset123"
        assert update_request.paths["metadata_id"] == "meta456"

        delete_request = (
            DeleteMetadataRequest.builder()
            .dataset_id("dataset123")
            .metadata_id("meta456")
            .build()
        )
        assert delete_request.uri == "/v1/datasets/:dataset_id/metadata/:metadata_id"
        assert delete_request.paths["dataset_id"] == "dataset123"
        assert delete_request.paths["metadata_id"] == "meta456"

        toggle_request = (
            ToggleBuiltinMetadataRequest.builder()
            .dataset_id("dataset123")
            .action("enable")
            .build()
        )
        assert toggle_request.uri == "/v1/datasets/:dataset_id/metadata/built-in/:action"
        assert toggle_request.paths["dataset_id"] == "dataset123"
        assert toggle_request.paths["action"] == "enable"

        update_doc_request = (
            UpdateDocumentMetadataRequest.builder()
            .dataset_id("dataset123")
            .build()
        )
        assert update_doc_request.uri == "/v1/datasets/:dataset_id/documents/metadata"
        assert update_doc_request.paths["dataset_id"] == "dataset123"

    def test_http_methods(self) -> None:
        # Test HTTP methods for different requests
        from dify_oapi.core.enum import HttpMethod

        create_request = CreateMetadataRequest.builder().build()
        assert create_request.http_method == HttpMethod.POST

        list_request = ListMetadataRequest.builder().build()
        assert list_request.http_method == HttpMethod.GET

        update_request = UpdateMetadataRequest.builder().build()
        assert update_request.http_method == HttpMethod.PATCH

        delete_request = DeleteMetadataRequest.builder().build()
        assert delete_request.http_method == HttpMethod.DELETE

        toggle_request = ToggleBuiltinMetadataRequest.builder().build()
        assert toggle_request.http_method == HttpMethod.POST

        update_doc_request = UpdateDocumentMetadataRequest.builder().build()
        assert update_doc_request.http_method == HttpMethod.POST