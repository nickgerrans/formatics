import sys
from pathlib import Path

import pytest

# Ensure the reference form_ directory is importable when running tests from repo root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
FORM_REF_DIR = PROJECT_ROOT / "_ref" / "form_"
sys.path.insert(0, str(FORM_REF_DIR))

from formatic_mark import (  # noqa: E402  - imported after sys.path tweak
    Closure,
    Orbit,
    Slot,
    collapsed_form,
    demonstrate_python_mark,
    expanded_form,
    formatic_mark_equality,
)


def test_formatic_mark_equality_matches_expanded_and_collapsed_forms():
    orbit = Orbit([Slot(1), Slot(2), Slot(3)])

    def closure_fn(o: Orbit[Slot[int]]) -> Slot[int]:
        # choose first filled slot as canonical representative
        return o.members[0]

    left = expanded_form(orbit, closure_fn)
    right = collapsed_form(closure_fn(orbit))

    assert formatic_mark_equality(orbit, closure_fn) is True
    assert left.canonical == right.canonical


def test_closure_collapse_returns_canonical_value():
    closure = Closure("canonical")

    assert closure.collapse() == "canonical"


@pytest.mark.parametrize(
    "value, expected",
    [
        (42, "int: 42"),
        ("hi", "str: hi"),
        ([1, 2], "terminal"),
    ],
)
def test_demonstrate_python_mark_matches_expected_outcomes(value, expected):
    assert demonstrate_python_mark(value) == expected
