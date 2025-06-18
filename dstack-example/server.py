#!/usr/bin/env python3
import os
import urllib.parse
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
import httpx
import uvicorn
from pydantic import BaseModel

# Path to the tappd Unix socket
TAPPD_SOCKET = "/var/run/tappd.sock"

# Percent-encode the socket path for httpx
_uds_path = urllib.parse.quote(TAPPD_SOCKET, safe="")
TAPPD_URL = f"http+unix://{_uds_path}"

app = FastAPI(title="TDX Attestation Server")

class QuoteRequest(BaseModel):
    report_data: str

@app.get("/report", response_class=JSONResponse)
async def report(nonce: str = Query("0x" + "00"*32, min_length=3)):
    """
    HTTP GET /report
    - Optional query param `nonce`, defaulting to 32 zero bytes.
    - Returns the JSON-formatted TDX attestation quote from tappd.
    """
    payload = {"report_data": nonce}

    async with httpx.AsyncClient(transport=httpx.HTTPTransport(uds=TAPPD_SOCKET)) as client:
        try:
            resp = await client.post(f"{TAPPD_URL}/prpc/Tappd.TdxQuote?json", json=payload, timeout=10.0)
            resp.raise_for_status()
        except httpx.HTTPError as exc:
            raise HTTPException(status_code=502, detail=f"Tappd error: {exc}") from exc

    return resp.json()

if __name__ == "__main__":
    # Use Uvicorn to serve the FastAPI app
    uvicorn.run("attestation_server:app", host="0.0.0.0", port=5000)
