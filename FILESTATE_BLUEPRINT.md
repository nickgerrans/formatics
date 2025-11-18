# Filestate Blueprint

## Overview

The `filestate.py` module provides **folder-leap detection** for any Python script in this repository. It serves as the **single source of truth** for tracking file origins and detecting when files are moved between directories.

## Core Concept

When any Python file imports `filestate`, the module:

1. **Detects** which script imported it
2. **Reads** the script's `# ORIGIN:` tag (if present)
3. **Compares** the origin directory to the current directory
4. **Triggers** an action if they differ (folder-leap detected)
5. **Updates** the origin tag to the new location

## Usage

In any Python file, simply add:

```python
from filestate import folderleap
```

That's it. No other setup required.

## How It Works

### First Run

When you first run a script that imports `filestate`:

```python
# my_script.py
from filestate import folderleap

print("Hello!")
```

After running, the file is automatically modified:

```python
# ORIGIN:/home/user/formatics
from filestate import folderleap

print("Hello!")
```

### On Folder-Leap

If you copy/move this file to another directory and run it:

```bash
cp my_script.py /tmp/
cd /tmp
python my_script.py
```

Output:
```
[folderleap] my_script.py moved:
  from: /home/user/formatics
    to: /tmp
Hello!
```

The file is automatically updated with the new origin:

```python
# ORIGIN:/tmp
from filestate import folderleap

print("Hello!")
```

## Repository Structure

This blueprint works with the current formatics repo structure:

```
formatics/
  filestate.py              # ← Single source of truth (repo root)

  tools/
    __init__.py
    prefix_suffix_index.py  # Can import filestate

  tests/
    test_filestate.py       # Tests for filestate
    test_formatic_mark.py   # Can import filestate

  _ref/
    form_/
      formatic_mark.py      # Can import filestate

  example_leap_aware.py     # Example usage
```

## Environment Variables

The implementation supports optional control:

- **`FILESTATE_DISABLE_TRIGGER`**: Set to disable the automatic trigger on leap
- **`FILESTATE_DISABLE_AUTO_PRIME`**: Set to disable all auto-priming behavior
- **`FILESTATE_DEBUG`**: Set to enable debug output

Example:

```bash
FILESTATE_DISABLE_TRIGGER=1 python my_script.py
```

## Integration with Formatics Philosophy

This blueprint aligns with formatics' **strata/form/order** principles:

### Strata (Layers)
- `filestate.py` occupies its own **stratum** at the repo root
- It's a foundational layer that other layers can depend on
- Clear separation: file-state logic is isolated from domain logic

### Form (Structure)
- Each file opts into leap-awareness via a simple import
- The `# ORIGIN:` tag is a **visible marker** of state
- Form is self-documenting: the tag shows the file's history

### Order (Dependencies)
- Unidirectional dependency: files import `filestate`, never the reverse
- No circular dependencies possible
- Clean, predictable import graph

## Advanced: Custom Leap Behavior

The default `_on_leap()` function prints a message and runs the script. You can customize this by modifying `filestate.py:55-60`:

```python
def _on_leap(path: Path, old_dir: str, new_dir: str) -> None:
    """Default handler executed when a folder leap is detected."""
    print(f"[folderleap] {path.name} moved:")
    print(f"  from: {old_dir}")
    print(f"    to: {new_dir}")
    # Customize this behavior as needed
    subprocess.run([sys.executable, str(path)], check=False)
```

## Testing

Run the test suite:

```bash
pytest tests/test_filestate.py -v
```

Tests verify:
- Origin recording on first import
- Origin updates on folder-leap
- Proper handling with environment variables

## Example

See `example_leap_aware.py` for a minimal demonstration:

```bash
python example_leap_aware.py
```

## Benefits

1. **Repo-agnostic**: Works with any directory structure
2. **Opt-in**: Only files that import `filestate` are affected
3. **Zero-config**: No setup files or configuration needed
4. **Self-documenting**: The `# ORIGIN:` tag is visible in the file
5. **Testable**: Environment variables allow control for testing
6. **Minimal**: Single file, ~105 lines of code

## Extending the Repository

As the repo grows, the pattern scales:

```
formatics/
  filestate.py              # Always at root

  package_a/
    __init__.py
    module1.py              # from filestate import folderleap
    module2.py              # from filestate import folderleap

  package_b/
    __init__.py
    core.py                 # from filestate import folderleap

  scripts/
    analyze.py              # from filestate import folderleap
    transform.py            # from filestate import folderleap

  notebooks/
    exploration.ipynb       # Can use %run or import
```

As long as `filestate.py` stays at the root (or is installed as a package), all files can access it via the standard import mechanism.

## Conclusion

The `filestate` module embodies the formatics philosophy:

- **Single responsibility**: Track file origins, nothing else
- **Minimal coupling**: One-way import dependency
- **Explicit state**: Visible `# ORIGIN:` tags
- **Emergent behavior**: Simple import → complex tracking

This is the blueprint for folder-leap awareness in **any** repository.
