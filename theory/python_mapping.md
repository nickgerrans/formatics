# Python Pattern Matching and the Formatic Mark

## The Three Operators in Python

Python's structural pattern matching (PEP 634) provides a **runtime manifestation** of the Formatic mark through three keywords:

| Formatics | Python | Role | Example |
|-----------|--------|------|---------|
| `()` | `case <pattern>:` | **Slot** | `case Point(x, y):` — local slot waiting for match |
| `[]` | `match <expr>:` | **Orbit selector** | `match value:` — selects which equivalence class |
| `(())` | `_` | **Terminal closure** | `case _:` — wildcard catches all remaining cases |

## The Mark in Runtime Semantics

### Explicit Expansion: `([()])`

```python
match value:           # [] - orbit selection
    case Pattern1():   # () - slot
    case Pattern2():   # () - slot
    case _:            # (()) - terminal closure
```

The structure `([()])` is the **full expansion**:
- Outer `(•)`: The match block scope
- Middle `[•]`: The orbit selection via `match`
- Inner `()`: Individual case slots

### Collapsed Form: `(())`

The wildcard `_` is the **collapsed canonical form**:

```python
case _:  # Equivalent to (())
```

This is the terminal pattern that:
- Ignores all internal structure
- Treats all remaining orbits as equivalent
- Returns a single universal closure

## The Runtime Formatic Mark

Python **enforces** the equation:

```
([()]) = (())
```

Through the semantic rule:

```python
# These are equivalent:
match x:
    case A(): ...
    case B(): ...
    case _: result    # Terminal closure

# Equals:
result  # Direct collapse (if all cases lead here)
```

**Proof**: The wildcard `_` must behave identically whether:
1. You explicitly enumerate all case patterns (expanded orbit structure)
2. You immediately collapse to the terminal (direct closure)

## Why Wildcards Are Necessary

This reveals why `_` exists in **every** pattern matching language:

**It is not a convenience—it is the categorical terminal object.**

Without `_`, you cannot express:
- Universal closure
- The collapsed form of orbit structure
- The canonical representative of "all remaining cases"

## Languages Exhibiting This Mark

All structural pattern matching systems contain the mark:

| Language | Slot | Orbit | Closure |
|----------|------|-------|---------|
| Python | `case pattern` | `match` | `_` |
| Rust | `Pattern =>` | `match` | `_` |
| Haskell | Pattern guards | `case` | `_` or `otherwise` |
| Scala | `case` | `match` | `case _` |
| OCaml | Pattern | `match` | `_` |

**Universal structure**: Every pattern matching construct must implement slot/orbit/closure trinity.

This is the Formatic mark appearing cross-linguistically.
