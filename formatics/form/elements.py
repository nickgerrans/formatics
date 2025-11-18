"""
Formatics form elements: Fundamental structural units.

Defines the base Element class and FormElement composition.
"""

from typing import Any, Optional, Dict
from dataclasses import dataclass, field


@dataclass
class Element:
    """Base element in Formatics theory."""

    value: Any
    metadata: Dict[str, Any] = field(default_factory=dict)

    def transform(self, func) -> "Element":
        """Apply transformation to element value."""
        return Element(value=func(self.value), metadata=self.metadata.copy())

    def __repr__(self) -> str:
        return f"Element({self.value})"


@dataclass
class FormElement:
    """Composite element with structural form."""

    elements: list[Element] = field(default_factory=list)
    form_type: Optional[str] = None

    def add(self, element: Element) -> None:
        """Add element to form."""
        self.elements.append(element)

    def compose(self) -> Any:
        """Compose elements into unified structure."""
        return [e.value for e in self.elements]

    def __repr__(self) -> str:
        return f"FormElement(type={self.form_type}, count={len(self.elements)})"
