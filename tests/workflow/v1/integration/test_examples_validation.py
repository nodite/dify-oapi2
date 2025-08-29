"""Validation tests for workflow examples."""

import ast
from pathlib import Path


class TestExamplesValidation:
    """Validation tests for all workflow examples."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.examples_dir = Path(__file__).parent.parent.parent.parent.parent / "examples" / "workflow"

    def test_run_workflow_example(self) -> None:
        """Validate run_workflow example structure."""
        example_file = self.examples_dir / "run_workflow.py"
        assert example_file.exists()

        with open(example_file) as f:
            content = f.read()

        # Check environment variable validation
        assert "API_KEY environment variable is required" in content
        assert "[Example]" in content
        assert "run_workflow_sync" in content
        assert "run_workflow_async" in content
        assert "run_workflow_streaming" in content

    def test_get_workflow_run_detail_example(self) -> None:
        """Validate get_workflow_run_detail example structure."""
        example_file = self.examples_dir / "get_workflow_run_detail.py"
        assert example_file.exists()

        with open(example_file) as f:
            content = f.read()

        assert "WORKFLOW_RUN_ID environment variable is required" in content
        assert "get_workflow_run_detail_sync" in content
        assert "get_workflow_run_detail_async" in content

    def test_stop_workflow_example(self) -> None:
        """Validate stop_workflow example structure."""
        example_file = self.examples_dir / "stop_workflow.py"
        assert example_file.exists()

        with open(example_file) as f:
            content = f.read()

        assert "TASK_ID environment variable is required" in content
        assert "[Example]" in content
        assert "stop_workflow_sync" in content
        assert "stop_workflow_async" in content

    def test_upload_file_example(self) -> None:
        """Validate upload_file example structure."""
        example_file = self.examples_dir / "upload_file.py"
        assert example_file.exists()

        with open(example_file) as f:
            content = f.read()

        assert "[Example]" in content
        assert "upload_file_sync" in content
        assert "upload_file_async" in content
        assert "BytesIO" in content

    def test_get_workflow_logs_example(self) -> None:
        """Validate get_workflow_logs example structure."""
        example_file = self.examples_dir / "get_workflow_logs.py"
        assert example_file.exists()

        with open(example_file) as f:
            content = f.read()

        assert "[Example]" in content
        assert "get_workflow_logs_sync" in content
        assert "get_workflow_logs_async" in content
        assert "get_workflow_logs_filtered" in content

    def test_get_info_example(self) -> None:
        """Validate get_info example structure."""
        example_file = self.examples_dir / "get_info.py"
        assert example_file.exists()

        with open(example_file) as f:
            content = f.read()

        assert "get_info_sync" in content
        assert "get_info_async" in content

    def test_get_parameters_example(self) -> None:
        """Validate get_parameters example structure."""
        example_file = self.examples_dir / "get_parameters.py"
        assert example_file.exists()

        with open(example_file) as f:
            content = f.read()

        assert "get_parameters_sync" in content
        assert "get_parameters_async" in content

    def test_get_site_example(self) -> None:
        """Validate get_site example structure."""
        example_file = self.examples_dir / "get_site.py"
        assert example_file.exists()

        with open(example_file) as f:
            content = f.read()

        assert "get_site_sync" in content
        assert "get_site_async" in content

    def test_all_examples_syntax_valid(self) -> None:
        """Verify all examples have valid Python syntax."""
        for example_file in self.examples_dir.glob("*.py"):
            if example_file.name == "__init__.py":
                continue

            with open(example_file) as f:
                content = f.read()

            # Parse to check syntax
            try:
                ast.parse(content)
            except SyntaxError as e:
                raise AssertionError(f"Syntax error in {example_file.name}: {e}")

    def test_environment_validation_presence(self) -> None:
        """Verify environment variable validation in all examples."""
        for example_file in self.examples_dir.glob("*.py"):
            if example_file.name in ["__init__.py", "README.md"]:
                continue

            with open(example_file) as f:
                content = f.read()

            # Check for API_KEY validation
            assert "API_KEY environment variable is required" in content, (
                f"Missing API_KEY validation in {example_file.name}"
            )

    def test_example_prefix_usage(self) -> None:
        """Verify [Example] prefix usage in test data."""
        for example_file in self.examples_dir.glob("*.py"):
            if example_file.name in ["__init__.py", "README.md"]:
                continue

            with open(example_file) as f:
                content = f.read()

            # Check for [Example] prefix in user data
            if "user(" in content:
                assert "[Example]" in content, f"Missing [Example] prefix in {example_file.name}"

    def test_sync_async_function_pairs(self) -> None:
        """Verify all examples have both sync and async versions."""
        for example_file in self.examples_dir.glob("*.py"):
            if example_file.name in ["__init__.py", "README.md"]:
                continue

            with open(example_file) as f:
                content = f.read()

            # Parse AST to find function definitions
            tree = ast.parse(content)
            functions = [
                node.name for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            ]

            # Find sync functions (not async)
            sync_functions = [f for f in functions if f.endswith("_sync")]

            # Check each sync function has async counterpart
            for sync_func in sync_functions:
                async_func = sync_func.replace("_sync", "_async")
                assert async_func in functions, (
                    f"Missing async version of {sync_func} in {example_file.name}. Found functions: {functions}"
                )

    def test_code_minimalism_compliance(self) -> None:
        """Verify examples follow code minimalism principles."""
        for example_file in self.examples_dir.glob("*.py"):
            if example_file.name in ["__init__.py", "README.md"]:
                continue

            with open(example_file) as f:
                content = f.read()

            # Check for minimal error handling
            assert "try:" in content, f"Missing error handling in {example_file.name}"
            assert "except Exception as e:" in content, f"Missing exception handling in {example_file.name}"

            # Check for concise output
            lines = content.split("\n")
            print_lines = [line for line in lines if "print(" in line and "Error:" not in line]

            # Should have minimal success messages
            assert len(print_lines) <= 10, (
                f"Too many print statements in {example_file.name} (found {len(print_lines)})"
            )
