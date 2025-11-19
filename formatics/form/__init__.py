"""
Formatics form: Core element structure and composition.

This module defines the fundamental form elements and their anchors.
"""

from .anchor import Anchor
from .elements import Element, FormElement

__all__ = ["Element", "FormElement", "Anchor"]
