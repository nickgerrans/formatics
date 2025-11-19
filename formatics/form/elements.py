"""
Formatics form elements: Fundamental structural units.

Defines the base Element class and FormElement composition.

Theory Reference: theory/AXIOMS.md - Derived Principles (Theorem 1)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from ..exceptions import InvalidElementError, InvalidFormError


@dataclass
class Element:
    """
    Base element in Formatics theory.

    Elements are the fundamental units that can be placed in slots,
    transformed via orbits, and composed into forms.

    Theory Connection:
        Represents the X in the anchor relation X ~ C (Element ~ Canonical)

    Attributes:
        value: The actual data held by this element
        metadata: Additional properties (extensible)
    """

    value: Any
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate element on creation."""
        if not isinstance(self.metadata, dict):
            raise InvalidElementError(self.value, "metadata must be a dictionary")

    def transform(self, func: Callable[[Any], Any]) -> Element:
        """
        Apply transformation to element value.

        Creates a new Element with transformed value, preserving metadata.

        Args:
            func: Transformation function to apply

        Returns:
            New Element with transformed value

        Raises:
            InvalidElementError: If transformation produces invalid result
        """
        if not callable(func):
            raise InvalidElementError(
                self.value, f"transform requires callable, got {type(func).__name__}"
            )

        try:
            new_value = func(self.value)
        except Exception as e:
            raise InvalidElementError(self.value, f"transformation failed: {e}") from e

        return Element(value=new_value, metadata=self.metadata.copy())

    def with_metadata(self, **kwargs: Any) -> Element:
        """
        Create a new Element with updated metadata.

        Args:
            **kwargs: Metadata key-value pairs to add/update

        Returns:
            New Element with merged metadata
        """
        new_metadata = self.metadata.copy()
        new_metadata.update(kwargs)
        return Element(value=self.value, metadata=new_metadata)

    def __eq__(self, other: object) -> bool:
        """
        Elements are equal if values are equal (metadata not considered).

        This implements structural equality rather than identity.
        """
        if not isinstance(other, Element):
            return NotImplemented
        return bool(self.value == other.value)

    def __hash__(self) -> int:
        """Allow elements to be used in sets/dicts (based on value)."""
        try:
            return hash(self.value)
        except TypeError:
            # For unhashable values, use id
            return hash(id(self.value))

    def __repr__(self) -> str:
        if self.metadata:
            return f"Element({self.value!r}, metadata={self.metadata})"
        return f"Element({self.value!r})"


@dataclass
class FormElement:
    """
    Composite element with structural form.

    FormElements contain other elements and define compositional structure.
    This models "strata holds itself" - the form can contain forms recursively.

    Theory Connection:
        Implements strata : form ; order
        The FormElement is both a container (form) and can hold structure (order)

    Attributes:
        elements: List of constituent elements
        form_type: Optional type label for this form

    Raises:
        InvalidFormError: If form structure is invalid
    """

    elements: list[Element] = field(default_factory=list)
    form_type: str | None = None

    def __post_init__(self) -> None:
        """Validate form on creation."""
        if not isinstance(self.elements, list):
            raise InvalidFormError(f"elements must be a list, got {type(self.elements).__name__}")
        # Validate all elements
        for i, elem in enumerate(self.elements):
            if not isinstance(elem, Element):
                raise InvalidFormError(
                    f"Element at index {i} must be Element instance, got {type(elem).__name__}"
                )

    def add(self, element: Element) -> None:
        """
        Add element to form.

        Args:
            element: Element to add

        Raises:
            InvalidFormError: If element is invalid
        """
        if not isinstance(element, Element):
            raise InvalidFormError(f"Can only add Element instances, got {type(element).__name__}")
        self.elements.append(element)

    def remove(self, element: Element) -> None:
        """
        Remove element from form.

        Args:
            element: Element to remove

        Raises:
            ValueError: If element not in form
        """
        try:
            self.elements.remove(element)
        except ValueError as e:
            raise ValueError(f"Element {element!r} not found in form") from e

    def compose(self) -> list[Any]:
        """
        Compose elements into unified structure.

        Extracts values from all elements to create a simple list representation.

        Returns:
            List of element values
        """
        return [e.value for e in self.elements]

    def transform_all(self, func: Callable[[Any], Any]) -> FormElement:
        """
        Apply transformation to all elements in form.

        Args:
            func: Transformation function

        Returns:
            New FormElement with all elements transformed

        Raises:
            InvalidFormError: If transformation fails
        """
        try:
            transformed_elements = [elem.transform(func) for elem in self.elements]
        except Exception as e:
            raise InvalidFormError(f"Failed to transform form elements: {e}") from e

        return FormElement(elements=transformed_elements, form_type=self.form_type)

    def is_empty(self) -> bool:
        """Check if form has no elements."""
        return len(self.elements) == 0

    def count(self) -> int:
        """Return number of elements in form."""
        return len(self.elements)

    def __len__(self) -> int:
        """Allow len(form_element)."""
        return len(self.elements)

    def __iter__(self):
        """Allow iteration over elements."""
        return iter(self.elements)

    def __repr__(self) -> str:
        type_str = f", type={self.form_type!r}" if self.form_type else ""
        return f"FormElement(count={len(self.elements)}{type_str})"
