Set-Content -Path docs\DIVISAO_DE_TAREFAS.md -Encoding UTF8 -Value @'
# Divisão de Tarefas — Data Guardian
## Sprint 1 / Entrega Inicial (Ambiente, Especificação e Test Harness)

**Equipe:**
| Nome | RA |
|------|----|
| Marcos André Camargo Belo | _22510865_ |
| João Paulo Rodrigues de Oliveira | _22508370_ |
| Pedro Henrique Barbosa | _22503467_ |

Cada pessoa é dona de uma frente independente. Isso facilita o Code Review (cada PR fica pequeno e focado) e evidencia a decomposição do problema pedida na rubrica.

---

## 👤 Pedro Henrique — Repositório & Governança

**Branch:** `feature/repo-governance` / `feature/env-agents-skeleton` (docs consolidadas aqui)

<<<<<<< HEAD
- [x] Criar o repositório no GitHub
- [x] Configurar estrutura de branches: `main` (protegida), `develop`, `feature/*`
- [x] Ativar proteção da branch `main` (exige PR + aprovação antes do merge)
- [ ] Criar o GitHub Project (quadro Kanban: To Do / In Progress / Review / Done)
- [x] Criar Issues no GitHub (via `gh issue create`) — falta vincular ao Project
- [x] Criar template de Pull Request (`.github/PULL_REQUEST_TEMPLATE.md`)
- [x] Escrever o `README.md` (visão geral, guia de execução, seção de ADRs)
- [ ] Revisar/aprovar pelo menos 1 PR de outro membro
- [ ] Preencher os RAs da equipe no README e neste documento

**Entregável:** repositório estruturado + README.md + Project/Issues populados.

---

## Marcos André Camargo Belo — Ambiente, Agentes de IA & Esqueleto do Código

**Branch:** `feature/env-agents-skeleton`

- [x] Escolher a stack e registrar a decisão (ADR-0002: Python/FastAPI + React/TS/Vite/Tailwind + Docker)
- [x] Criar `Dockerfile` (backend e frontend) e `docker-compose.yml`
- [x] Configurar o agente de IA (Claude Code) e commitar `CLAUDE.md` com as regras do fluxo SDD
- [x] Implementar os componentes do pipeline (não são stubs — pipeline completo e funcional):
  - `detector.py` — detecção via regex por tipo de entidade (CPF, CNPJ, EMAIL, TELEFONE, CEP, CARTAO_CREDITO)
  - `validator.py` — validação de checksum de CPF/CNPJ (RN01/RN02)
  - `classifier.py` — classificação de sensibilidade + resolução de sobreposição (RN03/RN04)
  - `redactor.py` — estratégias de mascaramento MASK/REDACT/HASH (RN05)
  - `audit.py` — geração do log de auditoria sem dado original (RN06)
  - `service.py` — orquestração de todo o pipeline
- [x] Expor os endpoints `POST /v1/scan` e `GET /v1/health` (`main.py`)
- [x] Implementar o frontend de demonstração (React + TypeScript + Vite + Tailwind) consumindo a API
- [x] Documentar os comandos de execução no README (`docker-compose up --build`)

**Entregável:** ambiente containerizado funcional + arquivo de regras do agente + pipeline completo rodando os endpoints. ✅ **Concluído.**

---

## 👤 João Paulo Rodrigues de Oliveira — Test Harness & Evidências de Execução

**Branch:** `feature/test-harness`

<<<<<<< HEAD
- [x] Escolher o framework de testes (pytest)
- [x] Suíte cobrindo os cenários principais (RF01–RF08 da spec)
- [x] Testes para os 8 casos de borda da seção 9 da spec
- [x] Comando único de execução (`pytest -v`)
- [ ] Rodar a suíte no próprio ambiente e capturar o log/print real da execução
- [ ] (Bônus) workflow de GitHub Actions
=======
- [ ] Escolher o framework de testes compatível com a stack (pytest).
- [ ] Criar a suíte de testes cobrindo os cenários principais (RF01-RF08 da spec).
- [ ] Criar testes para os casos de borda (seção 9 da spec).
- [ ] Criar um único comando de execução que rode toda a suíte de uma vez.
- [ ] Rodar a suíte, capturar o log/print da execução bem-sucedida e salvar.
- [ ] (Bônus) configurar um workflow de GitHub Actions rodando os testes a cada Pull Request.

**Entregável:** suíte de testes (36 testes) + comando único de execução + log/print comprobatório real.

---

## Ordem sugerida (para não travar ninguém)

1. Pedro Henrique cria repo, branches e Issues.
2. Em paralelo, Marcos sobe o Dockerfile e o esqueleto; João Paulo escreve os testes a partir da spec.
3. Assim que o Marcos sobe os componentes, o João Paulo pluga os testes reais neles.
4. Cada PR precisa ser revisado por pelo menos um outro membro antes do merge.
5. Reunião rápida antes do prazo: revisar README, prints de execução e montar o PDF final juntos.

## Checklist do PDF final (Moodle)
## 🔗 Ordem sugerida (para não travar ninguém)

1. **Dia 1:** Pedro Henrique cria repo, branches e Issues → todo mundo já consegue abrir sua branch.
2. **Em paralelo:** Marcos já sobe o Dockerfile e começa o esqueleto; João Paulo já pode **escrever os testes a partir da spec** (estilo TDD), mesmo antes do código existir.
3. Assim que o Marcos subir os stubs dos componentes, o João Paulo pluga os testes reais neles.
4. Cada PR precisa ser revisado por **pelo menos um outro membro** antes do merge (exigência de Code Review).
5. Reunião rápida de 15min antes do prazo: revisar README, prints de execução e montar o PDF final juntos.

## 📌 Checklist do PDF final (Moodle)
- [ ] Link do repositório GitHub
- [ ] Nomes completos + RAs de todos
- [ ] Resumo do ambiente, agentes usados e comandos do harness
- [ ] Prints/logs da suíte de testes rodando
'@