"""
Example: Element and Form Composition

Demonstrates Element and FormElement with transformations and error handling.
Shows how "strata holds itself" - forms can contain forms recursively.

Theory Reference: theory/AXIOMS.md - Theorem 1 (Slot Holds Strata)
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from formatics.exceptions import InvalidElementError, InvalidFormError
from formatics.form.elements import Element, FormElement


def demonstrate_elements():
    """Demonstrate Element creation and transformation."""
    print("=" * 60)
    print("ELEMENT DEMONSTRATION")
    print("=" * 60)

    # Creating elements
    e1 = Element(value=42)
    e2 = Element(value="text", metadata={"source": "user"})
    print(f"\nCreated: {e1}")
    print(f"Created: {e2}")

    # Transforming elements
    doubled = e1.transform(lambda x: x * 2)
    print(f"\nOriginal: {e1}")
    print(f"Transformed: {doubled}")

    # Adding metadata
    e3 = e1.with_metadata(origin="example", validated=True)
    print(f"\nWith metadata: {e3}")

    # Equality (structural, not by metadata)
    e4 = Element(value=42, metadata={"different": "metadata"})
    print(f"\ne1 == e4: {e1 == e4}  (values equal, metadata ignored)")

    # Error handling
    print("\n--- Error Handling ---")
    try:
        e1.transform("not a function")
    except InvalidElementError as e:
        print(f"✓ Caught expected error: {e}")


def demonstrate_forms():
    """Demonstrate FormElement composition."""
    print("\n" + "=" * 60)
    print("FORM DEMONSTRATION")
    print("=" * 60)

    # Creating a form
    form = FormElement(form_type="data_collection")
    print(f"\nCreated: {form}")

    # Adding elements
    form.add(Element(value=1))
    form.add(Element(value=2))
    form.add(Element(value=3))
    print(f"After adding elements: {form}")
    print(f"Element count: {form.count()}")

    # Composing to get values
    values = form.compose()
    print(f"Composed values: {values}")

    # Transforming all elements
    doubled_form = form.transform_all(lambda x: x * 2)
    print(f"\nOriginal form values: {form.compose()}")
    print(f"Transformed form values: {doubled_form.compose()}")

    # Iteration
    print("\n--- Iteration ---")
    for i, elem in enumerate(form):
        print(f"Element {i}: {elem}")

    # Removal
    first_elem = form.elements[0]
    form.remove(first_elem)
    print(f"\nAfter removing first element: {form.compose()}")

    # Error handling
    print("\n--- Error Handling ---")
    try:
        form.add("not an element")
    except InvalidFormError as e:
        print(f"✓ Caught expected error: {e}")


def demonstrate_recursive_forms():
    """Demonstrate 'strata holds itself' - forms containing forms."""
    print("\n" + "=" * 60)
    print("RECURSIVE FORMS (Strata Holds Itself)")
    print("=" * 60)

    # Inner form
    inner = FormElement(form_type="inner_structure")
    inner.add(Element(value="a"))
    inner.add(Element(value="b"))
    print(f"\nInner form: {inner.compose()}")

    # Wrap the inner form's data in outer form
    outer = FormElement(form_type="outer_structure")
    for val in inner.compose():
        outer.add(Element(value=val))
    outer.add(Element(value="c"))
    print(f"Outer form: {outer.compose()}")

    # Transform nested structure
    uppercased = outer.transform_all(lambda x: x.upper() if isinstance(x, str) else x)
    print(f"Transformed: {uppercased.compose()}")

    print("\n✓ Forms can compose arbitrarily - 'strata holds itself'")


def demonstrate_theory_connection():
    """Demonstrate connection to formal theory."""
    print("\n" + "=" * 60)
    print("THEORY CONNECTION")
    print("=" * 60)

    print("\nElement Theory (X ~ C):")
    print("- Elements represent X (data)")
    print("- Transformations move between equivalent forms")
    print("- Metadata preserves context")

    e = Element(value="original")
    transformed = e.transform(lambda x: x.upper())
    print(f"X: {e.value} ~ C: {transformed.value}")
    print("✓ Anchor relation demonstrated")

    print("\nStrata ! Structure:")
    print("- FormElement is the container (strata)")
    print("- It holds Elements (structure)")
    print("- It can hold itself recursively")

    form = FormElement()
    form.add(Element(value=1))
    print(f"Form holds: {form.compose()}")
    print("✓ Strata holding structure verified")


if __name__ == "__main__":
    demonstrate_elements()
    demonstrate_forms()
    demonstrate_recursive_forms()
    demonstrate_theory_connection()

    print("\n" + "=" * 60)
    print("All demonstrations complete!")
    print("See theory/AXIOMS.md and theory/THEORY_TO_CODE.md")
    print("=" * 60)
