Set-Content -Path docs\DIVISAO_DE_TAREFAS.md -Encoding UTF8 -Value @'
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

## Pedro Henrique — Repositório & Governança

**Branch sugerida:** `feature/repo-governance`

- [ ] Criar o repositório no GitHub (público ou com acesso liberado aos professores).
- [ ] Configurar estrutura de branches: `main` (protegida, sem commit direto), `develop`, `feature/*`.
- [ ] Ativar proteção da branch `main` (Settings -> Branches -> exigir Pull Request antes do merge).
- [ ] Criar o **GitHub Project** (quadro Kanban: To Do / In Progress / Review / Done).
- [ ] Transformar cada checklist deste documento em **Issues** no GitHub e vincular ao Project.
- [ ] Criar um template de Pull Request simples (checklist: "testes passaram?", "revisado por outro membro?").
- [ ] Escrever o `README.md` inicial com visão geral, guia de instalação/execução e seção de ADRs.

**Entregável:** repositório estruturado + README.md + Project/Issues populados.

---

## Marcos André Camargo Belo — Ambiente, Agentes de IA & Esqueleto do Código

**Branch sugerida:** `feature/env-agents-skeleton`

- [ ] Escolher a stack e registrar a decisão como ADR.
- [ ] Criar `Dockerfile` e `docker-compose.yml` para rodar o serviço de forma reprodutível.
- [ ] Configurar o agente de IA usado e commitar o arquivo de regras/contexto no repo (`CLAUDE.md`).
- [ ] Implementar o esqueleto inicial dos componentes da spec: Detector, Validator, Classifier, Redactor, Audit Logger.
- [ ] Expor os endpoints `POST /v1/scan` e `GET /v1/health` conforme o contrato da `SPECIFICATION.md` (seção 7).
- [ ] Documentar os comandos exatos de execução no README.

**Entregável:** ambiente containerizado funcional + arquivo de regras do agente + esqueleto de código rodando os endpoints básicos.

---

## João Paulo Rodrigues de Oliveira — Test Harness & Evidências de Execução

**Branch sugerida:** `feature/test-harness`

- [ ] Escolher o framework de testes compatível com a stack (pytest).
- [ ] Criar a suíte de testes cobrindo os cenários principais (RF01-RF08 da spec).
- [ ] Criar testes para os casos de borda (seção 9 da spec).
- [ ] Criar um único comando de execução que rode toda a suíte de uma vez.
- [ ] Rodar a suíte, capturar o log/print da execução bem-sucedida e salvar.
- [ ] (Bônus) configurar um workflow de GitHub Actions rodando os testes a cada Pull Request.

**Entregável:** suíte de testes + comando único de execução + log/print comprobatório.

---

## Ordem sugerida (para não travar ninguém)

1. Pedro Henrique cria repo, branches e Issues.
2. Em paralelo, Marcos sobe o Dockerfile e o esqueleto; João Paulo já escreve os testes a partir da spec.
3. Assim que o Marcos subir os componentes, o João Paulo pluga os testes reais neles.
4. Cada PR precisa ser revisado por pelo menos um outro membro antes do merge.
5. Reunião rápida antes do prazo: revisar README, prints de execução e montar o PDF final juntos.

## Checklist do PDF final (Moodle)
- [ ] Link do repositório GitHub
- [ ] Nomes completos + RAs de todos
- [ ] Resumo do ambiente, agentes usados e comandos do harness
- [ ] Prints/logs da suíte de testes rodando
'@Set-Content -Path docs\adr\0001-deteccao-deterministica.md -Encoding UTF8 -Value @'
