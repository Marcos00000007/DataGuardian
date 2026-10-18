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
    EntityType.RG: re.compile(r"\b\d{1,2}\.?\d{3}\.?\d{3}-?\d{1,2}\b"),
    EntityType.NOME: re.compile(
        r"\b(?:me chamo|nome(?: completo)?(?:\s+\u00e9|:))\s+"
        r"(?P<value>[A-Z\u00c0-\u00d6\u00d8-\u00de][a-z\u00df-\u00f6\u00f8-\u00ff]+"
        r"(?:\s+[A-Z\u00c0-\u00d6\u00d8-\u00de][a-z\u00df-\u00f6\u00f8-\u00ff]+)+)",
        re.IGNORECASE,
    ),
    EntityType.ENDERECO: re.compile(
        r"\b(?:Rua|Avenida|Av\.|Travessa|Alameda|Pra\u00e7a)\s+"
        r"[\w]+(?:\s+[\w]+)*,\s*\d+[A-Za-z]?\b",
        re.IGNORECASE,
    ),
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
            value = match.groupdict().get("value")
            start, end = match.span("value") if value is not None else match.span()
            candidates.append(
                Candidate(
                    type=entity_type,
                    value=value if value is not None else match.group(),
                    start=start,
                    end=end,
                )
            )
    return candidates
