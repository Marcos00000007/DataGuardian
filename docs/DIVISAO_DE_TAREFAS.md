# Divisão de Tarefas — Data Guardian
## Sprint 1 / Entrega Inicial (Ambiente, Especificação e Test Harness)

**Equipe:**
| Nome | RA |
|------|----|
| Marcos André Camargo Belo | _(preencher)_ |
| João Paulo Rodrigues de Oliveira | _(preencher)_ |
| Pedro Henrique Barbosa | _(preencher)_ |

Cada pessoa é dona de uma frente independente. Isso facilita o Code Review (cada PR fica pequeno e focado) e evidencia a decomposição do problema pedida na rubrica.

---

## 👤 Pedro Henrique — Repositório & Governança

**Branch sugerida:** `feature/repo-governance`

- [ ] Criar o repositório no GitHub (público ou com acesso liberado aos professores).
- [ ] Configurar estrutura de branches: `main` (protegida, sem commit direto), `develop`, `feature/*`.
- [ ] Ativar proteção da branch `main` (Settings → Branches → exigir Pull Request antes do merge).
- [ ] Criar o **GitHub Project** (quadro Kanban: To Do / In Progress / Review / Done).
- [ ] Transformar cada checklist deste documento em **Issues** no GitHub e vincular ao Project.
- [ ] Criar um template de Pull Request simples (checklist: "testes passaram?", "revisado por outro membro?").
- [ ] Escrever o `README.md` inicial com:
  - Visão geral do projeto (usar o resumo da `SPECIFICATION.md`)
  - Guia de instalação/execução (puxar do Marcos assim que o Docker estiver pronto)
  - Seção **ADRs** (Registro de Decisões Arquiteturais) — registrar pelo menos 2:
    - ADR-001: por que a v1 usa regras determinísticas (regex + validação) em vez de ML para detecção.
    - ADR-002: escolha de linguagem/stack (alinhar com o Marcos).

**Entregável:** repositório estruturado + README.md + Project/Issues populados.

---

## 👤 Marcos André Camargo Belo — Ambiente, Agentes de IA & Esqueleto do Código

**Branch sugerida:** `feature/env-agents-skeleton`

- [ ] Escolher a stack (ex: Python/FastAPI, Node/Express) e registrar a decisão como ADR (mandar pro Pedro Henrique incluir no README).
- [ ] Criar `Dockerfile` e `docker-compose.yml` para rodar o serviço de forma reprodutível.
- [ ] Configurar o agente de IA usado (Claude Code, Cursor, etc.) e commitar o arquivo de regras/contexto no repo (`.cursorrules`, `CLAUDE.md` ou equivalente) — deve referenciar a `SPECIFICATION.md` para manter o fluxo SDD.
- [ ] Implementar o **esqueleto inicial** dos componentes da spec (podem ser stubs simples nesta sprint):
  - `Detector` (regex por tipo de entidade)
  - `Validator` (checksum CPF/CNPJ — RN01/RN02)
  - `Classifier` (níveis de sensibilidade — RN03/RN04)
  - `Redactor` (estratégias de mascaramento — RN05)
  - `Audit Logger` (RN06)
- [ ] Expor os endpoints `POST /v1/scan` e `GET /v1/health` conforme o contrato da `SPECIFICATION.md` (seção 7).
- [ ] Documentar, junto com o Pedro Henrique, os comandos exatos de execução (`docker-compose up`, etc.) no README.

**Entregável:** ambiente containerizado funcional + arquivo de regras do agente + esqueleto de código rodando os endpoints básicos.

---

## 👤 João Paulo Rodrigues de Oliveira — Test Harness & Evidências de Execução

**Branch sugerida:** `feature/test-harness`

- [ ] Escolher o framework de testes compatível com a stack do Marcos (ex: `pytest`, `jest`).
- [ ] Criar a suíte de testes cobrindo os **cenários principais** (RF01–RF08 da spec): CPF válido detectado, e-mail detectado, mascaramento aplicado corretamente, etc.
- [ ] Criar testes para os **casos de borda** (seção 9 da spec): CPF com dígitos repetidos, payload vazio, texto sem dados pessoais, entidades sobrepostas, config com tipo inválido.
- [ ] Criar um único comando de execução (`make test`, `npm test` ou `pytest`) que rode toda a suíte de uma vez — isso vai virar o "harness".
- [ ] Rodar a suíte, capturar o **log/print da execução bem-sucedida** e salvar (para anexar no PDF final e no README).
- [ ] (Bônus, se der tempo) configurar um workflow de **GitHub Actions** rodando os testes a cada Pull Request.

**Entregável:** suíte de testes + comando único de execução + log/print comprobatório.

---

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
