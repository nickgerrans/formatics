# Contributing to Formatics: Guidelines for GPTs

This document provides explicit guidelines for AI models (GPTs) assisting with the Formatics repository. Since GPTs cannot see the repository directly, these rules ensure coherent, maintainable contributions.

---

## 0. Ground Rule: Blindfolded Editing

A GPT **does not see your repo**.
So every code change is logically:

> `new_file = transform(old_file, prompt_context)`

**Never** assume:

* directory layout (unless user states it),
* existing modules,
* or unseen code structure.

All guidance below assumes:
👉 *the user has to bring the relevant code into the chat*.

---

## 1. Protocol for Asking a GPT to Modify Code

When you (future you / other humans) use a GPT on the Formatics repo, the prompt should:

1. **Show the exact file** to be edited (full text).
2. **Say what you want** in terms of behavior or invariant:

   * "Add folderleap-style self-origin tracking"
   * "Implement X ~ C anchor check"
3. **Say the filename + logical path**:

   * `filestate.py` at repo root
   * `formatics/core/element.py`, etc.
4. **Say what MUST NOT CHANGE**:

   * "Do not change function signatures"
   * "Do not change public API names"
   * "Keep class Element stable"

This is how you compensate for "repo is invisible."

---

## 2. File & Module Naming Rules for Formatics

To keep things coherent for GPTs:

* **Core naming:**

  * `form_*.py` → Formatic semantics modules.
  * `filestate.py` → file-origin + folderleap scaffolding.
  * `folderleap.py` (optional) → specific folder-leap utilities.
* **Never repurpose**:

  * `form_` for non-Formatic logic.
  * `filestate` for arbitrary random utilities.
* **One concept per file** if possible:

  * `element_theory.py` for X ~ C / strata ! structure logic.
  * `prefix_logic.py` for `un` / `null` / set-theory parallels.

GPT rule of thumb:

> "If I'm writing Formatics semantics, they go in a `form_*.py` or a clearly named core module. Filestate/folderleap stays about *files & movement*, not math."

---

## 3. Style & Safety Constraints for GPT Code

GPTs generating Python in this repo should follow:

### 3.1. No global container hijacking

* Don't override builtins (`list`, `dict`) magic in ways that break normal expectations.
* Custom Formatics containers should be **explicit classes**:

  * `FormList`, `OrderContainer`, `Strata`, etc.

### 3.2. Pure functions where possible

* For anything math/Formatics-y, prefer **pure, testable functions**:

  ```python
  def anchor_xc(element) -> tuple[X, C]:
      ...
  ```
* Avoid hidden I/O in core theory modules.

### 3.3. Side-effect modules are clearly marked

* `filestate.py` and `folderleap.py` **are allowed** to have side effects on import, but:

  * Side effects must be **obvious and documented**.
  * No "surprise behavior" in theory modules.

---

## 4. Filestate / Folderleap Canon Rules

For any GPT touching these:

1. `filestate.py` is the **one true backbone**.

2. Import pattern is:

   ```python
   from filestate import folderleap
   ```

3. filestate responsibilities:

   * Record calling script path on import.
   * Maintain `# ORIGIN:` header logic.
   * Handle folder-leap detection + response.
   * Expose a **no-op or simple** `folderleap()` symbol so user code can safely import it even if unused at runtime.

4. **No GPT should**:

   * Invent new origin markers (`# HOME:` etc.) without explicit user request.
   * Hardcode machine-specific paths.
   * Add heavy dependencies for simple behaviors.

---

## 5. Formatics Semantics: How GPTs Should Encode Them

When encoding your theory into code:

### 5.1. Mirrors, not mysticism

* `X ~ C` → explicit function or dataclass relation:

  ```python
  @dataclass
  class Anchor:
      X: Any
      C: Any
  ```

* `strata : form ; order` can be captured as:

  ```python
  @dataclass
  class Strata:
      form: Any
      order: Any
  ```

### 5.2. Never bury the math in "clever" syntax

* GPTs should **avoid metaprogramming tricks** that obscure the theory.

* Code should read like:

  > "Here is Element Theory / X ~ C / strata ! structure written in Python."

* Every core concept should have:

  * A type (class or dataclass),
  * A clear docstring mapping back to your notation.

---

## 6. Change Discipline: Patch, Don't Rewrite

When asking GPT to help:

* **One file at a time**.
* GPT edits should be **minimal diff** style:

  * Add functions instead of inlining logic into existing ones, unless requested.
  * Refactor only when explicitly told.

For GPT:

> "If I don't see it in the prompt, I must assume it doesn't exist."

So:

* Don't add imports to modules you haven't been told about.
* Don't assume repo structure other than what's shown/manually described.

---

## 7. Tests: How GPTs Should Add Them

If you let GPT add tests:

* Use `tests/` directory:

  * `tests/test_element_theory.py`
  * `tests/test_filestate.py`
* Prefer Python's built-in `unittest` or `pytest` with simple, declarative tests.

Example:

```python
def test_anchor_xc_invariants():
    X, C = anchor_xc("example")
    assert X is not None
    assert C is not None
```

---

## 8. Summary: The Core Protocol

Any GPT assisting with this repo MUST assume:

- It cannot see the repo; it only sees what is pasted into the prompt.
- It must not invent non-existent modules or paths.
- It must treat code edits as small transforms of visible files.

### Core rules:

1. **Filestate/folderleap**
   - `filestate.py` owns file-origin and folder-leap logic.
   - Import pattern: `from filestate import folderleap`.
   - Side effects on import must be explicit and documented.

2. **Formatics core**
   - Math and Element Theory live in `form_*.py` or clearly named modules.
   - Represent theories (X ~ C, strata ! structure, etc.) as explicit classes/functions.
   - Avoid hidden I/O or global state changes in theory modules.

3. **Edits**
   - Only modify what is provided.
   - Prefer additive changes and minimal diffs.
   - Don't refactor broadly unless explicitly asked.

---

## Next Steps

For new contributors or GPT sessions:

1. Read this document first.
2. Ask the user to provide the specific file(s) to modify.
3. Confirm the desired behavior or invariant.
4. Apply minimal, clear changes.
5. Document theory-to-code mappings in docstrings.

See also: `FORMATICS_GPT_PROTOCOL.md` for a condensed reference.
