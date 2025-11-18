"""
Formatics slot: Positional anchors for elements in structural space.

Slots define where elements fit within the Formatics framework.
"""

from typing import Optional, Any
from dataclasses import dataclass


@dataclass
class Slot:
    """A structural position for element placement."""

    position: int
    element: Optional[Any] = None
    label: Optional[str] = None

    def fill(self, element: Any) -> None:
        """Place an element in this slot."""
        self.element = element

    def empty(self) -> Optional[Any]:
        """Remove and return the element from this slot."""
        elem = self.element
        self.element = None
        return elem

    def is_filled(self) -> bool:
        """Check if slot contains an element."""
        return self.element is not None

    def __repr__(self) -> str:
        status = f"filled with {self.element}" if self.is_filled() else "empty"
        return f"Slot(pos={self.position}, {status})"
