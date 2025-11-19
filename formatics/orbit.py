"""
Formatics orbit: Element circulation and transformation cycles.

Defines how elements orbit through states and transformations.

Theory Reference: theory/AXIOMS.md#axiom-2-existence-of-orbits
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .exceptions import EmptyOrbitError, InvalidOrbitStateError


@dataclass
class Orbit:
    """
    Represents an element's orbital path through transformations.

    Implements Axiom 2: Existence of Orbits
    - Orbits group structurally equivalent elements
    - Elements in the same orbit are interchangeable under the equivalence
    - Orbit selection determines which equivalence class an element belongs to

    Soundness Property (Orbit Partitioning):
        Every value belongs to exactly one orbit in a partition

    Raises:
        EmptyOrbitError: If orbit has no states defined
        InvalidOrbitStateError: If state index is out of bounds
    """

    element: Any
    states: list[str]
    current_index: int = 0

    def __post_init__(self) -> None:
        """Validate orbit on creation."""
        if not self.states:
            raise EmptyOrbitError()
        if not 0 <= self.current_index < len(self.states):
            raise InvalidOrbitStateError(self.current_index, len(self.states) - 1)

    def advance(self) -> str | None:
        """
        Move to next state in orbit.

        Returns:
            The new state name, or None if at end of orbit

        Raises:
            EmptyOrbitError: If orbit has no states
        """
        if not self.states:
            raise EmptyOrbitError()

        if self.current_index < len(self.states) - 1:
            self.current_index += 1
            return self.states[self.current_index]
        return None

    def current_state(self) -> str:
        """
        Get current orbital state.

        Returns:
            The name of the current state

        Raises:
            EmptyOrbitError: If orbit has no states
            InvalidOrbitStateError: If current index is invalid
        """
        if not self.states:
            raise EmptyOrbitError()
        if not 0 <= self.current_index < len(self.states):
            raise InvalidOrbitStateError(self.current_index, len(self.states) - 1)
        return self.states[self.current_index]

    def reset(self) -> None:
        """Reset orbit to initial state."""
        self.current_index = 0

    def at_end(self) -> bool:
        """Check if orbit is at the final state."""
        if not self.states:
            return True
        return self.current_index >= len(self.states) - 1

    def jump_to(self, state_name: str) -> None:
        """
        Jump directly to a named state.

        Args:
            state_name: The name of the state to jump to

        Raises:
            ValueError: If state_name is not in orbit
            EmptyOrbitError: If orbit has no states
        """
        if not self.states:
            raise EmptyOrbitError()
        try:
            self.current_index = self.states.index(state_name)
        except ValueError as e:
            raise ValueError(
                f"State {state_name!r} not found in orbit. "
                f"Available states: {self.states}"
            ) from e

    def __repr__(self) -> str:
        if not self.states:
            return f"Orbit(element={self.element!r}, state=EMPTY)"
        return (
            f"Orbit(element={self.element!r}, "
            f"state={self.current_state()!r} [{self.current_index}/{len(self.states)-1}])"
        )
