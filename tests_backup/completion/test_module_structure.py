"""Tests to validate the completion module structure."""

from pathlib import Path


class TestCompletionModuleStructure:
    """Test class for validating completion module structure."""

    def test_module_directories_exist(self):
        """Test that all required module directories exist."""
        base_path = Path(__file__).parent.parent.parent / "dify_oapi" / "api" / "completion"

        # Check main directories
        assert (base_path).exists(), "completion directory should exist"
        assert (base_path / "v1").exists(), "v1 directory should exist"
        assert (base_path / "v1" / "model").exists(), "model directory should exist"
        assert (base_path / "v1" / "resource").exists(), "resource directory should exist"

    def test_init_files_exist(self):
        """Test that all required __init__.py files exist."""
        base_path = Path(__file__).parent.parent.parent / "dify_oapi" / "api" / "completion"

        # Check __init__.py files
        assert (base_path / "__init__.py").exists(), "completion __init__.py should exist"
        assert (base_path / "v1" / "__init__.py").exists(), "v1 __init__.py should exist"
        assert (base_path / "v1" / "model" / "__init__.py").exists(), "model __init__.py should exist"
        assert (base_path / "v1" / "resource" / "__init__.py").exists(), "resource __init__.py should exist"

    def test_service_file_exists(self):
        """Test that the service.py file exists."""
        base_path = Path(__file__).parent.parent.parent / "dify_oapi" / "api" / "completion"
        assert (base_path / "service.py").exists(), "service.py should exist"

    def test_version_file_exists(self):
        """Test that the version.py file exists."""
        base_path = Path(__file__).parent.parent.parent / "dify_oapi" / "api" / "completion" / "v1"
        assert (base_path / "version.py").exists(), "version.py should exist"

    def test_module_imports_work(self):
        """Test that module imports work correctly."""
        # Test completion service import
        from dify_oapi.api.completion.service import CompletionService

        assert CompletionService is not None, "CompletionService should be importable"

        # Test v1 version import
        from dify_oapi.api.completion.v1.version import V1

        assert V1 is not None, "V1 should be importable"

    def test_resource_files_exist(self):
        """Test that all resource files exist."""
        base_path = Path(__file__).parent.parent.parent / "dify_oapi" / "api" / "completion" / "v1" / "resource"

        # Check resource files
        resource_files = [
            "completion.py",
            "file.py",
            "feedback.py",
            "audio.py",
            "info.py",
            "annotation.py",
        ]

        for resource_file in resource_files:
            assert (base_path / resource_file).exists(), f"{resource_file} should exist"

    def test_model_directories_exist(self):
        """Test that all model directories exist."""
        base_path = Path(__file__).parent.parent.parent / "dify_oapi" / "api" / "completion" / "v1" / "model"

        # Check model directories
        model_dirs = [
            "completion",
            "file",
            "feedback",
            "audio",
            "info",
            "annotation",
        ]

        for model_dir in model_dirs:
            assert (base_path / model_dir).exists(), f"{model_dir} directory should exist"

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
        assert (base_path / "__init__.py").exists(), "completion test __init__.py should exist"
        assert (base_path / "v1" / "__init__.py").exists(), "v1 test __init__.py should exist"

    def test_resource_imports_work(self):
        """Test that all resource imports work correctly."""
        from dify_oapi.api.completion.v1.resource.annotation import Annotation
        from dify_oapi.api.completion.v1.resource.audio import Audio
        from dify_oapi.api.completion.v1.resource.completion import Completion
        from dify_oapi.api.completion.v1.resource.feedback import Feedback
        from dify_oapi.api.completion.v1.resource.file import File
        from dify_oapi.api.completion.v1.resource.info import Info

        # Verify imports are successful
        assert Completion is not None, "Completion resource should be importable"
        assert File is not None, "File resource should be importable"
        assert Feedback is not None, "Feedback resource should be importable"
        assert Audio is not None, "Audio resource should be importable"
        assert Info is not None, "Info resource should be importable"
        assert Annotation is not None, "Annotation resource should be importable"
