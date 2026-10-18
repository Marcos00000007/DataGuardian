from typing import List

from .detector import Candidate
from .models import EntityType, Sensitivity

# RN03 — classificação de sensibilidade
SENSITIVITY_MAP = {
    EntityType.CPF: Sensitivity.ALTA,
    EntityType.RG: Sensitivity.ALTA,
    EntityType.CARTAO_CREDITO: Sensitivity.ALTA,
    EntityType.EMAIL: Sensitivity.MEDIA,
    EntityType.TELEFONE: Sensitivity.MEDIA,
    EntityType.CNPJ: Sensitivity.MEDIA,
    EntityType.CEP: Sensitivity.BAIXA,
    EntityType.NOME: Sensitivity.BAIXA,
    EntityType.ENDERECO: Sensitivity.BAIXA,
}

_RANK = {Sensitivity.BAIXA: 0, Sensitivity.MEDIA: 1, Sensitivity.ALTA: 2}


def classify(entity_type: EntityType) -> Sensitivity:
    return SENSITIVITY_MAP.get(entity_type, Sensitivity.BAIXA)


def resolve_overlaps(candidates: List[Candidate]) -> List[Candidate]:
    """RN04: se duas entidades se sobrepõem no texto, mantém a de maior sensibilidade."""
    sorted_candidates = sorted(candidates, key=lambda c: (c.start, c.end))
    resolved: List[Candidate] = []

    for candidate in sorted_candidates:
        overlap_index = None
        for i, kept in enumerate(resolved):
            if candidate.start < kept.end and candidate.end > kept.start:
                overlap_index = i
                break

        if overlap_index is None:
            resolved.append(candidate)
            continue

        kept = resolved[overlap_index]
        if _RANK[classify(candidate.type)] > _RANK[classify(kept.type)]:
            resolved[overlap_index] = candidate

    return resolved
