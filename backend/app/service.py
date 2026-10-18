from typing import List

from . import audit, classifier, detector, redactor, validator
from .models import EntityType, Finding, ScanConfig, ScanResponse

VALIDATORS = {
    EntityType.CPF: validator.is_valid_cpf,
    EntityType.CNPJ: validator.is_valid_cnpj,
}


def scan_text(text: str, config: ScanConfig) -> ScanResponse:
    candidates = detector.detect(text, config.entities)

    validated = []
    for candidate in candidates:
        validate_fn = VALIDATORS.get(candidate.type)
        if validate_fn and not validate_fn(candidate.value):
            continue  # RN01/RN02: descarta falso positivo
        validated.append(candidate)

    resolved = classifier.resolve_overlaps(validated)
    resolved.sort(key=lambda c: c.start)

    findings: List[Finding] = []
    sanitized_parts = []
    cursor = 0

    for candidate in resolved:
        sanitized_parts.append(text[cursor:candidate.start])
        masked_value = redactor.apply_strategy(candidate.type, candidate.value, config.strategy)
        sanitized_parts.append(masked_value)
        cursor = candidate.end

        findings.append(
            Finding(
                type=candidate.type,
                value_masked=masked_value,
                start=candidate.start,
                end=candidate.end,
                sensitivity=classifier.classify(candidate.type),
                valid=True,
            )
        )

    sanitized_parts.append(text[cursor:])
    sanitized_text = "".join(sanitized_parts)

    audit_info = audit.build_audit(resolved, config.strategy)

    return ScanResponse(findings=findings, sanitized_text=sanitized_text, audit=audit_info)
