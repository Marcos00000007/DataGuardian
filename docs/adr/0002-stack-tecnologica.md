# ADR-0002: Escolha da stack tecnológica

**Status:** Em definição — preencher após decisão do Marcos
**Data:** _(preencher)_

## Contexto

O Data Guardian precisa de uma stack para implementar a API (`POST /v1/scan`, `GET /v1/health`) descrita em `docs/SPECIFICATION.md`, que seja fácil de containerizar (RNF04) e tenha suporte maduro para testes automatizados (RNF05).

## Opções consideradas

- **Python + FastAPI** — tipagem com Pydantic facilita validar os contratos de entrada/saída da spec; `pytest` maduro para o test harness.
- **Node.js + Express** — ecossistema `jest`/`supertest` também maduro para testes de API.

## Decisão

<!-- Marcos: preencher qual foi escolhida e por quê -->

## Motivos

<!-- ex: familiaridade da equipe, facilidade de validação de regex/checksum, ecossistema de testes -->

## Consequências

<!-- ex: define a linguagem que o João Paulo usará no test harness e o Pedro Henrique no README -->
