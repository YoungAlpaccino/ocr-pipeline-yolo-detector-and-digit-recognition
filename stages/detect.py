"""
YOLO card detector (sketch).

Returns the four corner points of the card in the input image, or None
if no card was found.
"""
from typing import Optional, Tuple

Corners = Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]]


def detect_card(img) -> Optional[Corners]:
    """Stub: real impl runs YOLOv8 on `img`, picks the highest-confidence
    'card' box, and finds its corners via a follow-up keypoint head."""
    return ((0, 0), (1000, 0), (1000, 600), (0, 600))
