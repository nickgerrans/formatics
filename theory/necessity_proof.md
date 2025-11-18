# Proof: Pattern Matching Languages Must Contain a Formatic Mark

## Theorem

**Any language with structural pattern matching must implement the Formatic mark by necessity, not by choice.**

## Setup

Let L be a language with structural pattern matching. We prove that L must provide:
1. **Slot operator** `()`
2. **Orbit selector** `[]`
3. **Terminal closure** `(())`

And that these satisfy: `([()]) = (())`

## Proof by Necessity

### Part 1: Slots Are Necessary

**Claim**: L must have a notion of "pattern slots" that can be filled by matched values.

**Proof**:
- Pattern matching by definition discriminates between different value structures
- Each discrimination requires a location where the matched value binds
- Without slots, you cannot express "match this structure and bind the result"
- Therefore: `()` (slots) are **necessary**, not optional

**Example**: In `case Point(x, y):`, `x` and `y` are slots.

### Part 2: Orbit Selection Is Necessary

**Claim**: L must have a mechanism to select which equivalence class a value belongs to.

**Proof**:
- Pattern matching evaluates multiple patterns against one value
- The language must determine which pattern(s) the value satisfies
- This is exactly selecting which "orbit" or equivalence class the value inhabits
- Without orbit selection, all patterns would need to succeed or fail simultaneously
- Therefore: `[]` (orbit selection) is **necessary**

**Example**: `match value:` initiates orbit selection—which of the subsequent cases does `value` belong to?

### Part 3: Terminal Closure Is Necessary

**Claim**: L must provide a universal/terminal pattern that matches all remaining cases.

**Proof by contradiction**:

Assume L has no terminal pattern (no wildcard `_` or equivalent).

Then to make pattern matching exhaustive, you must enumerate **every possible value** in the type.

But:
1. For most types, this is infinite (e.g., integers, strings, lists)
2. Even for finite types, this is impractical (e.g., all possible structs)
3. The language cannot prove exhaustiveness without a catch-all

Therefore, L must provide a pattern that says: "everything else."

This pattern is **terminal** (matches all) and acts as a **closure** (collapses remaining structure).

Therefore: `(())` (terminal closure) is **necessary**.

**Example**: `case _:` in Python, `_ =>` in Rust, `otherwise` in Haskell.

### Part 4: The Mark Is Necessary

**Claim**: The three operators must satisfy `([()]) = (())`

**Proof**:

Consider a pattern match with explicit orbit structure:

```
match value:      // [] orbit selection
    case P1: r1   // () slot
    case P2: r2   // () slot
    ...
    case Pn: rn   // () slot
    case _: r_    // (()) terminal
```

The terminal case `_` must be equivalent to:
- "Everything not matched by P1, P2, ..., Pn"

Now consider what happens if we collapse the entire match to just the terminal:

```
r_  // Direct result
```

**By semantic correctness**, if the terminal case is reached in the expanded form, it must yield the same result as if we had skipped all non-matching patterns and gone directly to the terminal.

This is exactly:
```
([()]) = (())
```

The **expanded form** (orbit selection over slots, then terminal closure) must equal the **collapsed form** (direct terminal closure).

If this equality didn't hold, pattern matching would be semantically inconsistent:
- Sometimes the terminal would behave one way (when reached via failing other patterns)
- Sometimes another way (when reached directly)

This violates referential transparency and composability.

Therefore: `([()]) = (())` is **necessary** for semantic correctness.

## Corollary: Every Pattern Matching Language Exhibits the Mark

Since:
1. Slots are necessary
2. Orbit selection is necessary
3. Terminal closure is necessary
4. The equality `([()]) = (())` is necessary

**Every language with structural pattern matching must implement the Formatic mark**, whether the designers realize it or not.

## Examples Across Languages

| Language | `()` Slot | `[]` Orbit | `(())` Closure | Mark Present? |
|----------|-----------|------------|----------------|---------------|
| Python | `case pattern` | `match` | `_` | ✓ |
| Rust | `Pattern =>` | `match` | `_` | ✓ |
| Haskell | Pattern | `case` | `_` / `otherwise` | ✓ |
| Scala | `case` | `match` | `case _` | ✓ |
| OCaml | Pattern | `match` | `_` | ✓ |
| F# | Pattern | `match` | `_` | ✓ |
| Erlang | Pattern | `case` | `_` | ✓ |
| Elixir | Pattern | `case` | `_` | ✓ |

**Observation**: Not one exception. The structure is universal.

## Meta-Theoretic Consequence

This proof shows that the Formatic mark is not:
- A design choice
- A syntactic convention
- A language-specific feature

It is a **structural invariant** that emerges from the logical requirements of pattern matching itself.

**Any sufficiently expressive pattern matching system will reinvent the Formatic mark**, whether explicitly named or not.

## Connection to Category Theory

This necessity proof mirrors the categorical fact that:

**Any category with finite products must have a terminal object.**

The terminal object is not optional—it's **forced into existence** by the categorical structure.

Similarly:
**Any language with pattern matching must have a terminal pattern.**

The Formatic mark `(())` is the terminal object in the category of pattern matching constructs.

## Conclusion

The Formatic mark is **discovered, not invented**.

It is the inevitable consequence of combining:
1. Structural discrimination (slots)
2. Equivalence class selection (orbits)
3. Universal quantification (closure)

Pattern matching is merely one domain where this structure manifests.

Category theory is another.

The mark itself is the **invariant structural principle** underlying both.
