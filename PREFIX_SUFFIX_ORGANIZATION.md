# Prefix/Suffix Organization Guide

This guide combines the `tools/prefix_suffix_index.py` grouping logic with the FormET
naming patterns to keep the repository easy to navigate for agents and humans.
Alphabetic prefixes and suffixes are treated as the primary keys; file
extensions are ignored.

## Quick commands

- Full scan from repository root:
  ```bash
  python3 tools/prefix_suffix_index.py
  ```
- Focused scan (e.g., tests only):
  ```bash
  python3 tools/prefix_suffix_index.py tests
  ```

## Primary prefix clusters

- **formET_corpus/**: FormET artifacts grouped by prefix
  (`formET_0a.txt`, `formET_1a.txt`, `formET_2a.txt`, `formET_A1.txt`,
  `formET_B1.txt`, `formET_Ba.txt`, `formET_C1.txt`, `formET_Ca.txt`,
  `formET.pdf`, `formET.ods`). Use the common prefix to track versions and
  variants together.
- **formatic***: reference definitions and Python implementations inside
  `_ref/form_/formatic_mark.{md,py}` with corresponding tests in
  `tests/test_formatic_mark.py`.
- **theory/**: conceptual proofs and mappings (`categorical_interpretation.md`,
  `necessity_proof.md`, `python_mapping.md`, `index.md`).
- **filestate***: folder-leap tracking utility (`filestate.py`) with coverage in
  `tests/test_filestate.py`.
- **prefix_suffix***: directory-grouping CLI (`tools/prefix_suffix_index.py`)
  that powers this guide.
- **protocol/reference docs**: `FORMATICS_AGENT_PROTOCOL.md`,
  `CONTRIBUTING-AGENT.md`, `QUICK_REFERENCE.md`, and the repository root
  `README.md`.

## Primary suffix clusters

Suffixes reveal how related entries close out their names, useful when prefixes
are shared:

- **`*_a`**: progressive sequence (`formET_0a`, `formET_1a`, `formET_2a`).
- **`*_A1` / `*_B1` / `*_C1`**: numbered family with uppercase anchors.
- **`*_Ba` / `*_Ca`**: variant branches off the `B` and `C` tracks.
- **`*mark`**: Formatic mark definitions and code (`formatic_mark.md`,
  `formatic_mark.py`, `test_formatic_mark.py`).
- **`*filestate`**: runtime location tracking (`filestate.py`,
  `test_filestate.py`).
- **`*index`**: entry-point indexes (`tools/prefix_suffix_index.py`,
  `theory/index.md`).

## Navigation heuristics

1. **Start with the prefix** to locate the topic family (e.g., `formET`,
   `theory`, `test`).
2. **Check the suffix** to locate a variant or role within that family
   (`_A1` vs `_Ba`, `mark` vs `index`).
3. **Ignore extensions first**: `.md`, `.py`, `.pdf`, `.ods`, and `.txt` are
   alternate views of the same conceptual item.
4. **Pair code with tests** by matching suffixes (`filestate` ↔ `test_filestate`,
   `formatic_mark` ↔ `test_formatic_mark`).

## When adding new files

- Choose a **prefix** that aligns with an existing family before inventing a new
  one; this keeps scans coherent.
- Use **meaningful suffixes** to indicate lineage (e.g., `_A2` for the next
  A-series addition or `_mark` for new mark-focused material).
- Keep **extensions secondary**: prefer adding `.md` or `.py` variants under the
  same prefix/suffix instead of creating unrelated names.
