# API Stability, Fork Policy, and External Interface Contract

This document defines:
1. What parts of Formatics are stable vs. experimental
2. How external systems may interact with Formatics
3. Fork policy and derivative work rules
4. The boundary between theory and implementation

---

## API Stability Guarantees

### Stable (Public API)

The following are **guaranteed stable** across MINOR versions (0.x.0 → 0.y.0):

#### Core Classes
- `formatics.slot.Slot`
  - Constructor: `Slot(position: int, element: Optional[Any], label: Optional[str])`
  - Methods: `fill()`, `empty()`, `is_filled()`

- `formatics.orbit.Orbit`
  - Constructor: `Orbit(element: Any, states: List[str], current_index: int)`
  - Methods: `advance()`, `current_state()`, `reset()`

- `formatics.form.Element`
  - Constructor: `Element(value: Any, metadata: Dict[str, Any])`
  - Methods: `transform()`

- `formatics.form.FormElement`
  - Constructor: `FormElement(elements: list[Element], form_type: Optional[str])`
  - Methods: `add()`, `compose()`

#### Module Exports
- `formatics/__init__.py` exports are stable
- Anything listed in `__all__` is part of public API

#### Theory Documents
- Core axioms in `theory/AXIOMS.md` (Items 1-4)
- The Formatic mark equation: `([()]) = (())`
- Necessity theorem for pattern matching

**Stability Promise:** These will not have breaking changes in MINOR versions. Deprecation warnings will be issued at least one MAJOR version before removal.

---

### Experimental (Unstable API)

The following may change in MINOR versions:

#### Modules
- `formatics.paths.*` - Path tracking (under development)
- `formatics.logs.*` - History logging (under development)
- `formatics.filestate` / `formatics.folderleap` - Utility features

#### Implementation Details
- Internal helper functions not in `__all__`
- Private methods (prefixed with `_`)
- Test utilities

**Use at your own risk:** These may change signature, behavior, or be removed without notice.

---

### Deprecated

Currently no deprecated features. When features are deprecated:
- They will be marked in code with `warnings.warn(DeprecationWarning)`
- They will be listed in CHANGELOG.md
- They will remain functional for at least one MAJOR version
- Migration path will be documented

---

## Theory vs. Implementation Boundary

### What is Theory?

**Theory is the mathematical structure that exists independent of any implementation:**

- The Formatic mark: `([()]) = (())`
- The three operators: slot `()`, orbit `[]`, closure `(())`
- Core axioms (see `theory/AXIOMS.md`)
- Necessity theorem (pattern matching languages must exhibit the mark)
- Categorical interpretation (Core ≅ Skel)

**Theory is discovered, not invented.** It exists in mathematics prior to any code.

---

### What is Implementation?

**Implementation is the specific realization in Python code:**

- `Slot`, `Orbit`, `Closure` classes
- Module organization (`formatics/slot.py`, etc.)
- File paths and naming conventions
- Build system (pyproject.toml)
- Testing infrastructure

**Implementation is designed and may change.** However, it must always correctly implement the theory.

---

### The Boundary

**You cannot claim to have "invented a different theory" by:**
- Renaming `Slot` to `Container`
- Reorganizing module structure
- Rewriting in a different language
- Changing variable names or documentation

**These are implementation details, not theoretical contributions.**

**You CAN contribute a genuine theoretical extension by:**
- Proving a new necessity theorem in a different domain
- Discovering a new operator beyond slot/orbit/closure
- Proving deeper categorical connections
- Extending to dependent types, HoTT, etc.

Such contributions must:
1. Be mathematically novel (not just code refactoring)
2. Build upon (not contradict) existing axioms
3. Be properly attributed to Formatics as the foundation
4. Be contributed under the CLA (see CONTRIBUTING.md)

---

## Fork Policy

### Academic Forks (Permitted)

You MAY fork Formatics for academic research if:

✅ **Permitted Uses:**
- Studying the theory for educational purposes
- Implementing in other languages (Rust, Haskell, etc.) for research
- Extending proofs or exploring new domains
- Creating educational materials citing Formatics
- Publishing academic papers that reference and build upon Formatics

✅ **Requirements:**
- Retain all LICENSE, CITATION.cff, and copyright notices
- Clearly state "Based on Formatics by Nicholas Gerrans"
- Link back to original repository: https://github.com/nickgerrans/formatics
- Do not claim independent discovery of the Formatic mark
- Cite properly using CITATION.cff format

---

### Commercial Forks (Prohibited)

You MAY NOT fork Formatics for commercial use, including:

❌ **Prohibited:**
- Building commercial products based on Formatics
- Using in proprietary software without explicit permission
- Training AI/ML models on Formatics code or theory
- Incorporating into closed-source applications
- Commercial research or industrial R&D
- Consulting services based on Formatics

**To obtain commercial rights:** Contact Nicholas Gerrans for licensing terms.

---

### Derivative Work Restrictions

Even in academic contexts, you MAY NOT:

❌ **Prohibited Derivative Works:**
- Create "competing frameworks" that obscure Formatics origin
- Rename the core concepts and claim independent discovery
- Remove attribution or delink from Formatics
- Relicense under more permissive terms
- Create forks that allow commercial use

**All derivative works remain subject to the Formatics Proprietary License** and ownership of Nicholas Gerrans per the LICENSE agreement.

---

## External Interface Contract

### How External Systems May Use Formatics

#### Permitted Interfaces

✅ **Import and Use in Academic Projects:**
```python
from formatics import Slot, Orbit
from formatics.form import Element

# Use in non-commercial academic research
slot = Slot(position=0)
slot.fill(my_data)
```

✅ **Reference in Academic Publications:**
- Cite using CITATION.cff format
- Discuss theory in papers with proper attribution
- Compare to other formal systems

✅ **Educational Use:**
- Teaching formal methods courses
- Demonstrating structural invariants
- Category theory pedagogy

---

#### Prohibited Interfaces

❌ **NO Training AI Models:**
```python
# PROHIBITED - violates LICENSE Section 2
training_data = load_formatics_repo()
model.train(training_data)  # NOT ALLOWED
```

❌ **NO Commercial API Consumption:**
```python
# PROHIBITED - commercial use requires license
from formatics import Slot  # In commercial product
```

❌ **NO Embedding in Proprietary Software:**
```python
# PROHIBITED - derivative works are not permitted
# in closed-source or commercial contexts
```

---

### API Consumption Rules

If you use Formatics in permitted (academic) contexts:

**1. Version Pinning:**
Pin to specific versions to avoid breaking changes:
```toml
[dependencies]
formatics = "==0.1.0"  # Exact version
```

**2. Import Only from Public API:**
Only import from modules listed in `formatics/__init__.py.__all__`

**3. No Monkey Patching:**
Do not modify Formatics classes at runtime:
```python
# PROHIBITED
Slot.fill = my_custom_fill  # Don't do this
```

**4. Attribution in Your Code:**
Include attribution in your project README:
```markdown
This project uses Formatics by Nicholas Gerrans.
See: https://github.com/nickgerrans/formatics
```

---

## Breaking Change Policy

### What Constitutes a Breaking Change?

**API Breaking Changes:**
- Removing public classes, functions, or methods
- Changing function signatures (parameter names, types, defaults)
- Changing return types
- Renaming modules in public API
- Altering class inheritance hierarchy

**Theory Breaking Changes:**
- Modifying core axioms (extremely rare)
- Contradicting existing proofs
- Redefining the mark equation

**Non-Breaking Changes:**
- Adding new classes, functions, or modules
- Adding optional parameters with defaults
- Performance improvements
- Bug fixes that correct behavior to match theory
- Documentation improvements

---

### Deprecation Process

When we must make a breaking change:

**1. Announce (version N):**
- Add deprecation warning in code
- Document in CHANGELOG.md
- Provide migration guide

**2. Deprecation Period (version N+1):**
- Old API still works but warns
- New API available alongside
- Documentation shows both

**3. Removal (version N+2):**
- Old API removed
- MAJOR version bump (N → N+1 in semver)

**Example:**
```
v0.5.0: Announce Slot.remove() is deprecated, use Slot.empty()
v0.6.0: Both work, Slot.remove() warns
v1.0.0: Slot.remove() removed, only Slot.empty() exists
```

---

## External System Compatibility

### Supported Python Versions

**Currently Supported:** Python 3.8, 3.9, 3.10, 3.11, 3.12

**Support Policy:**
- Support actively maintained Python versions
- Drop support for EOL Python versions in MINOR releases
- Announce deprecation at least 6 months before dropping

---

### Dependencies

**Current Policy:** Zero runtime dependencies

**Future Policy:**
- Avoid dependencies where possible
- Any new dependency must be:
  - Widely used and maintained
  - Compatible with the academic-use license
  - Essential (not convenience)
  - Approved by copyright holder

---

### Interoperability

Formatics is designed to be **self-contained** and not tightly coupled to external frameworks.

**Deliberate Design:**
- No required integration with specific web frameworks
- No database dependencies
- No cloud service dependencies
- Pure Python, portable across platforms

**This ensures:**
- Longevity (no dependency rot)
- Academic accessibility (easy to install and study)
- IP clarity (no license contamination)

---

## Enforcement

### Violation Examples

**Scenario 1: Unnamed Commercial Fork**
A company forks Formatics, removes LICENSE, renames it "PatternTheory," and sells it.

**Violation:** Copyright infringement, LICENSE violation, derivative work without permission

**Action:** Legal action for damages, injunction, public notice

---

**Scenario 2: AI Model Training**
An AI lab trains a language model on Formatics code and theory without permission.

**Violation:** LICENSE Section 2 (prohibited use by AI systems)

**Action:** Cease-and-desist, potential legal action

---

**Scenario 3: Attribution Removal**
An academic paper describes the mark `([()]) = (())` but doesn't cite Formatics.

**Violation:** Academic misconduct, LICENSE Section 2 (delinking attribution)

**Action:** Contact journal, request correction/retraction, public notice

---

**Scenario 4: Permitted Academic Use**
A university researcher forks Formatics, implements it in Haskell, properly cites Formatics, and publishes academic paper with attribution.

**Violation:** None ✅

**Action:** None (encouraged use case)

---

## Contact for Licensing

For questions about:
- Commercial licensing
- Permitted use cases
- API stability for specific use
- Derivative work permissions

**Contact:** Nicholas Gerrans via GitHub issues or direct contact

**Response Time:** Best effort within 2 weeks for licensing inquiries

---

## Summary Table

| Use Case | Permitted? | Requirements |
|----------|-----------|--------------|
| Academic research | ✅ Yes | Proper citation |
| Educational teaching | ✅ Yes | Retain LICENSE |
| Commercial product | ❌ No | Explicit license required |
| AI model training | ❌ No | Prohibited by LICENSE |
| Fork for study | ✅ Yes | Academic only, with attribution |
| Fork for commercial | ❌ No | Prohibited |
| Cite in paper | ✅ Yes | Use CITATION.cff format |
| Remove attribution | ❌ No | Always prohibited |
| Extend theory | ✅ Yes | Via CLA contribution process |
| Rename and claim | ❌ No | Always prohibited |

---

**Last Updated:** 2025-01-19
**Version:** 1.0 (tracks Formatics v0.1.0)
**Copyright (c) 2025 Nicholas Gerrans. All rights reserved.**
