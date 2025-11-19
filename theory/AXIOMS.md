# Formatics: Core Axioms and Definitions

This document contains the **minimal axiomatic foundation** for Formatics theory. All other results are derived from these axioms.

---

## Primitive Objects

### Axiom 1: Existence of Slots
A **slot** `()` is a primitive structural container capable of holding a value.

**Properties:**
- Slots are distinguishable from one another by position or label
- A slot may be filled or empty
- Slots have no intrinsic semantic meaning beyond "place for a value"

**Notation:** `()` or `Slot(n)` where `n` is a position index.

---

### Axiom 2: Existence of Orbits
An **orbit** `[•]` is an equivalence class under a structural relation.

**Properties:**
- Orbits group structurally equivalent elements
- Elements in the same orbit are interchangeable under the equivalence
- Orbit selection is the operation of determining which equivalence class an element belongs to

**Notation:** `[X]` denotes the orbit containing element `X`.

---

### Axiom 3: Existence of Terminal Closure
A **terminal closure** `(())` is a universal construction that:
- Accepts all inputs without discrimination
- Collapses internal structure to a canonical representative
- Acts as a terminal object in the categorical sense

**Properties:**
- `(())` is unique (up to isomorphism)
- For any object `X`, there exists a unique morphism `X → (())`
- `(())` has no non-trivial structure

**Notation:** `(())` or `⊤` (top element).

---

## Core Inference Rules

### Rule 1: Slot Composition
Slots can be composed into structured forms.

**Inference:**
```
() : Slot, () : Slot
─────────────────────
((), ()) : Product
```

**Meaning:** Multiple slots can form product structures (tuples, records).

---

### Rule 2: Orbit Selection
Given a value and a set of equivalence classes, orbit selection determines membership.

**Inference:**
```
X : Value, {[A], [B], ..., [N]} : OrbitSet
───────────────────────────────────────────
select_orbit(X) ∈ {[A], [B], ..., [N]}
```

**Meaning:** Every value belongs to exactly one orbit in a partition.

---

### Rule 3: Closure Absorption
Applying closure to any orbit yields the terminal closure.

**Inference:**
```
[X] : Orbit
───────────
([X]) = (())
```

**Meaning:** Closing an orbit collapses it to the universal terminal.

---

### Rule 4: The Formatic Mark (Main Theorem)
The expanded form (orbit of a slot under closure) equals the collapsed terminal closure.

**Axiom/Theorem:**
```
([()]) = (())
```

**Status:** This can be proven from Axioms 1-3 + Rules 1-3, but is fundamental enough to state axiomatically.

**Proof sketch:**
1. `()` is a slot (Axiom 1)
2. `[()]` forms an orbit around the slot (Axiom 2)
3. `([•])` applies terminal closure to orbits (Axiom 3 + Rule 3)
4. By Rule 3: `([()]) = (())`

---

## Derived Principles

### Theorem 1: Slot Holds Strata
**Statement:** In Element Theory, the slot operator `()` models the fact that strata holds itself.

**Formalization:**
```
strata : form ; order
strata ! structure
```

Where `!` denotes the "holds" relation.

**Connection to Axiom 1:** The slot `()` is the structural realization of the self-holding property.

---

### Theorem 2: Orbit Equivalence (X ~ C)
**Statement:** Elements are anchored to equivalence classes via the orbit relation.

**Formalization:**
```
X ~ C
```

Means: Element `X` belongs to the orbit characterized by canonical form `C`.

**Connection to Axiom 2:** `~` is the orbit membership relation.

---

### Theorem 3: Terminal Universality
**Statement:** The terminal closure `(())` is the unique object satisfying:

```
∀X : ∃! f : X → (())
```

**Connection to Axiom 3:** This is the categorical definition of terminal object.

---

### Theorem 4: Necessity of Pattern Matching Structure
**Statement:** Any language with structural pattern matching must implement:
1. Slot operator (case patterns)
2. Orbit selector (match statement)
3. Terminal closure (wildcard `_`)

And these must satisfy the Formatic mark: `([()]) = (())`

**Proof:** See [necessity_proof.md](necessity_proof.md)

---

### Theorem 5: Core-Skeleton Equivalence
**Statement:** In category theory, the Formatic mark manifests as:

```
Core(C) ≅ Skel(C)
```

**Proof:** See [categorical_interpretation.md](categorical_interpretation.md)

---

## Soundness Conditions

For a system to correctly implement Formatics, it must satisfy:

### Soundness 1: Slot Identity
Slots are identity-preserving under fill/empty operations.

**Property:**
```python
slot.fill(x)
assert slot.empty() == x
```

---

### Soundness 2: Orbit Partitioning
Orbits form a partition of the value space.

**Property:**
```
∀X, Y: X ∈ [A] ∧ Y ∈ [A] ⟹ X ~ Y
∀X: ∃! [A] : X ∈ [A]
```

---

### Soundness 3: Closure Idempotence
Applying closure multiple times yields the same result.

**Property:**
```
((•)) = (•) for any terminal closure
```

---

### Soundness 4: Mark Equality
The fundamental mark equality must hold.

**Property:**
```python
def verify_mark_equality(orbit, closure_fn):
    expanded = closure_fn(orbit)
    collapsed = closure_fn.canonical
    assert expanded == collapsed
```

---

## Minimality

These axioms are **minimal** in the sense that:
1. No axiom can be derived from the others
2. All Formatics theorems can be derived from these axioms
3. Removing any axiom makes certain theorems unprovable

**Note:** Axiom 3 (Terminal Closure) is sometimes derivable in categorical settings via universal properties, but we state it axiomatically for clarity in non-categorical contexts.

---

## References

- [The Formatic Mark](../_ref/form_/formatic_mark.md) - Foundational definition
- [Categorical Interpretation](categorical_interpretation.md) - Category theory realization
- [Necessity Proof](necessity_proof.md) - Why pattern matching requires this structure
- [Python Mapping](python_mapping.md) - Concrete implementation

---

**Copyright (c) 2025 Nicholas Gerrans. All rights reserved.**
