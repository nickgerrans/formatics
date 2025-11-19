"""
Formatics exception hierarchy.

This module defines all custom exceptions for the Formatics package,
organized by conceptual domain.

Theory Reference: theory/AXIOMS.md - Violations of axiomatic properties
"""

from __future__ import annotations


class FormaticsError(Exception):
    """Base exception for all Formatics-specific errors."""

    pass


# Slot-related errors (Axiom 1)


class SlotError(FormaticsError):
    """Base class for slot-related errors."""

    pass


class SlotOccupiedError(SlotError):
    """Raised when attempting to fill an already-occupied slot."""

    def __init__(self, position: int | str, current_value: object):
        self.position = position
        self.current_value = current_value
        super().__init__(
            f"Slot at position {position} is already occupied with {current_value!r}"
        )


class SlotEmptyError(SlotError):
    """Raised when attempting to empty or access an already-empty slot."""

    def __init__(self, position: int | str):
        self.position = position
        super().__init__(f"Slot at position {position} is already empty")


class InvalidSlotPositionError(SlotError):
    """Raised when a slot position is invalid."""

    def __init__(self, position: object, reason: str = ""):
        self.position = position
        msg = f"Invalid slot position: {position!r}"
        if reason:
            msg += f" ({reason})"
        super().__init__(msg)


# Orbit-related errors (Axiom 2)


class OrbitError(FormaticsError):
    """Base class for orbit-related errors."""

    pass


class InvalidOrbitStateError(OrbitError):
    """Raised when orbit state is invalid or out of bounds."""

    def __init__(self, current_index: int, max_index: int):
        self.current_index = current_index
        self.max_index = max_index
        super().__init__(
            f"Invalid orbit state: index {current_index} out of bounds [0, {max_index}]"
        )


class EmptyOrbitError(OrbitError):
    """Raised when attempting operations on an empty orbit."""

    def __init__(self):
        super().__init__("Cannot perform operation on empty orbit (no states defined)")


# Element and Form errors


class ElementError(FormaticsError):
    """Base class for element-related errors."""

    pass


class InvalidElementError(ElementError):
    """Raised when an element fails validation."""

    def __init__(self, value: object, reason: str):
        self.value = value
        super().__init__(f"Invalid element {value!r}: {reason}")


class InvalidFormError(FormaticsError):
    """Raised when a form structure is invalid."""

    def __init__(self, reason: str):
        super().__init__(f"Invalid form structure: {reason}")


# Anchor-related errors


class AnchorError(FormaticsError):
    """Base class for anchor-related errors (X ~ C relation)."""

    pass


class InvalidAnchorError(AnchorError):
    """Raised when anchor relation is invalid."""

    def __init__(self, x: object, c: object, reason: str):
        self.x = x
        self.c = c
        super().__init__(f"Invalid anchor {x!r} ~ {c!r}: {reason}")


# Invariant violation errors


class InvariantViolationError(FormaticsError):
    """
    Raised when a core Formatics invariant is violated.

    This indicates a serious problem - either a bug in the implementation
    or an attempt to use the library in a way that violates axiomatic properties.

    Theory Reference: theory/AXIOMS.md - Soundness Conditions
    """

    def __init__(self, invariant_name: str, details: str):
        self.invariant_name = invariant_name
        super().__init__(f"Invariant violated: {invariant_name}\nDetails: {details}")


class MarkEqualityViolationError(InvariantViolationError):
    """Raised when the Formatic mark equality ([()]) = (()) is violated."""

    def __init__(self, left_value: object, right_value: object):
        self.left_value = left_value
        self.right_value = right_value
        details = f"Expected ([()]) = (()), but got {left_value!r} ≠ {right_value!r}"
        super().__init__("Mark Equality", details)


# Theory-to-code mismatch errors


class TheoryCodeMismatchError(FormaticsError):
    """
    Raised when implementation behavior diverges from theoretical specification.

    This should never happen in correctly implemented code, but helps
    identify bugs during development.

    Theory Reference: theory/THEORY_TO_CODE.md
    """

    def __init__(self, theorem: str, expected: str, actual: str):
        self.theorem = theorem
        self.expected = expected
        self.actual = actual
        super().__init__(
            f"Theory-code mismatch for {theorem}:\n"
            f"  Expected (theory): {expected}\n"
            f"  Actual (code): {actual}"
        )
