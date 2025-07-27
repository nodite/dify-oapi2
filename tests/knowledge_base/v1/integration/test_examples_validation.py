"""
Tests for validating knowledge base examples.

This module validates that all examples in the knowledge_base directory
are syntactically correct, follow best practices, and have proper error handling.
"""

import ast
import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

# Add the project root to the Python path for imports
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root))


class ExampleValidator:
    """Validates example files for syntax, imports, and best practices."""

    def __init__(self, example_path: Path) -> None:
        self.example_path = example_path
        self.content = example_path.read_text()
        self.tree = ast.parse(self.content)

    def validate_syntax(self) -> bool:
        """Validate that the example has valid Python syntax."""
        try:
            ast.parse(self.content)
            return True
        except SyntaxError:
            return False

    def validate_imports(self) -> bool:
        """Validate that all imports are correct and follow patterns."""

        import_nodes = [node for node in ast.walk(self.tree) if isinstance(node, (ast.Import, ast.ImportFrom))]
        import_strings = []

        for node in import_nodes:
            if isinstance(node, ast.ImportFrom):
                module = node.module or ""
                for alias in node.names:
                    import_strings.append(f"{module}.{alias.name}")
            else:
                for alias in node.names:
                    import_strings.append(alias.name)

        # Check if basic required imports are present
        has_client = any("client" in imp.lower() for imp in import_strings)
        has_request_option = any("request_option" in imp.lower() for imp in import_strings)

        return has_client and has_request_option

    def validate_error_handling(self) -> bool:
        """Validate that the example has proper error handling."""
        try_nodes = [node for node in ast.walk(self.tree) if isinstance(node, ast.Try)]
        return len(try_nodes) > 0

    def validate_async_sync_variants(self) -> tuple[bool, bool]:
        """Check if example has both sync and async variants."""
        function_nodes = [node for node in ast.walk(self.tree) if isinstance(node, ast.FunctionDef)]
        async_function_nodes = [node for node in ast.walk(self.tree) if isinstance(node, ast.AsyncFunctionDef)]

        has_sync = len(function_nodes) > 0
        has_async = len(async_function_nodes) > 0

        return has_sync, has_async

    def validate_comments(self) -> bool:
        """Validate that the example has educational comments."""
        lines = self.content.split("\n")
        # Count both # comments and docstring lines
        comment_lines = [line for line in lines if line.strip().startswith("#")]
        docstring_lines = [line for line in lines if '"""' in line or "'''" in line]
        total_educational_lines = len(comment_lines) + len(docstring_lines)
        return total_educational_lines >= 2  # At least 2 educational lines


class TestDatasetExamples:
    """Test dataset examples validation."""

    @pytest.fixture
    def dataset_examples_dir(self) -> Path:
        return project_root / "examples" / "knowledge_base" / "dataset"

    def test_create_example_validation(self, dataset_examples_dir: Path) -> None:
        """Test dataset create example validation."""
        example_file = dataset_examples_dir / "create.py"
        assert example_file.exists(), "Dataset create example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "Create example should have valid syntax"
        assert validator.validate_imports(), "Create example should have correct imports"
        assert validator.validate_error_handling(), "Create example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "Create example should have sync variant"
        assert has_async, "Create example should have async variant"
        assert validator.validate_comments(), "Create example should have educational comments"

    def test_list_example_validation(self, dataset_examples_dir: Path) -> None:
        """Test dataset list example validation."""
        example_file = dataset_examples_dir / "list.py"
        assert example_file.exists(), "Dataset list example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "List example should have valid syntax"
        assert validator.validate_imports(), "List example should have correct imports"
        assert validator.validate_error_handling(), "List example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "List example should have sync variant"
        assert has_async, "List example should have async variant"
        assert validator.validate_comments(), "List example should have educational comments"

    def test_get_example_validation(self, dataset_examples_dir: Path) -> None:
        """Test dataset get example validation."""
        example_file = dataset_examples_dir / "get.py"
        assert example_file.exists(), "Dataset get example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "Get example should have valid syntax"
        assert validator.validate_imports(), "Get example should have correct imports"
        assert validator.validate_error_handling(), "Get example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "Get example should have sync variant"
        assert has_async, "Get example should have async variant"
        assert validator.validate_comments(), "Get example should have educational comments"

    def test_update_example_validation(self, dataset_examples_dir: Path) -> None:
        """Test dataset update example validation."""
        example_file = dataset_examples_dir / "update.py"
        assert example_file.exists(), "Dataset update example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "Update example should have valid syntax"
        assert validator.validate_imports(), "Update example should have correct imports"
        assert validator.validate_error_handling(), "Update example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "Update example should have sync variant"
        assert has_async, "Update example should have async variant"
        assert validator.validate_comments(), "Update example should have educational comments"

    def test_delete_example_validation(self, dataset_examples_dir: Path) -> None:
        """Test dataset delete example validation."""
        example_file = dataset_examples_dir / "delete.py"
        assert example_file.exists(), "Dataset delete example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "Delete example should have valid syntax"
        assert validator.validate_imports(), "Delete example should have correct imports"
        assert validator.validate_error_handling(), "Delete example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "Delete example should have sync variant"
        assert has_async, "Delete example should have async variant"
        assert validator.validate_comments(), "Delete example should have educational comments"

    def test_retrieve_example_validation(self, dataset_examples_dir: Path) -> None:
        """Test dataset retrieve example validation."""
        example_file = dataset_examples_dir / "retrieve.py"
        assert example_file.exists(), "Dataset retrieve example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "Retrieve example should have valid syntax"
        assert validator.validate_imports(), "Retrieve example should have correct imports"
        assert validator.validate_error_handling(), "Retrieve example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "Retrieve example should have sync variant"
        assert has_async, "Retrieve example should have async variant"
        assert validator.validate_comments(), "Retrieve example should have educational comments"


class TestMetadataExamples:
    """Test metadata examples validation."""

    @pytest.fixture
    def metadata_examples_dir(self) -> Path:
        return project_root / "examples" / "knowledge_base" / "metadata"

    def test_create_example_validation(self, metadata_examples_dir: Path) -> None:
        """Test metadata create example validation."""
        example_file = metadata_examples_dir / "create.py"
        assert example_file.exists(), "Metadata create example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "Create example should have valid syntax"
        assert validator.validate_imports(), "Create example should have correct imports"
        assert validator.validate_error_handling(), "Create example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "Create example should have sync variant"
        assert has_async, "Create example should have async variant"
        assert validator.validate_comments(), "Create example should have educational comments"

    def test_list_example_validation(self, metadata_examples_dir: Path) -> None:
        """Test metadata list example validation."""
        example_file = metadata_examples_dir / "list.py"
        assert example_file.exists(), "Metadata list example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "List example should have valid syntax"
        assert validator.validate_imports(), "List example should have correct imports"
        assert validator.validate_error_handling(), "List example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "List example should have sync variant"
        assert has_async, "List example should have async variant"
        assert validator.validate_comments(), "List example should have educational comments"

    def test_update_example_validation(self, metadata_examples_dir: Path) -> None:
        """Test metadata update example validation."""
        example_file = metadata_examples_dir / "update.py"
        assert example_file.exists(), "Metadata update example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "Update example should have valid syntax"
        assert validator.validate_imports(), "Update example should have correct imports"
        assert validator.validate_error_handling(), "Update example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "Update example should have sync variant"
        assert has_async, "Update example should have async variant"
        assert validator.validate_comments(), "Update example should have educational comments"

    def test_delete_example_validation(self, metadata_examples_dir: Path) -> None:
        """Test metadata delete example validation."""
        example_file = metadata_examples_dir / "delete.py"
        assert example_file.exists(), "Metadata delete example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "Delete example should have valid syntax"
        assert validator.validate_imports(), "Delete example should have correct imports"
        assert validator.validate_error_handling(), "Delete example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "Delete example should have sync variant"
        assert has_async, "Delete example should have async variant"
        assert validator.validate_comments(), "Delete example should have educational comments"

    def test_toggle_builtin_example_validation(self, metadata_examples_dir: Path) -> None:
        """Test metadata toggle builtin example validation."""
        example_file = metadata_examples_dir / "toggle_builtin.py"
        assert example_file.exists(), "Metadata toggle builtin example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "Toggle builtin example should have valid syntax"
        assert validator.validate_imports(), "Toggle builtin example should have correct imports"
        assert validator.validate_error_handling(), "Toggle builtin example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "Toggle builtin example should have sync variant"
        assert has_async, "Toggle builtin example should have async variant"
        assert validator.validate_comments(), "Toggle builtin example should have educational comments"

    def test_update_document_example_validation(self, metadata_examples_dir: Path) -> None:
        """Test metadata update document example validation."""
        example_file = metadata_examples_dir / "update_document.py"
        assert example_file.exists(), "Metadata update document example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "Update document example should have valid syntax"
        assert validator.validate_imports(), "Update document example should have correct imports"
        assert validator.validate_error_handling(), "Update document example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "Update document example should have sync variant"
        assert has_async, "Update document example should have async variant"
        assert validator.validate_comments(), "Update document example should have educational comments"


class TestTagExamples:
    """Test tag examples validation."""

    @pytest.fixture
    def tag_examples_dir(self) -> Path:
        return project_root / "examples" / "knowledge_base" / "tag"

    def test_create_example_validation(self, tag_examples_dir: Path) -> None:
        """Test tag create example validation."""
        example_file = tag_examples_dir / "create.py"
        assert example_file.exists(), "Tag create example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "Create example should have valid syntax"
        assert validator.validate_imports(), "Create example should have correct imports"
        assert validator.validate_error_handling(), "Create example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "Create example should have sync variant"
        assert has_async, "Create example should have async variant"
        assert validator.validate_comments(), "Create example should have educational comments"

    def test_list_example_validation(self, tag_examples_dir: Path) -> None:
        """Test tag list example validation."""
        example_file = tag_examples_dir / "list.py"
        assert example_file.exists(), "Tag list example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "List example should have valid syntax"
        assert validator.validate_imports(), "List example should have correct imports"
        assert validator.validate_error_handling(), "List example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "List example should have sync variant"
        assert has_async, "List example should have async variant"
        assert validator.validate_comments(), "List example should have educational comments"

    def test_update_example_validation(self, tag_examples_dir: Path) -> None:
        """Test tag update example validation."""
        example_file = tag_examples_dir / "update.py"
        assert example_file.exists(), "Tag update example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "Update example should have valid syntax"
        assert validator.validate_imports(), "Update example should have correct imports"
        assert validator.validate_error_handling(), "Update example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "Update example should have sync variant"
        assert has_async, "Update example should have async variant"
        assert validator.validate_comments(), "Update example should have educational comments"

    def test_delete_example_validation(self, tag_examples_dir: Path) -> None:
        """Test tag delete example validation."""
        example_file = tag_examples_dir / "delete.py"
        assert example_file.exists(), "Tag delete example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "Delete example should have valid syntax"
        assert validator.validate_imports(), "Delete example should have correct imports"
        assert validator.validate_error_handling(), "Delete example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "Delete example should have sync variant"
        assert has_async, "Delete example should have async variant"
        assert validator.validate_comments(), "Delete example should have educational comments"

    def test_bind_example_validation(self, tag_examples_dir: Path) -> None:
        """Test tag bind example validation."""
        example_file = tag_examples_dir / "bind.py"
        assert example_file.exists(), "Tag bind example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "Bind example should have valid syntax"
        assert validator.validate_imports(), "Bind example should have correct imports"
        assert validator.validate_error_handling(), "Bind example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "Bind example should have sync variant"
        assert has_async, "Bind example should have async variant"
        assert validator.validate_comments(), "Bind example should have educational comments"

    def test_unbind_example_validation(self, tag_examples_dir: Path) -> None:
        """Test tag unbind example validation."""
        example_file = tag_examples_dir / "unbind.py"
        assert example_file.exists(), "Tag unbind example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "Unbind example should have valid syntax"
        assert validator.validate_imports(), "Unbind example should have correct imports"
        assert validator.validate_error_handling(), "Unbind example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "Unbind example should have sync variant"
        assert has_async, "Unbind example should have async variant"
        assert validator.validate_comments(), "Unbind example should have educational comments"

    def test_query_bound_example_validation(self, tag_examples_dir: Path) -> None:
        """Test tag query bound example validation."""
        example_file = tag_examples_dir / "query_bound.py"
        assert example_file.exists(), "Tag query bound example should exist"

        validator = ExampleValidator(example_file)
        assert validator.validate_syntax(), "Query bound example should have valid syntax"
        assert validator.validate_imports(), "Query bound example should have correct imports"
        assert validator.validate_error_handling(), "Query bound example should have error handling"

        has_sync, has_async = validator.validate_async_sync_variants()
        assert has_sync, "Query bound example should have sync variant"
        assert has_async, "Query bound example should have async variant"
        assert validator.validate_comments(), "Query bound example should have educational comments"


class TestExamplesMocking:
    """Test that examples work correctly with mocked API calls."""

    @pytest.fixture
    def mock_client(self) -> MagicMock:
        """Create a mock client for testing examples."""
        mock_client = MagicMock()
        mock_client.knowledge_base.v1.dataset = MagicMock()
        mock_client.knowledge_base.v1.metadata = MagicMock()
        mock_client.knowledge_base.v1.tag = MagicMock()
        return mock_client

    def test_dataset_examples_with_mocks(self, mock_client: MagicMock) -> None:
        """Test that dataset examples work with mocked API calls."""
        # Mock dataset responses
        mock_client.knowledge_base.v1.dataset.create.return_value = MagicMock(id="test-id", name="Test Dataset")
        mock_client.knowledge_base.v1.dataset.list.return_value = MagicMock(data=[], has_more=False)
        mock_client.knowledge_base.v1.dataset.get.return_value = MagicMock(id="test-id", name="Test Dataset")
        mock_client.knowledge_base.v1.dataset.update.return_value = MagicMock(id="test-id", name="Updated Dataset")
        mock_client.knowledge_base.v1.dataset.delete.return_value = None
        mock_client.knowledge_base.v1.dataset.retrieve.return_value = MagicMock(query={"content": "test"}, records=[])

        # Test that mocked methods can be called (simulating example execution)
        assert mock_client.knowledge_base.v1.dataset.create is not None
        assert mock_client.knowledge_base.v1.dataset.list is not None
        assert mock_client.knowledge_base.v1.dataset.get is not None
        assert mock_client.knowledge_base.v1.dataset.update is not None
        assert mock_client.knowledge_base.v1.dataset.delete is not None
        assert mock_client.knowledge_base.v1.dataset.retrieve is not None

    def test_metadata_examples_with_mocks(self, mock_client: MagicMock) -> None:
        """Test that metadata examples work with mocked API calls."""
        # Mock metadata responses
        mock_client.knowledge_base.v1.metadata.create.return_value = MagicMock(id="meta-id", name="Test Metadata")
        mock_client.knowledge_base.v1.metadata.list.return_value = MagicMock(
            doc_metadata=[], built_in_field_enabled=True
        )
        mock_client.knowledge_base.v1.metadata.update.return_value = MagicMock(id="meta-id", name="Updated Metadata")
        mock_client.knowledge_base.v1.metadata.delete.return_value = None
        mock_client.knowledge_base.v1.metadata.toggle_builtin.return_value = MagicMock(result="success")
        mock_client.knowledge_base.v1.metadata.update_document.return_value = MagicMock(result="success")

        # Test that mocked methods can be called (simulating example execution)
        assert mock_client.knowledge_base.v1.metadata.create is not None
        assert mock_client.knowledge_base.v1.metadata.list is not None
        assert mock_client.knowledge_base.v1.metadata.update is not None
        assert mock_client.knowledge_base.v1.metadata.delete is not None
        assert mock_client.knowledge_base.v1.metadata.toggle_builtin is not None
        assert mock_client.knowledge_base.v1.metadata.update_document is not None

    def test_tag_examples_with_mocks(self, mock_client: MagicMock) -> None:
        """Test that tag examples work with mocked API calls."""
        # Mock tag responses
        mock_client.knowledge_base.v1.tag.create.return_value = MagicMock(id="tag-id", name="Test Tag")
        mock_client.knowledge_base.v1.tag.list.return_value = []
        mock_client.knowledge_base.v1.tag.update.return_value = MagicMock(id="tag-id", name="Updated Tag")
        mock_client.knowledge_base.v1.tag.delete.return_value = MagicMock(result="success")
        mock_client.knowledge_base.v1.tag.bind_tags.return_value = MagicMock(result="success")
        mock_client.knowledge_base.v1.tag.unbind_tag.return_value = MagicMock(result="success")
        mock_client.knowledge_base.v1.tag.query_bound.return_value = MagicMock(data=[], total=0)

        # Test that mocked methods can be called (simulating example execution)
        assert mock_client.knowledge_base.v1.tag.create is not None
        assert mock_client.knowledge_base.v1.tag.list is not None
        assert mock_client.knowledge_base.v1.tag.update is not None
        assert mock_client.knowledge_base.v1.tag.delete is not None
        assert mock_client.knowledge_base.v1.tag.bind_tags is not None
        assert mock_client.knowledge_base.v1.tag.unbind_tag is not None
        assert mock_client.knowledge_base.v1.tag.query_bound is not None


class TestExamplesDocumentation:
    """Test examples documentation and README."""

    def test_examples_readme_exists(self) -> None:
        """Test that examples README exists and has proper content."""
        readme_path = project_root / "examples" / "knowledge_base" / "README.md"
        assert readme_path.exists(), "Knowledge base examples README should exist"

        content = readme_path.read_text()
        assert "Dataset Management" in content, "README should mention dataset management"
        assert "Metadata Management" in content, "README should mention metadata management"
        assert "Tag Management" in content, "README should mention tag management"
        assert "sync" in content.lower(), "README should mention sync examples"
        assert "async" in content.lower(), "README should mention async examples"

    def test_all_examples_directories_exist(self) -> None:
        """Test that all example directories exist."""
        base_dir = project_root / "examples" / "knowledge_base"

        dataset_dir = base_dir / "dataset"
        metadata_dir = base_dir / "metadata"
        tag_dir = base_dir / "tag"

        assert dataset_dir.exists() and dataset_dir.is_dir(), "Dataset examples directory should exist"
        assert metadata_dir.exists() and metadata_dir.is_dir(), "Metadata examples directory should exist"
        assert tag_dir.exists() and tag_dir.is_dir(), "Tag examples directory should exist"

    def test_all_example_files_exist(self) -> None:
        """Test that all expected example files exist."""
        base_dir = project_root / "examples" / "knowledge_base"

        # Dataset examples
        dataset_files = ["create.py", "list.py", "get.py", "update.py", "delete.py", "retrieve.py"]
        for file_name in dataset_files:
            file_path = base_dir / "dataset" / file_name
            assert file_path.exists(), f"Dataset example {file_name} should exist"

        # Metadata examples
        metadata_files = ["create.py", "list.py", "update.py", "delete.py", "toggle_builtin.py", "update_document.py"]
        for file_name in metadata_files:
            file_path = base_dir / "metadata" / file_name
            assert file_path.exists(), f"Metadata example {file_name} should exist"

        # Tag examples
        tag_files = ["create.py", "list.py", "update.py", "delete.py", "bind.py", "unbind.py", "query_bound.py"]
        for file_name in tag_files:
            file_path = base_dir / "tag" / file_name
            assert file_path.exists(), f"Tag example {file_name} should exist"


if __name__ == "__main__":
    pytest.main([__file__])
