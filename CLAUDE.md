# Instruções para Agentes de IA — Data Guardian

Este projeto segue o fluxo **SDD (Spec-Driven Development)**. Antes de gerar ou alterar qualquer código, o agente deve:

1. Ler `docs/SPECIFICATION.md` — é a fonte da verdade sobre requisitos, regras de negócio e contratos de API. Não gerar código que contradiga ou ignore esse documento.
2. Nunca inventar um campo, endpoint ou regra de negócio que não esteja na especificação. Se algo estiver ambíguo, sinalizar a ambiguidade em vez de assumir uma resposta.
3. Manter os componentes do backend isolados e puros sempre que possível (`detector`, `validator`, `classifier`, `redactor`, `audit`), conforme a seção 8 da especificação — isso é o que permite testes unitários independentes (RNF05).
4. Nunca persistir ou logar dados pessoais originais em texto puro (RNF03/RN06).
5. Qualquer mudança de escopo ou de regra de negócio deve ser registrada na seção 10 (Registro de Refinamento) de `docs/SPECIFICATION.md`, com data, motivo e responsável.
6. Ao alterar um componente do pipeline de scan, rodar/atualizar os testes existentes em `backend/tests/`.

## Stack do projeto

- **Backend:** Python 3.11 + FastAPI + Pydantic
- **Frontend:** React + TypeScript + Vite + Tailwind CSS
- **Infraestrutura:** Docker + Docker Compose

## Comandos úteis

```bash
# subir tudo (backend na porta 8000, frontend na porta 5173)
docker-compose up --build

# rodar os testes do backend
docker-compose exec backend pytest -v

# rodar os testes do backend sem Docker
cd backend && pip install -r requirements-dev.txt && pytest -v
```

## Convenções de commit

Usar prefixos: `feat:`, `fix:`, `docs:`, `test:`, `refactor:` — facilita ler o histórico e escrever as ADRs depois.
