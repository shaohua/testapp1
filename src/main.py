from __future__ import annotations

import os
from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="Billing Admin Demo")


@app.get("/")
def root() -> dict[str, str]:
    return {
        "app": "billing-admin",
        "status": "internal",
        "runtime": "Cloud Run",
    }


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {
        "ok": "true",
        "log_level": os.getenv("LOG_LEVEL", "info"),
        "checked_at": datetime.now(timezone.utc).isoformat(),
    }
