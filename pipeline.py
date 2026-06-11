"""
OCR pipeline orchestrator (sketch).

Each stage gets the previous stage's output and returns whatever the next
stage expects. Swap any one stage without touching the others.
"""
import logging
from dataclasses import dataclass
from typing import Optional

from stages.detect import detect_card
from stages.perspective_correction import correct_perspective
from stages.rotation import canonicalise
from stages.line_detector import find_text_lines
from stages.digit_segmenter import segment_digits
from stages.recogniser import recognise_digit
from stages.post_process import normalise_and_validate

logger = logging.getLogger(__name__)


@dataclass
class OcrResult:
    text: str
    confidence: float
    is_valid: Optional[bool]


def run(image_bytes: bytes) -> OcrResult:
    img = _load(image_bytes)

    corners = detect_card(img)
    if corners is None:
        return OcrResult(text="", confidence=0.0, is_valid=False)

    flat   = correct_perspective(img, corners)
    canon  = canonicalise(flat)

    digits = []
    confs  = []
    for line_box in find_text_lines(canon):
        for crop in segment_digits(canon, line_box):
            d, c = recognise_digit(crop)
            digits.append(d)
            confs.append(c)

    text, is_valid = normalise_and_validate("".join(digits))
    overall_conf = (sum(confs) / len(confs)) if confs else 0.0
    return OcrResult(text=text, confidence=overall_conf, is_valid=is_valid)


def _load(image_bytes: bytes):
    # Stub: real impl decodes with cv2.imdecode or PIL.Image.open.
    return image_bytes
