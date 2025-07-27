from dify_oapi.api.knowledge_base.v1.model.metadata.create_request import (
    CreateRequest,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.create_response import (
    CreateResponse,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.delete_request import (
    DeleteRequest,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.delete_response import (
    DeleteResponse,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.list_request import (
    ListRequest,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.list_response import (
    ListResponse,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.metadata_info import MetadataInfo
from dify_oapi.api.knowledge_base.v1.model.metadata.toggle_builtin_request import (
    ToggleBuiltinRequest,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.toggle_builtin_response import (
    ToggleBuiltinResponse,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_request import (
    UpdateDocumentRequest,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_request_body import (
    DocumentMetadata,
    OperationData,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_response import (
    UpdateDocumentResponse,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.update_request import (
    UpdateRequest,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.update_response import (
    UpdateResponse,
)


class TestCreateRequest:
    def test_builder_pattern(self):
        from dify_oapi.api.knowledge_base.v1.model.metadata.create_request_body import CreateRequestBody

        request_body = CreateRequestBody.builder().type("string").name("test-metadata").build()

        request = CreateRequest.builder().dataset_id("dataset-123").request_body(request_body).build()

        assert request.dataset_id == "dataset-123"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.request_body.type == "string"
        assert request.request_body.name == "test-metadata"

    def test_http_method_and_uri(self):
        request = CreateRequest.builder().build()
        assert request.http_method.name == "POST"
        assert request.uri == "/v1/datasets/:dataset_id/metadata"


class TestCreateResponse:
    def test_direct_instantiation(self):
        response = CreateResponse(id="meta-123", type="string", name="test-metadata")

        assert response.id == "meta-123"
        assert response.type == "string"
        assert response.name == "test-metadata"


class TestListRequest:
    def test_builder_pattern(self):
        request = ListRequest.builder().dataset_id("dataset-123").build()

        assert request.dataset_id == "dataset-123"
        assert request.paths["dataset_id"] == "dataset-123"

    def test_http_method_and_uri(self):
        request = ListRequest.builder().build()
        assert request.http_method.name == "GET"
        assert request.uri == "/v1/datasets/:dataset_id/metadata"


class TestListResponse:
    def test_direct_instantiation(self):
        metadata_info = MetadataInfo(id="meta-123", type="string", name="test-metadata")
        response = ListResponse(doc_metadata=[metadata_info], built_in_field_enabled=True)

        assert len(response.doc_metadata) == 1
        assert response.doc_metadata[0].id == "meta-123"
        assert response.built_in_field_enabled is True

    def test_empty_metadata_list(self):
        response = ListResponse(doc_metadata=[], built_in_field_enabled=False)
        assert response.doc_metadata == []
        assert response.built_in_field_enabled is False


class TestUpdateRequest:
    def test_builder_pattern(self):
        from dify_oapi.api.knowledge_base.v1.model.metadata.update_request_body import UpdateRequestBody

        request_body = UpdateRequestBody.builder().name("updated-name").build()

        request = (
            UpdateRequest.builder().dataset_id("dataset-123").metadata_id("meta-123").request_body(request_body).build()
        )

        assert request.dataset_id == "dataset-123"
        assert request.metadata_id == "meta-123"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["metadata_id"] == "meta-123"
        assert request.request_body.name == "updated-name"

    def test_http_method_and_uri(self):
        request = UpdateRequest.builder().build()
        assert request.http_method.name == "PATCH"
        assert request.uri == "/v1/datasets/:dataset_id/metadata/:metadata_id"


class TestUpdateResponse:
    def test_direct_instantiation(self):
        response = UpdateResponse(id="meta-123", type="string", name="updated-name")

        assert response.id == "meta-123"
        assert response.type == "string"
        assert response.name == "updated-name"


class TestDeleteRequest:
    def test_builder_pattern(self):
        request = DeleteRequest.builder().dataset_id("dataset-123").metadata_id("meta-123").build()

        assert request.dataset_id == "dataset-123"
        assert request.metadata_id == "meta-123"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["metadata_id"] == "meta-123"

    def test_http_method_and_uri(self):
        request = DeleteRequest.builder().build()
        assert request.http_method.name == "DELETE"
        assert request.uri == "/v1/datasets/:dataset_id/metadata/:metadata_id"


class TestDeleteResponse:
    def test_empty_response(self):
        response = DeleteResponse()
        assert isinstance(response, DeleteResponse)


class TestToggleBuiltinRequest:
    def test_builder_pattern(self):
        request = ToggleBuiltinRequest.builder().dataset_id("dataset-123").action("enable").build()

        assert request.dataset_id == "dataset-123"
        assert request.action == "enable"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["action"] == "enable"

    def test_disable_action(self):
        request = ToggleBuiltinRequest.builder().dataset_id("dataset-123").action("disable").build()

        assert request.dataset_id == "dataset-123"
        assert request.action == "disable"

    def test_http_method_and_uri(self):
        request = ToggleBuiltinRequest.builder().build()
        assert request.http_method.name == "POST"
        assert request.uri == "/v1/datasets/:dataset_id/metadata/built-in/:action"


class TestToggleBuiltinResponse:
    def test_direct_instantiation(self):
        response = ToggleBuiltinResponse(result="success")
        assert response.result == "success"


class TestDocumentMetadata:
    def test_direct_instantiation(self):
        metadata = DocumentMetadata(id="meta-123", value="test-value", name="test-name")

        assert metadata.id == "meta-123"
        assert metadata.value == "test-value"
        assert metadata.name == "test-name"


class TestOperationData:
    def test_direct_instantiation(self):
        metadata = DocumentMetadata(id="meta-123", value="test-value", name="test-name")
        operation_data = OperationData(document_id="doc-123", metadata_list=[metadata])

        assert operation_data.document_id == "doc-123"
        assert len(operation_data.metadata_list) == 1
        assert operation_data.metadata_list[0].id == "meta-123"

    def test_empty_metadata_list(self):
        operation_data = OperationData(document_id="doc-123", metadata_list=[])
        assert operation_data.document_id == "doc-123"
        assert operation_data.metadata_list == []


class TestUpdateDocumentRequest:
    def test_builder_pattern(self):
        from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_request_body import (
            UpdateDocumentRequestBody,
        )

        metadata = DocumentMetadata(id="meta-123", value="test-value", name="test-name")
        operation_data = OperationData(document_id="doc-123", metadata_list=[metadata])

        request_body = UpdateDocumentRequestBody.builder().operation_data([operation_data]).build()

        request = UpdateDocumentRequest.builder().dataset_id("dataset-123").request_body(request_body).build()

        assert request.dataset_id == "dataset-123"
        assert request.paths["dataset_id"] == "dataset-123"
        assert len(request.request_body.operation_data) == 1
        assert request.request_body.operation_data[0].document_id == "doc-123"

    def test_http_method_and_uri(self):
        request = UpdateDocumentRequest.builder().build()
        assert request.http_method.name == "POST"
        assert request.uri == "/v1/datasets/:dataset_id/documents/metadata"

    def test_complex_nested_structure(self):
        from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_request_body import (
            UpdateDocumentRequestBody,
        )

        metadata1 = DocumentMetadata(id="meta-1", value="value-1", name="name-1")
        metadata2 = DocumentMetadata(id="meta-2", value="value-2", name="name-2")

        operation_data1 = OperationData(document_id="doc-1", metadata_list=[metadata1])
        operation_data2 = OperationData(document_id="doc-2", metadata_list=[metadata2])

        request_body = UpdateDocumentRequestBody(operation_data=[operation_data1, operation_data2])
        request = UpdateDocumentRequest.builder().dataset_id("dataset-123").request_body(request_body).build()

        assert request.dataset_id == "dataset-123"
        assert len(request.request_body.operation_data) == 2
        assert request.request_body.operation_data[0].document_id == "doc-1"
        assert request.request_body.operation_data[1].document_id == "doc-2"


class TestUpdateDocumentResponse:
    def test_direct_instantiation(self):
        response = UpdateDocumentResponse(result="success")
        assert response.result == "success"


class TestMetadataModelsIntegration:
    def test_create_to_list_integration(self):
        # Test that create response can be used in list response
        create_response = CreateResponse(id="meta-123", type="string", name="test-metadata")

        # Convert to MetadataInfo for list response
        metadata_info = MetadataInfo(id=create_response.id, type=create_response.type, name=create_response.name)

        list_response = ListResponse(doc_metadata=[metadata_info], built_in_field_enabled=True)

        assert len(list_response.doc_metadata) == 1
        assert list_response.doc_metadata[0].id == "meta-123"
        assert list_response.doc_metadata[0].name == "test-metadata"

    def test_update_to_metadata_info_integration(self):
        # Test that update response can be converted to metadata info
        update_response = UpdateResponse(id="meta-123", type="string", name="updated-name")

        metadata_info = MetadataInfo(id=update_response.id, type=update_response.type, name=update_response.name)

        assert isinstance(metadata_info, MetadataInfo)
        assert metadata_info.id == "meta-123"
        assert metadata_info.name == "updated-name"

    def test_document_metadata_nested_structure(self):
        from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_request_body import (
            UpdateDocumentRequestBody,
        )

        # Test complex nested structure usage
        metadata = DocumentMetadata(id="meta-123", value="test-value", name="test-name")

        operation_data = OperationData(document_id="doc-123", metadata_list=[metadata])

        request_body = UpdateDocumentRequestBody(operation_data=[operation_data])

        request = UpdateDocumentRequest.builder().dataset_id("dataset-123").request_body(request_body).build()

        assert request.dataset_id == "dataset-123"
        assert len(request.request_body.operation_data) == 1
        assert request.request_body.operation_data[0].document_id == "doc-123"
        assert len(request.request_body.operation_data[0].metadata_list) == 1
        assert request.request_body.operation_data[0].metadata_list[0].id == "meta-123"
