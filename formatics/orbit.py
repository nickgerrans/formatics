"""
Formatics orbit: Element circulation and transformation cycles.

Defines how elements orbit through states and transformations.
"""

from typing import List, Optional, Any
from dataclasses import dataclass


@dataclass
class Orbit:
    """Represents an element's orbital path through transformations."""

    element: Any
    states: List[str]
    current_index: int = 0

    def advance(self) -> Optional[str]:
        """Move to next state in orbit."""
        if self.current_index < len(self.states) - 1:
            self.current_index += 1
            return self.states[self.current_index]
        return None

    def current_state(self) -> str:
        """Get current orbital state."""
        return self.states[self.current_index]

    def reset(self) -> None:
        """Reset orbit to initial state."""
        self.current_index = 0

    def __repr__(self) -> str:
        return f"Orbit(element={self.element}, state={self.current_state()})"
