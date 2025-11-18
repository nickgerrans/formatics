# Formatic Mark Quick Reference

## The Fundamental Equation

```
([()]) = (())
```

## The Three Operators

| Symbol | Name | Meaning | Category Theory | Python |
|--------|------|---------|-----------------|--------|
| `()` | **Slot** | Empty container | Object | `case pattern:` |
| `[]` | **Orbit** | Equivalence class | Isomorphism class | `match value:` |
| `(())` | **Closure** | Terminal universal | Terminal object | `_` wildcard |

## What the Mark Says

**English**: "The closure of an orbit containing a slot equals the collapsed closure."

**Category Theory**: "The core of a category is equivalent to its skeleton."
```
Core(C) ≅ Skel(C)
```

**Python**: "Exhaustively matching all patterns then hitting wildcard equals just using wildcard."
```python
match x:
    case A(): ...
    case B(): ...
    case _: result    # Terminal

# Equivalent to:
result  # If all paths lead here
```

## Why It Matters

1. **It's discovered, not designed**: Emerges necessarily from any slot/orbit/closure system
2. **It's universal**: Appears in category theory, type theory, programming languages
3. **It's mandatory**: Pattern matching languages must implement it for semantic correctness

## Quick Checks

### Does a system have a Formatic mark?

Ask three questions:
1. ✓ Does it have distinguishable slots/objects? → `()`
2. ✓ Can you form equivalence classes? → `[]`
3. ✓ Is there a universal/terminal construction? → `(())`

If all three: **Yes, the mark exists** (whether named or not)

### Examples

| Domain | Has Mark? | Evidence |
|--------|-----------|----------|
| Category theory | ✓ | Core/Skeleton equivalence |
| Python pattern matching | ✓ | `match`/`case`/`_` |
| Rust pattern matching | ✓ | `match`/`Pattern`/`_` |
| Haskell | ✓ | `case`/Pattern/`_` |
| Set theory | ✓ | Elements/equivalence classes/quotient |
| Group theory | ✓ | Elements/conjugacy classes/trivial orbit |
| Type theory | ✓ | Terms/definitional equality/unit type |

## Common Misconceptions

❌ "The wildcard `_` is just syntax sugar for unbound variables"
✓ **No**: `_` is the terminal object. It's structurally necessary, not convenient.

❌ "This only applies to functional languages"
✓ **No**: Any system with slot/orbit/closure structure exhibits the mark.

❌ "The mark is a metaphor"
✓ **No**: It's a mathematical equivalence with formal proof.

## Key Insight

**The Formatic mark is the same structure appearing in different disguises.**

When you see:
- Category theory's Core ≅ Skel
- Python's wildcard pattern `_`
- Set theory's quotient construction
- Type theory's unit type

You're seeing **the same structural invariant** in different clothing.

## Reading Time

- **5 minutes**: This document
- **15 minutes**: [_ref_/form_/formatic_mark.md](_ref_/form_/formatic_mark.md)
- **30 minutes**: [theory/python_mapping.md](theory/python_mapping.md) + [theory/categorical_interpretation.md](theory/categorical_interpretation.md)
- **1 hour**: [theory/necessity_proof.md](theory/necessity_proof.md)
- **Hands-on**: `python3 _ref_/form_/formatic_mark.py`

## Next Steps

1. Run the demo: `python3 _ref_/form_/formatic_mark.py`
2. Read [_ref_/form_/formatic_mark.md](_ref_/form_/formatic_mark.md)
3. Explore the necessity proof: [theory/necessity_proof.md](theory/necessity_proof.md)
4. Find the mark in your favorite language

## One-Sentence Summary

**The Formatic mark `([()]) = (())` is the structural invariant showing that expanded orbit structure equals collapsed canonical form—discovered (not invented) across category theory, pattern matching, and universal algebra.**
