from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class EntityType(str, Enum):
    CPF = "CPF"
    CNPJ = "CNPJ"
    EMAIL = "EMAIL"
    TELEFONE = "TELEFONE"
    CEP = "CEP"
    CARTAO_CREDITO = "CARTAO_CREDITO"
    RG = "RG"
    NOME = "NOME"
    ENDERECO = "ENDERECO"


class Sensitivity(str, Enum):
    ALTA = "ALTA"
    MEDIA = "MEDIA"
    BAIXA = "BAIXA"


class Strategy(str, Enum):
    MASK = "MASK"
    REDACT = "REDACT"
    HASH = "HASH"


class ScanConfig(BaseModel):
    entities: List[EntityType] = Field(default_factory=lambda: list(EntityType))
    strategy: Strategy = Strategy.MASK


class ScanRequest(BaseModel):
    text: str
    config: Optional[ScanConfig] = None


class Finding(BaseModel):
    type: EntityType
    value_masked: str
    start: int
    end: int
    sensitivity: Sensitivity
    valid: bool


class AuditInfo(BaseModel):
    timestamp: str
    total_findings: int
    strategy_applied: Strategy


class ScanResponse(BaseModel):
    findings: List[Finding]
    sanitized_text: str
    audit: AuditInfo
