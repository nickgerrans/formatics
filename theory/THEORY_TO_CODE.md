# Theory-to-Code Mapping

This document provides **explicit traceability** from Formatics theoretical concepts to their implementations in code.

---

## Core Concepts Mapping

### 1. Slot Operator `()`

**Theory:** [AXIOMS.md](AXIOMS.md#axiom-1-existence-of-slots)

**Implementation:** `formatics/slot.py:12-36`

```python
@dataclass
class Slot:
    """A structural position for element placement."""
    position: int
    element: Optional[Any] = None
    label: Optional[str] = None
```

**Key Properties:**
- `fill(element)` - Places value in slot
- `empty()` - Removes value from slot
- `is_filled()` - Checks occupancy

**Soundness Check:** `tests/test_formatic_mark.py` (implicit in pattern matching tests)

**Invariant:**
```python
slot = Slot(position=0)
slot.fill(x)
assert slot.empty() == x  # Identity preservation
```

---

### 2. Orbit Selector `[]`

**Theory:** [AXIOMS.md](AXIOMS.md#axiom-2-existence-of-orbits)

**Implementation:** `formatics/orbit.py:12-36`

```python
@dataclass
class Orbit:
    """Represents an element's orbital path through transformations."""
    element: Any
    states: List[str]
    current_index: int = 0
```

**Key Properties:**
- `advance()` - Move to next equivalence state
- `current_state()` - Get current orbit position
- `reset()` - Return to initial state

**Soundness Check:** `tests/test_formatic_mark.py:26-37`

**Invariant:**
```python
# Orbits partition the value space
orbit1 = Orbit(element=x, states=["A", "B"])
orbit2 = Orbit(element=y, states=["A", "B"])
# Elements in same orbit are equivalent under transformation
```

---

### 3. Terminal Closure `(())`

**Theory:** [AXIOMS.md](AXIOMS.md#axiom-3-existence-of-terminal-closure)

**Implementation:** `_ref/form_/formatic_mark.py:Closure`

```python
@dataclass
class Closure:
    """Terminal closure - universal construction."""
    canonical: T

    def collapse(self) -> T:
        """Collapse to canonical representative."""
        return self.canonical
```

**Key Properties:**
- Accepts any input (universal)
- Returns canonical representative
- Idempotent: `collapse(collapse(x)) == collapse(x)`

**Soundness Check:** `tests/test_formatic_mark.py:40-43`

**Invariant:**
```python
closure = Closure("canonical")
assert closure.collapse() == "canonical"
```

---

### 4. Element & Anchor (X ~ C)

**Theory:** [AXIOMS.md](AXIOMS.md#theorem-2-orbit-equivalence-x--c)

**Implementation:**
- `formatics/form/elements.py:12-24` - Element
- `formatics/form/anchor.py` - Anchor relation

```python
@dataclass
class Element:
    """Base element in Formatics theory."""
    value: Any
    metadata: Dict[str, Any] = field(default_factory=dict)
```

**Anchor Relation:**
```python
# X ~ C means: Element X is anchored to canonical form C
# This relation is implemented via orbit membership
```

**Soundness Check:** Tests verify element transformations preserve structural relationships

---

### 5. Strata Holding Structure (strata ! structure)

**Theory:** "Strata holds itself" - the self-referential foundation

**Implementation:** Implicit in Element composition

```python
@dataclass
class FormElement:
    """Composite element with structural form."""
    elements: list[Element] = field(default_factory=list)
    form_type: Optional[str] = None
```

**Interpretation:**
- `FormElement` contains `elements` (holds structure)
- A `FormElement` can contain itself via recursion
- This models `strata : form ; order` holding `structure`

---

## Theorems to Implementation

### Theorem: The Formatic Mark `([()]) = (())`

**Theory:** [AXIOMS.md](AXIOMS.md#rule-4-the-formatic-mark-main-theorem)

**Implementation:** `_ref/form_/formatic_mark.py:formatic_mark_equality`

```python
def formatic_mark_equality(orbit: Orbit[Slot[T]], closure_fn) -> bool:
    """Verify ([()]) = (()) equality."""
    left = expanded_form(orbit, closure_fn)
    right = collapsed_form(closure_fn(orbit))
    return left.canonical == right.canonical
```

**Test:** `tests/test_formatic_mark.py:26-37`

**Verification:**
```bash
pytest tests/test_formatic_mark.py::test_formatic_mark_equality_matches_expanded_and_collapsed_forms -v
```

---

### Theorem: Necessity of Pattern Matching Structure

**Theory:** [necessity_proof.md](necessity_proof.md)

**Implementation:** `_ref/form_/formatic_mark.py:demonstrate_python_mark`

```python
def demonstrate_python_mark(value: Any) -> str:
    """Show Python pattern matching implementing the mark."""
    match value:              # [] - Orbit selector
        case int(x):          # () - Slot
            return f"int: {x}"
        case str(s):          # () - Slot
            return f"str: {s}"
        case _:               # (()) - Terminal closure
            return "terminal"
```

**Test:** `tests/test_formatic_mark.py:46-55`

**Verification:** Run the demonstration to see all three operators in action.

---

### Theorem: Core-Skeleton Equivalence (Category Theory)

**Theory:** [categorical_interpretation.md](categorical_interpretation.md)

**Implementation:** Conceptual - demonstrated via mark equality

**Mapping:**
```
Core(C)  ≅  Skel(C)
  ↓           ↓
([()]) = (())
```

**Verification:** The mark equality in code proves the categorical equivalence holds in the implemented system.

---

## Module Responsibilities

### Core Theory Modules

| Module | Theory Concept | Axiom/Theorem | Line Reference |
|--------|---------------|---------------|----------------|
| `formatics/slot.py` | Slot operator `()` | Axiom 1 | Lines 12-36 |
| `formatics/orbit.py` | Orbit selector `[]` | Axiom 2 | Lines 12-36 |
| `formatics/form/elements.py` | Element & FormElement | Derived | Lines 12-43 |
| `formatics/form/anchor.py` | Anchor relation `X ~ C` | Theorem 2 | Full file |
| `_ref/form_/formatic_mark.py` | Complete mark implementation | Main Theorem | Full file |

---

### Supporting Infrastructure

| Module | Purpose | Theory Connection |
|--------|---------|-------------------|
| `formatics/paths/` | Path tracking | Supporting structure for transformations |
| `formatics/logs/` | History tracking | Monotone refinement (future) |
| `formatics/filestate.py` | Folderleap | Practical utility, not core theory |

---

## Soundness Checks in Code

### Check 1: Slot Identity Preservation
**Location:** Not explicitly tested yet - should add to test suite

**Recommended Test:**
```python
def test_slot_identity_preservation():
    slot = Slot(position=0)
    original_value = "test_value"
    slot.fill(original_value)
    retrieved = slot.empty()
    assert retrieved == original_value
    assert slot.element is None  # Slot is empty after empty()
```

---

### Check 2: Orbit Partitioning
**Location:** Implicit in orbit design

**Recommended Enhancement:**
```python
def test_orbit_partitioning():
    """Verify orbits form a proper partition."""
    # Elements in same orbit are equivalent
    # No element belongs to multiple orbits
    # Every element belongs to exactly one orbit
```

---

### Check 3: Closure Idempotence
**Location:** `tests/test_formatic_mark.py:40-43`

```python
def test_closure_collapse_returns_canonical_value():
    closure = Closure("canonical")
    assert closure.collapse() == "canonical"
```

**Enhancement Needed:** Test double-application:
```python
def test_closure_idempotence():
    closure = Closure("canonical")
    once = closure.collapse()
    twice = Closure(once).collapse()
    assert once == twice
```

---

### Check 4: Mark Equality
**Location:** `tests/test_formatic_mark.py:26-37`

```python
def test_formatic_mark_equality_matches_expanded_and_collapsed_forms():
    orbit = Orbit([Slot(1), Slot(2), Slot(3)])

    def closure_fn(o):
        return o.members[0]

    assert formatic_mark_equality(orbit, closure_fn) is True
```

**Status:** ✅ Verified by tests

---

## Missing Implementations

### 1. Explicit Invariant Checks
**What:** Runtime assertions verifying axiomatic properties

**Where:** Should be added to `formatics/form/__init__.py` or a new `formatics/invariants.py`

**Example:**
```python
def check_slot_invariant(slot: Slot, value: Any) -> None:
    """Runtime check for Axiom 1 properties."""
    slot.fill(value)
    retrieved = slot.empty()
    assert retrieved == value, f"Slot invariant violated: {retrieved} != {value}"
```

---

### 2. Proof Artifacts as Docstrings
**What:** Link each function/class docstring to its theorem

**Example:**
```python
class Slot:
    """
    Slot operator implementing Axiom 1.

    See: theory/AXIOMS.md#axiom-1-existence-of-slots

    Properties (Soundness 1):
    - Identity preservation: fill then empty returns original value
    - Position uniqueness: each slot has distinct position
    """
```

---

### 3. Automated Theorem Verification
**What:** Property-based tests using hypothesis library

**Example:**
```python
from hypothesis import given, strategies as st

@given(st.integers())
def test_slot_identity_property(value):
    """Property: ∀x: slot.fill(x).empty() == x"""
    slot = Slot(position=0)
    slot.fill(value)
    assert slot.empty() == value
```

---

## Verification Commands

### Run All Theory-Related Tests
```bash
pytest tests/test_formatic_mark.py -v
```

### Check Mark Equality Specifically
```bash
pytest tests/test_formatic_mark.py::test_formatic_mark_equality_matches_expanded_and_collapsed_forms -v
```

### Verify Closure Properties
```bash
pytest tests/test_formatic_mark.py::test_closure_collapse_returns_canonical_value -v
```

### Run Full Test Suite with Coverage
```bash
pytest tests/ --cov=formatics --cov-report=term-missing
```

---

## Theory Development Workflow

1. **Add new axiom/theorem** to `theory/AXIOMS.md` or relevant theory file
2. **Design implementation** in appropriate `formatics/` module
3. **Write soundness test** in `tests/`
4. **Update this mapping** to link theory ↔ code ↔ test
5. **Add docstring references** to theory documents
6. **Verify** with `pytest`

---

## Future Extensions

### Planned Mappings

1. **Monotone Refinement** (Axiom 5?)
   - Theory: Every proof pass refines, never contradicts
   - Implementation: `formatics/logs/history.py` (planned)

2. **Domain Boundaries** (Axiom 6?)
   - Theory: Explicit statement of what Formatics covers
   - Implementation: Type constraints and validation

3. **Homotopy Integration**
   - Theory: Connection to HoTT and univalence
   - Implementation: Future research

---

## Maintenance

**When you modify theory:**
1. Update relevant `theory/*.md` file
2. Update this mapping document
3. Modify corresponding code in `formatics/`
4. Update tests in `tests/`
5. Run full test suite
6. Update `CHANGELOG.md`

**When you modify code:**
1. Verify it doesn't violate any axiom
2. Update this mapping if it changes theory correspondence
3. Add tests for new properties
4. Update docstrings with theory references

---

**Last Updated:** 2025-01-19
**Maintained By:** Nicholas Gerrans
**Copyright (c) 2025 Nicholas Gerrans. All rights reserved.**
