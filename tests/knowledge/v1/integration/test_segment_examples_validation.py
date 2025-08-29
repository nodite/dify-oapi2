#!/usr/bin/env python3
"""
Segment Examples Validation Tests

This module validates all segment examples for syntax, imports, and functionality.
"""

import ast
import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest


class TestSegmentExamplesValidation:
    """Test class for validating segment examples."""

    @pytest.fixture
    def examples_dir(self) -> Path:
        """Get the examples directory path."""
        return Path(__file__).parent.parent.parent.parent.parent / "examples" / "knowledge" / "segment"

    @pytest.fixture
    def example_files(self, examples_dir: Path) -> list[Path]:
        """Get all example Python files."""
        return list(examples_dir.glob("*.py"))

    def test_examples_directory_exists(self, examples_dir: Path) -> None:
        """Test that the examples directory exists."""
        assert examples_dir.exists(), f"Examples directory does not exist: {examples_dir}"
        assert examples_dir.is_dir(), f"Examples path is not a directory: {examples_dir}"

    def test_all_example_files_exist(self, examples_dir: Path) -> None:
        """Test that all required example files exist."""
        required_files = [
            "create.py",
            "list.py",
            "get.py",
            "update.py",
            "delete.py",
            "create_child_chunk.py",
            "list_child_chunks.py",
            "update_child_chunk.py",
            "delete_child_chunk.py",
        ]

        for filename in required_files:
            file_path = examples_dir / filename
            assert file_path.exists(), f"Required example file does not exist: {filename}"

    def test_example_syntax_validation(self, example_files: list[Path]) -> None:
        """Test that all example files have valid Python syntax."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            try:
                ast.parse(content)
            except SyntaxError as e:
                pytest.fail(f"Syntax error in {file_path.name}: {e}")

    def test_example_imports_validation(self, example_files: list[Path]) -> None:
        """Test that all example files have correct imports."""
        required_imports = [
            "asyncio",
            "os",
            "dify_oapi.client",
            "dify_oapi.core.model.request_option",
        ]

        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            tree = ast.parse(content)
            imports = []

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.append(node.module)

            for required_import in required_imports:
                assert any(required_import in imp for imp in imports), (
                    f"Missing required import '{required_import}' in {file_path.name}"
                )

    def test_environment_variable_validation(self, example_files: list[Path]) -> None:
        """Test that all examples validate required environment variables."""
        required_env_vars = ["API_KEY", "DATASET_ID", "DOCUMENT_ID"]

        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            for env_var in required_env_vars:
                assert f'os.getenv("{env_var}")' in content, f"Missing {env_var} validation in {file_path.name}"
                assert f'raise ValueError("{env_var} environment variable is required")' in content, (
                    f"Missing {env_var} error handling in {file_path.name}"
                )

    def test_example_prefix_usage(self, example_files: list[Path]) -> None:
        """Test that examples use '[Example]' prefix for safety."""
        # Skip this test for files that don't need [Example] prefix
        skip_files = {"list_child_chunks.py", "get.py"}

        for file_path in example_files:
            if file_path.name in skip_files:
                continue

            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for [Example] prefix in content strings
            assert "[Example]" in content, f"Missing '[Example]' prefix in {file_path.name}"

    def test_sync_async_function_pairs(self, example_files: list[Path]) -> None:
        """Test that examples have both sync and async function variants."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            tree = ast.parse(content)
            functions = []
            async_functions = []

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    functions.append(node.name)
                elif isinstance(node, ast.AsyncFunctionDef):
                    async_functions.append(node.name)

            # Check for sync and async pairs
            sync_functions = [f for f in functions if f != "main"]

            assert len(sync_functions) > 0, f"No sync functions found in {file_path.name}"
            assert len(async_functions) > 0, f"No async functions found in {file_path.name}"

    @patch.dict(
        os.environ,
        {
            "API_KEY": "test-api-key",
            "DATASET_ID": "test-dataset-id",
            "DOCUMENT_ID": "test-document-id",
            "SEGMENT_ID": "test-segment-id",
            "CHILD_CHUNK_ID": "test-child-chunk-id",
            "DOMAIN": "https://api.dify.ai",
        },
    )
    def test_create_example_logic(self, examples_dir: Path) -> None:
        """Test create example logic with mocked API calls."""
        with patch("dify_oapi.client.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_response = MagicMock()
            mock_response.success = True
            mock_response.data = [MagicMock(id="test-id", content="[Example] Test content")]

            mock_client.knowledge.v1.segment.create.return_value = mock_response
            mock_client.knowledge.v1.segment.acreate.return_value = mock_response
            mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

            # Import and run the example
            sys.path.insert(0, str(examples_dir))
            try:
                import create

                create.create_segment_sync()
            finally:
                sys.path.remove(str(examples_dir))
                if "create" in sys.modules:
                    del sys.modules["create"]

    @patch.dict(
        os.environ,
        {
            "API_KEY": "test-api-key",
            "DATASET_ID": "test-dataset-id",
            "DOCUMENT_ID": "test-document-id",
            "DOMAIN": "https://api.dify.ai",
        },
    )
    def test_list_example_logic(self, examples_dir: Path) -> None:
        """Test list example logic with mocked API calls."""
        with patch("dify_oapi.client.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_response = MagicMock()
            mock_response.success = True
            mock_response.data = [MagicMock(id="test-id", content="Test content")]
            mock_response.total = 1

            mock_client.knowledge.v1.segment.list.return_value = mock_response
            mock_client.knowledge.v1.segment.alist.return_value = mock_response
            mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

            # Import and run the example
            sys.path.insert(0, str(examples_dir))
            try:
                import list as list_module

                list_module.list_segments_sync()
            finally:
                sys.path.remove(str(examples_dir))
                if "list" in sys.modules:
                    del sys.modules["list"]

    @patch.dict(
        os.environ,
        {
            "API_KEY": "test-api-key",
            "DATASET_ID": "test-dataset-id",
            "DOCUMENT_ID": "test-document-id",
            "SEGMENT_ID": "test-segment-id",
            "DOMAIN": "https://api.dify.ai",
        },
    )
    def test_get_example_logic(self, examples_dir: Path) -> None:
        """Test get example logic with mocked API calls."""
        with patch("dify_oapi.client.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_response = MagicMock()
            mock_response.success = True
            mock_response.data = MagicMock(id="test-id", content="Test content")

            mock_client.knowledge.v1.segment.get.return_value = mock_response
            mock_client.knowledge.v1.segment.aget.return_value = mock_response
            mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

            # Import and run the example
            sys.path.insert(0, str(examples_dir))
            try:
                import get

                get.get_segment_sync()
            finally:
                sys.path.remove(str(examples_dir))
                if "get" in sys.modules:
                    del sys.modules["get"]

    @patch.dict(
        os.environ,
        {
            "API_KEY": "test-api-key",
            "DATASET_ID": "test-dataset-id",
            "DOCUMENT_ID": "test-document-id",
            "SEGMENT_ID": "test-segment-id",
            "DOMAIN": "https://api.dify.ai",
        },
    )
    def test_update_example_logic(self, examples_dir: Path) -> None:
        """Test update example logic with mocked API calls."""
        with patch("dify_oapi.client.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_response = MagicMock()
            mock_response.success = True
            mock_response.data = MagicMock(id="test-id", content="[Example] Updated content")

            mock_client.knowledge.v1.segment.update.return_value = mock_response
            mock_client.knowledge.v1.segment.aupdate.return_value = mock_response
            mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

            # Import and run the example
            sys.path.insert(0, str(examples_dir))
            try:
                import update

                update.update_segment_sync()
            finally:
                sys.path.remove(str(examples_dir))
                if "update" in sys.modules:
                    del sys.modules["update"]

    @patch.dict(
        os.environ,
        {
            "API_KEY": "test-api-key",
            "DATASET_ID": "test-dataset-id",
            "DOCUMENT_ID": "test-document-id",
            "SEGMENT_ID": "test-segment-id",
            "DOMAIN": "https://api.dify.ai",
        },
    )
    def test_delete_example_logic(self, examples_dir: Path) -> None:
        """Test delete example logic with mocked API calls."""
        with patch("dify_oapi.client.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_response = MagicMock()
            mock_response.success = True

            mock_client.knowledge.v1.segment.delete.return_value = mock_response
            mock_client.knowledge.v1.segment.adelete.return_value = mock_response
            mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

            # Import and run the example
            sys.path.insert(0, str(examples_dir))
            try:
                import delete

                delete.delete_segment_sync()
            finally:
                sys.path.remove(str(examples_dir))
                if "delete" in sys.modules:
                    del sys.modules["delete"]

    @patch.dict(
        os.environ,
        {
            "API_KEY": "test-api-key",
            "DATASET_ID": "test-dataset-id",
            "DOCUMENT_ID": "test-document-id",
            "SEGMENT_ID": "test-segment-id",
            "DOMAIN": "https://api.dify.ai",
        },
    )
    def test_create_child_chunk_example_logic(self, examples_dir: Path) -> None:
        """Test create child chunk example logic with mocked API calls."""
        with patch("dify_oapi.client.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_response = MagicMock()
            mock_response.success = True
            mock_response.data = MagicMock(id="test-id", content="[Example] Child chunk content")

            mock_client.knowledge.v1.segment.create_child_chunk.return_value = mock_response
            mock_client.knowledge.v1.segment.acreate_child_chunk.return_value = mock_response
            mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

            # Import and run the example
            sys.path.insert(0, str(examples_dir))
            try:
                import create_child_chunk

                create_child_chunk.create_child_chunk_sync()
            finally:
                sys.path.remove(str(examples_dir))
                if "create_child_chunk" in sys.modules:
                    del sys.modules["create_child_chunk"]

    @patch.dict(
        os.environ,
        {
            "API_KEY": "test-api-key",
            "DATASET_ID": "test-dataset-id",
            "DOCUMENT_ID": "test-document-id",
            "SEGMENT_ID": "test-segment-id",
            "DOMAIN": "https://api.dify.ai",
        },
    )
    def test_list_child_chunks_example_logic(self, examples_dir: Path) -> None:
        """Test list child chunks example logic with mocked API calls."""
        with patch("dify_oapi.client.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_response = MagicMock()
            mock_response.success = True
            mock_response.data = [MagicMock(id="test-id", content="Child chunk content")]
            mock_response.total = 1

            mock_client.knowledge.v1.segment.list_child_chunks.return_value = mock_response
            mock_client.knowledge.v1.segment.alist_child_chunks.return_value = mock_response
            mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

            # Import and run the example
            sys.path.insert(0, str(examples_dir))
            try:
                import list_child_chunks

                list_child_chunks.list_child_chunks_sync()
            finally:
                sys.path.remove(str(examples_dir))
                if "list_child_chunks" in sys.modules:
                    del sys.modules["list_child_chunks"]

    @patch.dict(
        os.environ,
        {
            "API_KEY": "test-api-key",
            "DATASET_ID": "test-dataset-id",
            "DOCUMENT_ID": "test-document-id",
            "SEGMENT_ID": "test-segment-id",
            "CHILD_CHUNK_ID": "test-child-chunk-id",
            "DOMAIN": "https://api.dify.ai",
        },
    )
    def test_update_child_chunk_example_logic(self, examples_dir: Path) -> None:
        """Test update child chunk example logic with mocked API calls."""
        with patch("dify_oapi.client.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_response = MagicMock()
            mock_response.success = True
            mock_response.data = MagicMock(id="test-id", content="[Example] Updated child chunk content")

            mock_client.knowledge.v1.segment.update_child_chunk.return_value = mock_response
            mock_client.knowledge.v1.segment.aupdate_child_chunk.return_value = mock_response
            mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

            # Import and run the example
            sys.path.insert(0, str(examples_dir))
            try:
                import update_child_chunk

                update_child_chunk.update_child_chunk_sync()
            finally:
                sys.path.remove(str(examples_dir))
                if "update_child_chunk" in sys.modules:
                    del sys.modules["update_child_chunk"]

    @patch.dict(
        os.environ,
        {
            "API_KEY": "test-api-key",
            "DATASET_ID": "test-dataset-id",
            "DOCUMENT_ID": "test-document-id",
            "SEGMENT_ID": "test-segment-id",
            "CHILD_CHUNK_ID": "test-child-chunk-id",
            "DOMAIN": "https://api.dify.ai",
        },
    )
    def test_delete_child_chunk_example_logic(self, examples_dir: Path) -> None:
        """Test delete child chunk example logic with mocked API calls."""
        with patch("dify_oapi.client.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_response = MagicMock()
            mock_response.success = True

            mock_client.knowledge.v1.segment.delete_child_chunk.return_value = mock_response
            mock_client.knowledge.v1.segment.adelete_child_chunk.return_value = mock_response
            mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

            # Import and run the example
            sys.path.insert(0, str(examples_dir))
            try:
                import delete_child_chunk

                delete_child_chunk.delete_child_chunk_sync()
            finally:
                sys.path.remove(str(examples_dir))
                if "delete_child_chunk" in sys.modules:
                    del sys.modules["delete_child_chunk"]

    def test_error_handling_validation(self, example_files: list[Path]) -> None:
        """Test that examples have proper error handling."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for try-catch blocks
            assert "try:" in content, f"Missing try block in {file_path.name}"
            assert "except Exception as e:" in content, f"Missing exception handling in {file_path.name}"

            # Check for response.success validation
            assert "response.success" in content, f"Missing response.success check in {file_path.name}"

    def test_main_function_exists(self, example_files: list[Path]) -> None:
        """Test that all examples have a main function."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            tree = ast.parse(content)
            functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

            assert "main" in functions, f"Missing main function in {file_path.name}"
            assert 'if __name__ == "__main__":' in content, f"Missing main guard in {file_path.name}"
