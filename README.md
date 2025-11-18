# Formatics: The Structural Theory of Marks

**A formal framework for structural invariants across category theory, programming languages, and universal algebra.**

## Overview

Formatics identifies and formalizes **structural marks**—fundamental patterns that appear across multiple domains not by coincidence, but by mathematical necessity. The foundational structure is the **Formatic mark**:

```
([()]) = (())
```

This deceptively simple equation encodes a deep structural truth that manifests in:
- **Category theory**: The equivalence of cores and skeletons
- **Programming languages**: The structure of pattern matching
- **Type theory**: Universal quantification and closure
- **Universal algebra**: Terminal objects and canonical forms

## The Three Operators

Every Formatic structure contains three fundamental operators:

| Symbol | Name | Role |
|--------|------|------|
| `()` | **Slot** | Local container or object waiting to be filled |
| `[]` | **Orbit/Bound** | Equivalence class selector / groupoid action |
| `(())` | **Closure** | Terminal object / universal construction |

## Key Results

### 1. Categorical Interpretation

The Formatic mark translates directly to category theory:

```
Core(C) ≅ Skel(C)
```

**Meaning**: The core (all objects with all isomorphisms) is equivalent to the skeleton (one canonical representative per isomorphism class).

### 2. Pattern Matching Structure

Every language with structural pattern matching implements the mark:

| Formatics | Python | Rust | Haskell |
|-----------|--------|------|---------|
| `()` | `case` | `Pattern =>` | Pattern |
| `[]` | `match` | `match` | `case` |
| `(())` | `_` | `_` | `_` or `otherwise` |

The wildcard `_` is not a convenience—it's the **terminal object** of the pattern category.

### 3. Necessity Theorem

**Any language with structural pattern matching must contain a Formatic mark by necessity.**

This is not a design choice but a logical requirement for semantic correctness.

## Repository Structure (by prefix/suffix)

Use the prefix/suffix groupings as the primary navigation tool (see
[Prefix/Suffix Organization Guide](PREFIX_SUFFIX_ORGANIZATION.md) for full
details):

- `formET_corpus/`: core corpus directory containing `formET_0a/1a/2a`,
  `formET_A1/B1/C1`, `formET_Ba/Ca`, `formET.pdf`, and `formET.ods`.
- `_ref/form_/formatic_mark.{md,py}` with paired tests in
  `tests/test_formatic_mark.py`.
- `theory/*`: conceptual proofs and mappings (`categorical_interpretation.md`,
  `necessity_proof.md`, `python_mapping.md`, `index.md`).
- `filestate.py` with its mirror test `tests/test_filestate.py`.
- `tools/prefix_suffix_index.py`: CLI for generating live prefix/suffix views.
- Reference docs: `FORMATICS_AGENT_PROTOCOL.md`, `CONTRIBUTING-AGENT.md`,
  `QUICK_REFERENCE.md`, `README.md`.

## Quick Start

Run the demonstration:

```bash
python3 _ref/form_/formatic_mark.py
```

This verifies:
1. The categorical interpretation (Core ≅ Skel)
2. Python pattern matching structure
3. The mark equality `([()]) = (())`

## Directory prefixes and suffixes

Use `tools/prefix_suffix_index.py` to view every file and folder grouped by the
alphabetic prefixes and suffixes in their names, ignoring file extensions:

```bash
python3 tools/prefix_suffix_index.py            # scan from the repository root
python3 tools/prefix_suffix_index.py tests      # scan a specific subdirectory
python3 tools/prefix_suffix_index.py --include-hidden
```

Each section lists entries by prefix first and suffix second so you can see
clusters like `formET_*` or `_ref/*` together even when they have different
extensions.

## Folder leap tracking (`filestate.py`)

Use `filestate.py` as a single backbone module to detect when a script is run
from a different directory than the one where it was last executed:

1. Place `filestate.py` in your project root.
2. In any script that should track folder moves, add:

   ```python
   from filestate import folderleap
   ```

On import, `filestate` records the script's current directory using a
`# ORIGIN:` tag inserted into the file itself. If the script later runs from a
different folder, `filestate` prints the move, re-runs the script once by
default, and updates the embedded origin tag. Set `FILESTATE_DISABLE_TRIGGER=1`
to skip the automatic re-run (helpful in automated tests) or
`FILESTATE_DISABLE_AUTO_PRIME=1` to disable all automatic behavior.

## Testing

Run the automated checks with `pytest`:

```bash
pytest
```

## Core Claims

1. **Discovery, not invention**: The Formatic mark is not designed but discovered as a consequence of structural requirements

2. **Cross-domain invariance**: The same pattern appears in category theory, programming languages, and algebra because they share underlying structure

3. **Necessity**: Systems with slot/orbit/closure structure **must** exhibit the mark for semantic consistency

## Reading Order

For newcomers:

1. Start with [_ref/form_/formatic_mark.md](_ref/form_/formatic_mark.md) for the basic definition
2. Read [theory/python_mapping.md](theory/python_mapping.md) to see it in familiar code
3. Explore [theory/categorical_interpretation.md](theory/categorical_interpretation.md) for the deep connection
4. Study [theory/necessity_proof.md](theory/necessity_proof.md) to understand why this is inevitable

## Applications

- **Language design**: Understand the minimal structure needed for pattern matching
- **Type theory**: Identify universal constructions automatically
- **Category theory**: Recognize core/skeleton equivalences
- **Formal verification**: Prove exhaustiveness via terminal objects
- **Compiler optimization**: Exploit the mark equality for reductions

## Status

**Active development**. This repository formalizes recent theoretical discoveries about structural invariants.

## Contributing

This is a research project exploring fundamental structures. Contributions should:
- Identify new domains exhibiting the Formatic mark
- Prove additional necessity theorems
- Implement demonstrations in other languages
- Extend the categorical framework

## License

Theory is freely available for research and education.

## Contact

For questions about the theory or implementations, open an issue.
