"""
Text-line localisation (sketch).

Returns bounding boxes of the lines that contain the digits we want.
"""
from typing import List, Tuple

Box = Tuple[int, int, int, int]  # x, y, w, h


def find_text_lines(canon) -> List[Box]:
    """Stub: real impl uses projection profiles + a small line detector head."""
    return [(80, 300, 800, 56)]
