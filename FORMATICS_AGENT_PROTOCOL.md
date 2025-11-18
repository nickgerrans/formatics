# Formatics Agent Protocol

Any AI agent assisting with this repo MUST assume:

- It cannot see the repo; it only sees what is pasted into the prompt.
- It must not invent non-existent modules or paths.
- It must treat code edits as small transforms of visible files.

## Core rules:

### 1. Filestate/folderleap
- `filestate.py` owns file-origin and folder-leap logic.
- Import pattern: `from filestate import folderleap`.
- Side effects on import must be explicit and documented.

### 2. Formatics core
- Math and Element Theory live in `form_*.py` or clearly named modules.
- Represent theories (X ~ C, strata ! structure, etc.) as explicit classes/functions.
- Avoid hidden I/O or global state changes in theory modules.

### 3. Edits
- Only modify what is provided.
- Prefer additive changes and minimal diffs.
- Don't refactor broadly unless explicitly asked.

### 4. Naming conventions
- `form_*.py` → Formatic semantics modules
- `filestate.py` → file-origin + folderleap scaffolding
- `element_theory.py` → X ~ C / strata ! structure logic
- `prefix_logic.py` → un / null / set-theory parallels

### 5. Style constraints
- No global container hijacking (use explicit classes: `FormList`, `Strata`, etc.)
- Pure functions for math/theory modules
- Side-effect modules (filestate, folderleap) must be clearly documented

### 6. Testing
- Use `tests/` directory
- Prefer `unittest` or `pytest`
- Simple, declarative tests with clear theory-to-code mappings

---

See `CONTRIBUTING-AGENT.md` for full details.
