from datetime import datetime, timezone
from typing import List

from .detector import Candidate
from .models import AuditInfo, Strategy


def build_audit(findings: List[Candidate], strategy: Strategy) -> AuditInfo:
    """RN06: o log de auditoria nunca inclui o valor original do dado pessoal."""
    return AuditInfo(
        timestamp=datetime.now(timezone.utc).isoformat(),
        total_findings=len(findings),
        strategy_applied=strategy,
    )
