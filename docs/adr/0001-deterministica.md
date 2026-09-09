Set-Content -Path docs\adr\0001-deteccao-deterministica.md -Encoding UTF8 -Value @'
# ADR-0001: Detecção de dados pessoais via regras determinísticas (não ML) na v1

**Status:** Aceita
**Data:** 2026-09-08

## Contexto

O Data Guardian precisa identificar dados pessoais (CPF, CNPJ, e-mail, telefone, etc.) em textos de entrada. Existem duas abordagens possíveis: (a) regras determinísticas (regex + validação matemática de checksum) ou (b) um modelo de NLP/ML treinado para reconhecimento de entidades (NER).

## Decisão

Na v1, optamos por usar **regras determinísticas** (regex + validação de dígitos verificadores para CPF/CNPJ) em vez de um modelo de ML.

## Motivos

- **Testabilidade (RNF02, RNF05):** regras determinísticas produzem sempre a mesma saída para a mesma entrada.
- **Auditabilidade:** é possível explicar exatamente por que uma entidade foi ou não detectada.
- **Escopo e prazo:** treinar/ajustar um modelo de ML está fora do escopo desta sprint inicial.
- **Sem dependências externas:** mantém o ambiente simples e reprodutível via Docker (RNF04).

## Consequências

- Nomes e endereços serão detectados apenas por heurísticas simples na v1.
- Uma eventual v2 pode incorporar NER como camada complementar.
'@
