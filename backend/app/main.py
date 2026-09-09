from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .models import ScanConfig, ScanRequest, ScanResponse
from .service import scan_text

app = FastAPI(title="Data Guardian", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ajustar para os domínios corretos em produção
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/v1/health")
def health():
    return {"status": "ok"}


@app.post("/v1/scan", response_model=ScanResponse)
def scan(request: ScanRequest):
    if not request.text or not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail={
                "code": "INVALID_PAYLOAD",
                "message": "Campo 'text' é obrigatório e não pode ser vazio.",
            },
        )

    config = request.config or ScanConfig()
    return scan_text(request.text, config)
