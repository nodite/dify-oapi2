"""Tests to validate the chatflow module structure."""

from pathlib import Path


class TestChatflowModuleStructure:
    """Test class for validating chatflow module structure."""

    def test_module_directories_exist(self):
        """Test that all required module directories exist."""
        base_path = Path(__file__).parent.parent.parent / "dify_oapi" / "api" / "chatflow"

        # Check main directories
        assert (base_path).exists(), "chatflow directory should exist"
        assert (base_path / "v1").exists(), "v1 directory should exist"
        assert (base_path / "v1" / "model").exists(), "model directory should exist"
        assert (base_path / "v1" / "resource").exists(), "resource directory should exist"

    def test_init_files_exist(self):
        """Test that all required __init__.py files exist."""
        base_path = Path(__file__).parent.parent.parent / "dify_oapi" / "api" / "chatflow"

        # Check __init__.py files
        assert (base_path / "__init__.py").exists(), "chatflow __init__.py should exist"
        assert (base_path / "v1" / "__init__.py").exists(), "v1 __init__.py should exist"
        assert (base_path / "v1" / "model" / "__init__.py").exists(), "model __init__.py should exist"
        assert (base_path / "v1" / "resource" / "__init__.py").exists(), "resource __init__.py should exist"

    def test_service_file_exists(self):
        """Test that the service.py file exists."""
        base_path = Path(__file__).parent.parent.parent / "dify_oapi" / "api" / "chatflow"
        assert (base_path / "service.py").exists(), "service.py should exist"

    def test_version_file_exists(self):
        """Test that the version.py file exists."""
        base_path = Path(__file__).parent.parent.parent / "dify_oapi" / "api" / "chatflow" / "v1"
        assert (base_path / "version.py").exists(), "version.py should exist"

    def test_module_imports_work(self):
        """Test that module imports work correctly."""
        # Test chatflow service import
        from dify_oapi.api.chatflow import ChatflowService

        assert ChatflowService is not None, "ChatflowService should be importable"

        # Test v1 version import
        from dify_oapi.api.chatflow.v1 import V1

        assert V1 is not None, "V1 should be importable"

    def test_test_directories_exist(self):
        """Test that all required test directories exist."""
        base_path = Path(__file__).parent

        # Check test directories
        assert (base_path / "v1").exists(), "v1 test directory should exist"
        assert (base_path / "v1" / "model").exists(), "model test directory should exist"
        assert (base_path / "v1" / "resource").exists(), "resource test directory should exist"
        assert (base_path / "v1" / "integration").exists(), "integration test directory should exist"

    def test_test_init_files_exist(self):
        """Test that test __init__.py files exist."""
        base_path = Path(__file__).parent

        # Check test __init__.py files
        assert (base_path / "__init__.py").exists(), "chatflow test __init__.py should exist"
        assert (base_path / "v1" / "__init__.py").exists(), "v1 test __init__.py should exist"
