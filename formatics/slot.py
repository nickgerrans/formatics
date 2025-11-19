"""
Formatics slot: Positional anchors for elements in structural space.

Slots define where elements fit within the Formatics framework.

Theory Reference: theory/AXIOMS.md#axiom-1-existence-of-slots
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .exceptions import InvalidSlotPositionError, SlotEmptyError, SlotOccupiedError


@dataclass
class Slot:
    """
    A structural position for element placement.

    Implements Axiom 1: Existence of Slots
    - Slots are distinguishable by position or label
    - A slot may be filled or empty
    - Slots have no intrinsic semantic meaning beyond "place for a value"

    Soundness Property (Slot Identity):
        slot.fill(x); slot.empty() == x  (identity preservation)

    Raises:
        InvalidSlotPositionError: If position is invalid
        SlotOccupiedError: If filling an already-occupied slot
        SlotEmptyError: If emptying an already-empty slot
    """

    position: int
    element: Any | None = None
    label: str | None = None

    def __post_init__(self) -> None:
        """Validate slot position on creation."""
        if not isinstance(self.position, int):
            raise InvalidSlotPositionError(
                self.position, "position must be an integer"
            )
        if self.position < 0:
            raise InvalidSlotPositionError(
                self.position, "position must be non-negative"
            )

    def fill(self, element: Any, *, allow_overwrite: bool = False) -> None:
        """
        Place an element in this slot.

        Args:
            element: The value to place in the slot
            allow_overwrite: If True, allow overwriting existing value

        Raises:
            SlotOccupiedError: If slot is already filled and allow_overwrite=False
        """
        if self.is_filled() and not allow_overwrite:
            raise SlotOccupiedError(self.position, self.element)
        self.element = element

    def empty(self) -> Any:
        """
        Remove and return the element from this slot.

        Returns:
            The element that was in the slot

        Raises:
            SlotEmptyError: If slot is already empty
        """
        if not self.is_filled():
            raise SlotEmptyError(self.position)
        elem = self.element
        self.element = None
        return elem

    def peek(self) -> Any:
        """
        View the element without removing it.

        Returns:
            The element in the slot

        Raises:
            SlotEmptyError: If slot is empty
        """
        if not self.is_filled():
            raise SlotEmptyError(self.position)
        return self.element

    def is_filled(self) -> bool:
        """Check if slot contains an element."""
        return self.element is not None

    def clear(self) -> None:
        """Clear the slot without raising an error if already empty."""
        self.element = None

    def __repr__(self) -> str:
        status = f"filled with {self.element!r}" if self.is_filled() else "empty"
        label_str = f", label={self.label!r}" if self.label else ""
        return f"Slot(pos={self.position}, {status}{label_str})"
