"""
Formatics filestate: Track element origin and transformation history.

This module provides core file state tracking within the Formatics framework,
ensuring every element maintains its lineage and transformation path.
"""

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional


class FileState:
    """Track the state and origin of a file element."""

    def __init__(self, path: Path, origin: Optional[Path] = None):
        """
        Initialize FileState.

        Args:
            path: Current file path
            origin: Original file path (if moved/transformed)
        """
        self.path = Path(path)
        self.origin = Path(origin) if origin else self.path
        self.created_at = datetime.now()
        self.metadata: Dict[str, Any] = {}

    def track_move(self, new_path: Path) -> "FileState":
        """Record a file movement, preserving origin."""
        return FileState(path=new_path, origin=self.origin)

    def get_lineage(self) -> tuple[Path, Path]:
        """Return (origin, current) path tuple."""
        return (self.origin, self.path)

    def __repr__(self) -> str:
        return f"FileState(path={self.path}, origin={self.origin})"
