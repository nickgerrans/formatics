"""
Formatics folderleap: Navigate structural transformations across directories.

Implements leap-aware navigation where folder moves preserve semantic context.
"""

from pathlib import Path
from typing import List

from .filestate import FileState


class FolderLeap:
    """Manage folder-level transformations and leaps."""

    def __init__(self, source: Path, target: Path):
        """
        Initialize a folder leap transformation.

        Args:
            source: Source directory path
            target: Target directory path
        """
        self.source = Path(source)
        self.target = Path(target)
        self.tracked_files: List[FileState] = []

    def apply(self, file_path: Path) -> Path:
        """
        Apply leap transformation to a file path.

        Args:
            file_path: File to transform

        Returns:
            Transformed path in target directory
        """
        relative = file_path.relative_to(self.source)
        return self.target / relative

    def track_file(self, file_state: FileState) -> None:
        """Add file to leap tracking."""
        self.tracked_files.append(file_state)

    def __repr__(self) -> str:
        return f"FolderLeap({self.source} → {self.target})"
