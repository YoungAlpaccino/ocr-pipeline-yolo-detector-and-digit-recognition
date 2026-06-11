"""
Recogniser head (sketch).

A tiny CNN that maps a digit crop to a class + confidence.
"""
from typing import Tuple


def recognise_digit(crop) -> Tuple[str, float]:
    """Stub: real impl loads model_architecture.DigitCNN and runs a forward
    pass on the preprocessed crop."""
    return "0", 0.95
