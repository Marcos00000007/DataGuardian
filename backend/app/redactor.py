import hashlib

from .models import EntityType, Strategy


def _mask_default(value: str, visible_tail: int = 0) -> str:
    if visible_tail:
        return "*" * (len(value) - visible_tail) + value[-visible_tail:]
    return "*" * len(value)


def apply_strategy(entity_type: EntityType, value: str, strategy: Strategy) -> str:
    if strategy == Strategy.REDACT:
        return "[REDACTED]"

    if strategy == Strategy.HASH:
        digest = hashlib.sha256(value.encode()).hexdigest()[:10]
        return f"[HASH:{digest}]"

    # MASK — regras específicas por tipo (RN05)
    if entity_type in (EntityType.CPF, EntityType.CNPJ):
        return _mask_default(value, visible_tail=2)

    if entity_type == EntityType.CARTAO_CREDITO:
        return _mask_default(value, visible_tail=4)

    if entity_type == EntityType.EMAIL and "@" in value:
        _, domain = value.split("@", 1)
        return f"***@{domain}"

    return _mask_default(value)
