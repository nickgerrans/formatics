"""Minimal repository standardization utility for Python projects."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List


class RepoStandardizer:
    """Standardizes a Python repository with minimal assumptions."""

    def __init__(self, repo_path: str | Path = "."):
        self.repo_path = Path(repo_path).resolve()
        self.issues: List[str] = []
        self.actions_taken: List[str] = []

    def check_and_create_gitignore(self) -> None:
        """Ensure a .gitignore file exists with Python-specific entries."""
        gitignore_path = self.repo_path / ".gitignore"

        minimal_gitignore = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
dist/
*.egg-info/
.eggs/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Testing
.pytest_cache/
.coverage
htmlcov/

# Environment
.env
.env.local
"""

        if not gitignore_path.exists():
            gitignore_path.write_text(minimal_gitignore)
            self.actions_taken.append("Created .gitignore with Python defaults")
        else:
            self.actions_taken.append(".gitignore already exists (not modified)")

    def check_and_create_readme(self) -> None:
        """Ensure a README file exists."""
        readme_files = ["README.md", "README.rst", "README.txt", "README"]
        has_readme = any((self.repo_path / name).exists() for name in readme_files)

        if not has_readme:
            readme_path = self.repo_path / "README.md"
            readme_content = """# Project Title

## Description
A Python project.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```python
# Add usage examples here
```

## License
See LICENSE file for details.
"""
            readme_path.write_text(readme_content)
            self.actions_taken.append("Created README.md template")
        else:
            self.actions_taken.append("README file already exists")

    def check_and_create_requirements(self) -> None:
        """Check for dependency management files."""
        dep_files = [
            "requirements.txt",
            "pyproject.toml",
            "setup.py",
            "Pipfile",
            "environment.yml",
        ]

        has_deps = any((self.repo_path / name).exists() for name in dep_files)

        if not has_deps:
            req_path = self.repo_path / "requirements.txt"
            req_path.write_text("# Add your project dependencies here\n")
            self.actions_taken.append("Created requirements.txt placeholder")
            self.issues.append("No dependency file found - created requirements.txt")
        else:
            self.actions_taken.append("Dependency management file exists")

    def check_license(self) -> None:
        """Check if a LICENSE file exists."""
        license_files = ["LICENSE", "LICENSE.txt", "LICENSE.md", "COPYING"]
        has_license = any((self.repo_path / name).exists() for name in license_files)

        if not has_license:
            self.issues.append("No LICENSE file found - consider adding one")
        else:
            self.actions_taken.append("LICENSE file exists")

    def check_python_files(self) -> Dict[str, object]:
        """Analyze Python files in the repository."""
        py_files = list(self.repo_path.rglob("*.py"))

        excluded_dirs = {".git", "__pycache__", "venv", "env", ".venv", "build", "dist"}
        py_files = [
            file_path
            for file_path in py_files
            if not any(excluded in file_path.parts for excluded in excluded_dirs)
        ]

        info: Dict[str, object] = {
            "total_files": len(py_files),
            "has_init": any(file_path.name == "__init__.py" for file_path in py_files),
            "has_main": any(
                file_path.name in {"__main__.py", "main.py"} for file_path in py_files
            ),
        }

        return info

    def check_testing_setup(self) -> None:
        """Check for testing infrastructure."""
        test_indicators = ["tests/", "test/", "pytest.ini", "tox.ini", ".pytest.ini"]

        has_tests = any((self.repo_path / name).exists() for name in test_indicators)

        if not has_tests:
            test_files = list(self.repo_path.rglob("test_*.py")) + list(
                self.repo_path.rglob("*_test.py")
            )
            if not test_files:
                self.issues.append("No testing setup found - consider adding tests")
        else:
            self.actions_taken.append("Testing infrastructure exists")

    def create_editorconfig(self) -> None:
        """Create a basic .editorconfig for consistency."""
        editorconfig_path = self.repo_path / ".editorconfig"

        if not editorconfig_path.exists():
            editorconfig_content = """# EditorConfig helps maintain consistent coding styles
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true

[*.py]
indent_style = space
indent_size = 4

[*.{yml,yaml,json}]
indent_style = space
indent_size = 2
"""
            editorconfig_path.write_text(editorconfig_content)
            self.actions_taken.append("Created .editorconfig")
        else:
            self.actions_taken.append(".editorconfig already exists")

    def standardize(self) -> None:
        """Run all standardization checks and actions."""
        print(f"Standardizing repository at: {self.repo_path}\n")

        self.check_and_create_gitignore()
        self.check_and_create_readme()
        self.check_and_create_requirements()
        self.check_license()

        self.create_editorconfig()

        python_info = self.check_python_files()
        self.check_testing_setup()

        print("=" * 60)
        print("STANDARDIZATION COMPLETE")
        print("=" * 60)

        print("\nActions Taken:")
        for action in self.actions_taken:
            print(f"  ✓ {action}")

        if self.issues:
            print("\nRecommendations:")
            for issue in self.issues:
                print(f"  ⚠ {issue}")

        print("\nPython Files Analysis:")
        print(f"  - Total Python files: {python_info['total_files']}")
        print(f"  - Has __init__.py: {python_info['has_init']}")
        print(f"  - Has main entry point: {python_info['has_main']}")

        print("\n" + "=" * 60)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "repo_path",
        nargs="?",
        default=".",
        type=Path,
        help="path to the repository (defaults to current directory)",
    )
    args = parser.parse_args()

    standardizer = RepoStandardizer(args.repo_path)
    standardizer.standardize()


if __name__ == "__main__":
    main()
