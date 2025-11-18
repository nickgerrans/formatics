# Formatics Theory Index

Complete guide to the theoretical foundations.

## Core Documents

### 1. [The Formatic Mark](../_ref_/form_/formatic_mark.md)
**Start here**. Defines the fundamental equation `([()]) = (())` and introduces the three operators: slot, orbit, closure.

**Key concepts**:
- What slots, orbits, and closures are
- Why the mark expresses structural equivalence
- What makes this a universal invariant

### 2. [Categorical Interpretation](categorical_interpretation.md)
Shows how the Formatic mark exists in category theory as the Core/Skeleton equivalence.

**Key concepts**:
- Translation table: Formatics → Category Theory
- The mark as `Core(C) ≅ Skel(C)`
- Universal closure as a functor
- Why every category exhibits this structure

### 3. [Python Pattern Matching](python_mapping.md)
Demonstrates the mark in Python's `match`/`case`/`_` syntax.

**Key concepts**:
- `match` = orbit selector
- `case` = slot
- `_` = terminal closure
- Runtime manifestation of the mark
- Why wildcards exist in every pattern matching language

### 4. [Necessity Proof](necessity_proof.md)
**Most important**. Proves that pattern matching languages **must** implement the Formatic mark.

**Key concepts**:
- Proof that slots are necessary
- Proof that orbit selection is necessary
- Proof that terminal closure is necessary
- Proof that the mark equality must hold for semantic correctness
- Corollary: Every pattern matching language reinvents this structure

## Implementation

### [Python Implementation](../_ref_/form_/formatic_mark.py)
Working code that demonstrates:
- The three operators as Python classes
- The mark equality as a function
- Categorical interpretation (Core/Skeleton)
- Pattern matching structure
- Verification examples

Run with:
```bash
python3 ../_ref_/form_/formatic_mark.py
```

## Reading Paths

### For programmers:
1. [Python Pattern Matching](python_mapping.md)
2. [The Formatic Mark](../_ref_/form_/formatic_mark.md)
3. [Necessity Proof](necessity_proof.md)
4. [Python Implementation](../_ref_/form_/formatic_mark.py)

### For category theorists:
1. [Categorical Interpretation](categorical_interpretation.md)
2. [The Formatic Mark](../_ref_/form_/formatic_mark.md)
3. [Necessity Proof](necessity_proof.md)

### For type theorists:
1. [The Formatic Mark](../_ref_/form_/formatic_mark.md)
2. [Necessity Proof](necessity_proof.md)
3. [Categorical Interpretation](categorical_interpretation.md)
4. [Python Pattern Matching](python_mapping.md)

## Cross-References

### The Three Operators

| Concept | Formatics | Category | Python | Document |
|---------|-----------|----------|--------|----------|
| Local container | `()` | Object | `case` | [formatic_mark.md](../_ref_/form_/formatic_mark.md) |
| Equivalence class | `[]` | Iso class | `match` | [categorical_interpretation.md](categorical_interpretation.md) |
| Universal closure | `(())` | Terminal | `_` | [python_mapping.md](python_mapping.md) |

### The Mark Across Domains

| Domain | Left: Expanded | Right: Collapsed | Document |
|--------|----------------|------------------|----------|
| Formatics | `([()]) ` | `(())` | [formatic_mark.md](../_ref_/form_/formatic_mark.md) |
| Category | `Core(C)` | `Skel(C)` | [categorical_interpretation.md](categorical_interpretation.md) |
| Python | `match: case*: _` | `_` | [python_mapping.md](python_mapping.md) |

## Future Work

Potential extensions:
- **Rust pattern matching**: Same structure with lifetime annotations
- **Dependent types**: How the mark appears in dependent pattern matching
- **Proof assistants**: Formalization in Coq/Agda/Lean
- **Algebraic structures**: Orbit-counting theorems
- **Homotopy type theory**: Univalence and the mark

## Meta-Theory

The necessity proof establishes that:

**The Formatic mark is not designed—it is inevitable.**

Any system combining:
1. Distinguishable elements (slots)
2. Equivalence relations (orbits)
3. Universal constructions (closures)

Must exhibit the mark `([()]) = (())` for logical consistency.

This makes it a **discovered mathematical truth**, not an invented notation.

## Verification Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Category theory admits the mark | ✓ Verified | Core/Skeleton equivalence |
| Python implements the mark | ✓ Verified | `match`/`case`/`_` structure |
| The mark is necessary | ✓ Proven | Necessity proof |
| Other languages exhibit mark | ✓ Observed | Rust, Haskell, OCaml, etc. |
| Implementation works | ✓ Tested | Python code runs correctly |

## Questions & Extensions

Open questions for research:
1. Does the mark appear in quantum computing? (Measurement collapse?)
2. Can we formalize this in HoTT?
3. Is there a fourth operator beyond slot/orbit/closure?
4. How does this relate to Yoneda lemma?
5. Can we build a programming language explicitly around the mark?
