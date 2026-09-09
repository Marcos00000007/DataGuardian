# ADR-0002: Escolha da stack tecnológica

**Status:** Aceita
**Data:** 2026-09-09

## Contexto

O Data Guardian precisa de uma stack para implementar a API descrita em `docs/SPECIFICATION.md`, fácil de containerizar (RNF04) e com suporte maduro para testes automatizados (RNF05).

## Decisão

- **Backend:** Python 3.11 + FastAPI (validação de contrato via Pydantic).
- **Frontend:** React + TypeScript + Vite + Tailwind CSS.
- **Infraestrutura:** Docker + Docker Compose, com um serviço para cada camada.

## Motivos

- Pydantic mapeia diretamente os contratos de entrada/saída da spec.
- pytest é o framework padrão do ecossistema Python (RNF05).
- React + TypeScript compartilha o mesmo formato de tipos do contrato de API.

## Consequências

- O test harness será escrito em pytest, dentro de `backend/tests/`.
- O docker-compose documenta dois serviços: backend (porta 8000) e frontend (porta 5173).
- O frontend é um cliente de demonstração da API.
'@