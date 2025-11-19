"""
Example: Slot and Orbit with Error Handling

Demonstrates the core Slot and Orbit classes with proper error handling,
showcasing the "minimal maximal form" principle - maximum robustness with
minimal complexity.

Theory Reference: theory/AXIOMS.md - Axioms 1 & 2
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from formatics.exceptions import EmptyOrbitError, SlotEmptyError, SlotOccupiedError
from formatics.orbit import Orbit
from formatics.slot import Slot


def demonstrate_slots():
    """Demonstrate Slot functionality with error handling."""
    print("=" * 60)
    print("SLOT DEMONSTRATION")
    print("=" * 60)

    # Creating valid slots
    slot1 = Slot(position=0, label="first")
    slot2 = Slot(position=1, label="second")
    print(f"\nCreated: {slot1}")
    print(f"Created: {slot2}")

    # Filling slots
    slot1.fill("Hello, Formatics!")
    print(f"\nAfter fill: {slot1}")
    print(f"Is filled: {slot1.is_filled()}")

    # Peeking at value
    value = slot1.peek()
    print(f"Peeked value: {value!r}")
    print(f"Slot still has value: {slot1.is_filled()}")

    # Emptying slot (identity preservation)
    retrieved = slot1.empty()
    print(f"\nRetrieved: {retrieved!r}")
    print(f"After empty: {slot1}")

    # Error handling: trying to empty an already-empty slot
    print("\n--- Error Handling ---")
    try:
        slot1.empty()
    except SlotEmptyError as e:
        print(f"✓ Caught expected error: {e}")

    # Error handling: trying to fill an occupied slot
    slot2.fill("occupied")
    try:
        slot2.fill("trying to overwrite")
    except SlotOccupiedError as e:
        print(f"✓ Caught expected error: {e}")

    # Overwriting with explicit permission
    slot2.fill("new value", allow_overwrite=True)
    print(f"After overwrite: {slot2}")

    # Safe clearing
    slot2.clear()
    slot2.clear()  # Safe to call multiple times
    print(f"After clear: {slot2}")


def demonstrate_orbits():
    """Demonstrate Orbit functionality with error handling."""
    print("\n" + "=" * 60)
    print("ORBIT DEMONSTRATION")
    print("=" * 60)

    # Creating valid orbit
    element = "data_point"
    states = ["initial", "processing", "validated", "final"]
    orbit = Orbit(element=element, states=states)
    print(f"\nCreated: {orbit}")

    # Advancing through states
    print("\n--- Advancing through orbit ---")
    while not orbit.at_end():
        next_state = orbit.advance()
        print(f"Advanced to: {next_state} -> {orbit}")

    # Attempting to advance past end
    result = orbit.advance()
    print(f"Advance at end returns: {result}")

    # Resetting orbit
    orbit.reset()
    print(f"After reset: {orbit}")

    # Jumping to specific state
    orbit.jump_to("validated")
    print(f"After jump to 'validated': {orbit}")

    # Error handling: jumping to non-existent state
    print("\n--- Error Handling ---")
    try:
        orbit.jump_to("nonexistent")
    except ValueError as e:
        print(f"✓ Caught expected error: {e}")

    # Error handling: empty orbit
    try:
        Orbit(element="test", states=[])
    except EmptyOrbitError as e:
        print(f"✓ Caught expected error: {e}")


def demonstrate_theory_connection():
    """Demonstrate connection to formal theory."""
    print("\n" + "=" * 60)
    print("THEORY CONNECTION")
    print("=" * 60)

    print("\nAxiom 1 (Slots):")
    print("- Slots are distinguishable (position/label)")
    print("- Slots preserve identity (fill -> empty)")
    print("- Slots have no intrinsic meaning")

    s = Slot(position=42, label="demo")
    s.fill("value")
    assert s.empty() == "value"
    print("✓ Identity preservation verified")

    print("\nAxiom 2 (Orbits):")
    print("- Orbits group equivalent elements")
    print("- Orbit selection determines equivalence class")
    print("- Elements traverse orbit states")

    o = Orbit(element="x", states=["A", "B", "C"])
    print(f"Initial state: {o.current_state()}")
    o.advance()
    print(f"After advance: {o.current_state()}")
    print("✓ Orbit state transitions verified")


if __name__ == "__main__":
    demonstrate_slots()
    demonstrate_orbits()
    demonstrate_theory_connection()

    print("\n" + "=" * 60)
    print("All demonstrations complete!")
    print("See theory/AXIOMS.md for formal definitions")
    print("=" * 60)
