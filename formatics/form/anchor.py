"""
Formatics form anchors: Fixed reference points in element space.

Anchors provide stable attachment points for element relationships.
"""

from typing import Any, Optional
from dataclasses import dataclass


@dataclass
class Anchor:
    """A fixed reference point in Formatics space."""

    name: str
    position: tuple[float, float, float]
    attached_element: Optional[Any] = None

    def attach(self, element: Any) -> None:
        """Attach an element to this anchor."""
        self.attached_element = element

    def detach(self) -> Optional[Any]:
        """Detach and return the element."""
        elem = self.attached_element
        self.attached_element = None
        return elem

    def is_anchored(self) -> bool:
        """Check if anchor has attached element."""
        return self.attached_element is not None

    def __repr__(self) -> str:
        status = "anchored" if self.is_anchored() else "free"
        return f"Anchor(name={self.name}, pos={self.position}, {status})"
