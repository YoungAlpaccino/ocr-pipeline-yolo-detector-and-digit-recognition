"""
FastAPI wrapper — single POST /ocr endpoint (sketch).
"""
import logging
from fastapi import FastAPI, UploadFile, File, HTTPException

import pipeline

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s")

app = FastAPI(title="ocr-pipeline-sketch")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/ocr")
async def ocr(f: UploadFile = File(...)):
    raw = await f.read()
    if not raw:
        raise HTTPException(400, "empty payload")
    res = pipeline.run(raw)
    return {
        "text":       res.text,
        "confidence": res.confidence,
        "is_valid":   res.is_valid,
    }
