"""
Digit segmenter (sketch).

Off-the-shelf OCR struggles with this script — connected-component
analysis on its own over-merges joined glyphs. Real impl does a hybrid:
adaptive threshold → CC → split overly-wide CCs by a vertical-profile
minimum.
"""
from typing import Iterable


def segment_digits(canon, line_box) -> Iterable:
    """Stub: yields per-digit crops. Real impl returns ndarray crops."""
    x, y, w, h = line_box
    crop_w = w // 10
    for i in range(10):
        yield ("crop", x + i * crop_w, y, crop_w, h)
