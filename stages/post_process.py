"""
Post-process (sketch).

Normalises script + character variants, then runs a checksum-style
validation specific to the document type. Returns (normalised_text, is_valid).
"""
from typing import Tuple


def normalise_and_validate(raw: str) -> Tuple[str, bool]:
    cleaned = _normalise(raw)
    return cleaned, _validate_checksum(cleaned)


def _normalise(s: str) -> str:
    return "".join(c for c in s if c.isdigit())


def _validate_checksum(s: str) -> bool:
    """Stub: real impl computes the document-specific check digit."""
    return len(s) == 10
