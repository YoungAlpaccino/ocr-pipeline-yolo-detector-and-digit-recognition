# OCR Pipeline — YOLO Detector + Custom Digit Recognition

> ## NOTE
> **The code in this repository is a demonstration of the architecture and is not a working OCR service.**
> Model weights, dataset paths, character sets, and post-processing rules have been deliberately
> abstracted. Treat the files as a structural blueprint, not a turn-key OCR system.

---

## What this project demonstrates

A multi-stage OCR pipeline tuned for ID-card-style documents where off-the-shelf OCR engines
struggle (mixed scripts, glare, rotation, perspective). The pipeline is split into six
independent stages:

1. **Detect** the card in the input image (YOLO).
2. **Correct perspective** (homography from the four detected corners).
3. **De-rotate** to canonical orientation.
4. **Detect text lines** inside the card.
5. **Segment digits** out of each line (custom segmenter — the off-the-shelf ones break on
   the script we care about).
6. **Recognise** the digits with a small custom CNN, with optional post-processing rules
   (national-id checksum, script-translation, character normalisation).

The interesting part is the **per-stage isolation**: each stage exposes a tiny interface, and
the orchestrator runs them in order without knowing what's inside. Swapping the detector or
the recogniser is a one-file change.

## High-level diagram

```
   image ──► detect ──► perspective ──► derotate ──► line detect ──► digit segment ──► recognise ──► post-process ──► text
```

## Files in this showcase

| File | What it shows |
|------|---------------|
| `pipeline.py`                    | Orchestrator — wires the stages together. |
| `stages/detect.py`               | YOLO card detector (stub). |
| `stages/perspective_correction.py` | Four-corner homography. |
| `stages/rotation.py`             | Canonical orientation. |
| `stages/line_detector.py`        | Text-line localisation. |
| `stages/digit_segmenter.py`      | Per-line digit extractor (sketch). |
| `stages/recogniser.py`           | Small CNN classifier head. |
| `stages/post_process.py`         | Script normalisation + checksum validation. |
| `model_architecture.py`          | The CNN definition (PyTorch sketch). |
| `serve.py`                       | FastAPI wrapper — single `POST /ocr` endpoint. |
| `requirements.txt`               | Unpinned dependency surface. |
