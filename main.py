"""Generated Forge lite application for InsureGuard Fraud Scoring (IFS).
Built from build_spec.json (BRD ACs + backlog + architecture).
"""
from __future__ import annotations

import os
from typing import Any

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from domain import chat_answer, evaluate_rules, list_criteria, list_stories, meta, predict_payload

app = FastAPI(title="InsureGuard Fraud Scoring", version="1.0.0")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.joblib")
_model = None
try:
    import joblib
    if os.path.exists(MODEL_PATH):
        _model = joblib.load(MODEL_PATH)
except Exception:
    _model = None


@app.get("/health")
def health():
    m = meta()
    return {
        "status": "ok",
        "app": m.get("project_key"),
        "app_kind": m.get("app_kind"),
        "stories": len(m.get("story_ids") or []),
        "acceptance_criteria": len(m.get("ac_ids") or []),
    }


@app.get("/meta")
def get_meta():
    return meta()


@app.get("/stories")
def get_stories():
    return {"stories": list_stories()}


@app.get("/criteria")
def get_criteria():
    return {"acceptance_criteria": list_criteria()}


@app.post("/predict")
def predict(payload: dict[str, Any]):
    return predict_payload(payload, _model)


@app.get("/", response_class=HTMLResponse)
def index():
    with open(os.path.join(os.path.dirname(__file__), "index.html"), encoding="utf-8") as f:
        return f.read()
