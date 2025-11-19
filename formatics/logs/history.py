"""
Formatics history: Comprehensive transformation logging.

Records and retrieves element transformation history.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, List


@dataclass
class HistoryEntry:
    """Single entry in transformation history."""

    timestamp: datetime
    action: str
    element: Any
    metadata: dict = field(default_factory=dict)

    def __repr__(self) -> str:
        return f"HistoryEntry({self.action} at {self.timestamp.isoformat()})"


class History:
    """Maintains transformation history log."""

    def __init__(self):
        """Initialize empty history."""
        self.entries: List[HistoryEntry] = []

    def record(self, action: str, element: Any, **metadata) -> None:
        """Record a transformation event."""
        entry = HistoryEntry(
            timestamp=datetime.now(), action=action, element=element, metadata=metadata
        )
        self.entries.append(entry)

    def get_recent(self, n: int = 10) -> List[HistoryEntry]:
        """Get n most recent entries."""
        return self.entries[-n:]

    def filter_by_action(self, action: str) -> List[HistoryEntry]:
        """Get all entries matching action type."""
        return [e for e in self.entries if e.action == action]

    def clear(self) -> None:
        """Clear all history."""
        self.entries.clear()

    def __len__(self) -> int:
        return len(self.entries)

    def __repr__(self) -> str:
        return f"History(entries={len(self.entries)})"
