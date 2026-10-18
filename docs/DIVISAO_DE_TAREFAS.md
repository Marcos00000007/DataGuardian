# Divisão de Tarefas — Data Guardian
## Entrega 2 (Etapa Intermediária): Publicação, Refinamento e Análise Crítica do Uso de IA

---

## 👤 Marcos André Camargo Belo — Integração Final, Arquitetura & Governança Técnica

**Branch:** `feature/integracao-final-e2`

- [ X ] Revisar e finalizar a integração frontend ↔ backend, garantindo que a aplicação publicada resolve o problema completo (item 1 — "Solução Funcional")
- [  ] Corrigir os erros lógicos que o João documentar na rodada final de testes (ciclo teste → correção)
- [ X ] Atualizar `README.md`: seção de **arquitetura** + **diagrama do fluxo da aplicação** (posso gerar o diagrama, ex: Mermaid, com o pipeline Detector→Validator→Classifier→Redactor→Audit + frontend↔API)
- [ X ] Consolidar as ADRs existentes (0001, 0002) e registrar novas decisões/trade-offs desta etapa, se houver
- [ X ] Abrir os Pull Requests desta etapa com descrição detalhada e **critérios de aceitação explícitos** (isso é item obrigatório novo: "critérios claros de aceitação antes de cada merge")
- [ ] Garantir que as issues da Sprint 2 sejam fechadas conforme concluídas

**Entregável:** aplicação integrada e funcional publicada + README com arquitetura/diagrama + ADRs atualizadas.

---

## 👤 Pedro Henrique Barbosa — Governança da Sprint 2 & Relato de Experiência

**Branch:** `feature/governanca-sprint2`

- [ ] Criar as Issues da Sprint 2 no GitHub (já sabe usar o `gh issue create` — segue o mesmo padrão da Entrega 1)
- [ ] Atualizar o GitHub Project com as colunas/cards da Sprint 2
- [ ] Revisar e aprovar pelo menos **2 Pull Requests** desta etapa, com comentários reais de code review (não só "Approve" vazio)
- [ ] Consolidar em `docs/HISTORICO_SPRINTS.md` o histórico de commits e sprints: entregas iterativas, issues fechadas, como o trabalho foi organizado (item obrigatório novo: "Histórico de Commits e Sprints")
- [ ] Escrever a seção **"Relato de Experiência"** — aprendizados e desafios reais do desenvolvimento em grupo (é pessoal, precisa ser a vivência dele mesmo, não dá pra terceirizar isso)

**Entregável:** Sprint 2 organizada no Project/Issues + histórico documentado + relato de experiência.

---

## 👤 João Paulo Rodrigues de Oliveira — Testes Finais, Re-especificação & Análise Crítica de IA

**Branch:** `feature/testes-finais-e2`

- [x] Rodar a suíte completa localmente: **100% de aprovação (45/45)** em Python 3.13, incluindo cenários normais e de borda
- [x] Reexecutar a suíte no ambiente padronizado Python 3.11/Docker: **45 testes aprovados** em Python 3.11.17
- [x] Documentar os erros lógicos encontrados e a estratégia de correção adotada em `docs/RELATORIO_TESTES_E_ANALISE_IA.md`
- [x] Registrar o **"Loop de Re-especificação"** e os refinamentos motivados pelos testes na seção 10 de `docs/SPECIFICATION.md`
- [x] Elaborar a **Análise Comparativa de Ferramentas de IA** (Claude Code, Codex CLI, Cursor e Antigravity) em `docs/RELATORIO_TESTES_E_ANALISE_IA.md`
- [x] Elaborar a **discussão Ética/Segurança de IA** em `docs/RELATORIO_TESTES_E_ANALISE_IA.md`, cobrindo os 4 pilares:
  - [x] Alucinação de código e geração de código inseguro/destrutivo
  - [x] Vazamento de dados e confidencialidade ao expor contexto a modelos
  - [x] Propriedade intelectual do código gerado por IA
  - [x] Obrigatoriedade da revisão humana no fluxo SDD

**Entregável:** suíte 100% aprovada + relatório de re-especificação + relatório técnico-ético completo (item 4 da rubrica).

> Nota para o João: o último pilar (revisão humana obrigatória) tem material real pra usar — a gente passou por situações concretas nesse projeto (ex: o botão de "bypass rules and merge" que quase foi usado sem review) que servem de exemplo prático de por que essa revisão importa. Vale citar.

---

## Ordem sugerida

1. João roda a suíte completa primeiro e documenta qualquer erro lógico encontrado.
2. Marcos corrige o que o João apontar, finaliza a integração e o README/diagrama.
3. Em paralelo, Pedro organiza a Sprint 2 no Project/Issues e já começa o relato de experiência.
4. João escreve a análise comparativa e ético-técnica em paralelo aos passos 1-2 (não depende deles).
5. Todos os PRs desta etapa passam por revisão cruzada antes do merge — Pedro revisa pelo menos 2.
6. Reunião final: revisar README, ADRs, relatório de testes e montar o PDF consolidado.

## Checklist do PDF final (Sala Online)
- [ ] Link do repositório GitHub atualizado
- [ ] Nomes completos + RAs de todos
- [x] Relatório de execução dos testes com aprovação no ambiente padronizado: 45/45 em Python 3.11.17
- [x] Seção de Análise Comparativa e Ético-Técnica de IA (`docs/RELATORIO_TESTES_E_ANALISE_IA.md`)
- [ ] Links para os Pull Requests relevantes desta etapa