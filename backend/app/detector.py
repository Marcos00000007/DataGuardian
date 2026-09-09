import re
from typing import List, NamedTuple

from .models import EntityType


class Candidate(NamedTuple):
    type: EntityType
    value: str
    start: int
    end: int


# Padrões de detecção (RF01/RF02). NOME e ENDERECO ficam para uma v2 com
# heurística/NLP mais robusta — fora do escopo desta v1 (ver SPECIFICATION.md, seção 3).
PATTERNS = {
    EntityType.CPF: re.compile(r"\d{3}\.?\d{3}\.?\d{3}-?\d{2}"),
    EntityType.CNPJ: re.compile(r"\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}"),
    EntityType.EMAIL: re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"),
    EntityType.TELEFONE: re.compile(r"(?:\(?\d{2}\)?\s?)?9?\d{4}-?\d{4}"),
    EntityType.CEP: re.compile(r"\d{5}-?\d{3}"),
    EntityType.CARTAO_CREDITO: re.compile(r"(?:\d{4}[ -]?){3}\d{4}"),
}


def detect(text: str, entity_types: List[EntityType]) -> List[Candidate]:
    """Encontra candidatos a entidades de dado pessoal via regex.

    Retorna apenas candidatos "crus" (sem validação de checksum) — a
    validação matemática de CPF/CNPJ fica a cargo do módulo `validator`
    (separação que atende ao RNF05: componentes testáveis isoladamente).
    """
    candidates: List[Candidate] = []
    for entity_type in entity_types:
        pattern = PATTERNS.get(entity_type)
        if not pattern:
            continue
        for match in pattern.finditer(text):
            candidates.append(
                Candidate(
                    type=entity_type,
                    value=match.group(),
                    start=match.start(),
                    end=match.end(),
                )
            )
    return candidates
