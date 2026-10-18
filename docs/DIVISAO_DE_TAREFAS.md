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

---

# Divisão de Tarefas — Data Guardian
## Entrega 3 (Etapa Final): Solução Final, Testes Aprovados e Release Versionada

**Onde estamos (18/10/2026):** a `main` já tem a integração frontend ↔ backend, README com arquitetura/diagrama, ADRs 0001–0003, suíte com 45 testes aprovados, relatório de testes e análise de IA. **Ainda não existe:** relatório de cobertura, especificação As-Built, tag/release `v1.0.0`, vídeo, retrospectiva final e as entregas de governança da Entrega 2 (issues e Project da Sprint 2, histórico de sprints, relato de experiência).

---

## 👤 Marcos André Camargo Belo — Empacotamento, Higienização e Release

**Branch:** `feature/empacotamento-final`

**Pendências da Entrega 2 a fechar:**
- [ ] Confirmar se os erros lógicos da rodada de testes do João (15/10) já estão corrigidos no código (a suíte em 45/45 indica que sim) e marcar o item na Entrega 2
- [ ] Fechar as issues da Sprint 2 quando o Pedro as criar

**Entrega 3:**
- [ ] Docker: subir a aplicação e rodar os testes com um comando cada, a partir de um clone limpo (hoje a imagem do backend instala só `requirements.txt`, sem `pytest`, e o comando de teste do README depende de o backend estar no ar)
- [ ] Garantir que porta ocupada não impeça a execução dos testes (a 8000 já travou uma execução)
- [ ] Higienização: remover `__pycache__` versionado, tirar `--reload` do modo padrão, atualizar a versão `0.1.0` do `main.py`, resolver ou documentar o comentário "ajustar para produção" do CORS e conferir que não há credenciais
- [ ] README: manter arquitetura/diagrama e tabela de ADRs; atualizar instalação, variáveis de ambiente, execução e comando de testes/cobertura
- [ ] Registrar em ADR a decisão de empacotamento
- [ ] Abrir o PR com critérios de aceitação e revisão de outro membro
- [ ] Conferir `main` sem PRs abertos nem conflitos
- [ ] Criar a tag e publicar a release `v1.0.0` sobre o commit final aprovado
- [ ] Montar o PDF de encerramento

**Entregável:** ambiente de comando único, repositório higienizado e release `v1.0.0` publicada.

---

## 👤 João Paulo Rodrigues de Oliveira — Cobertura, Especificação As-Built e Evidências Finais

**Branch:** `feature/as-built-e-cobertura` (a branch `feature/testes-finais-e2` da Entrega 2 não chegou a ser criada)

**Já concluído na Entrega 2 e reaproveitado no PDF final:** suíte 45/45, erros lógicos e loop de re-especificação, análise comparativa das 4 ferramentas de IA e discussão ética (4 pilares). Não é preciso refazer; basta referenciar e ajustar o que estiver listado abaixo.

**Entrega 3:**
- [ ] Relatório de cobertura de código (`pytest-cov`): identificar módulos críticos com cobertura baixa (`validator`, `redactor`, `classifier`, `service`) e cobri-los com testes que tenham `assert`
- [ ] Log final da suíte 100% aprovada, gerado na `main` atualizada, com a tabela de cobertura (screenshots/logs para o PDF)
- [ ] Especificação As-Built: atualizar `docs/SPECIFICATION.md` (hoje marcada "Versão 1.0 (inicial) / Em revisão") ou criar documento próprio, refletindo exatamente o código entregue: contratos de entrada e saída, erro 400, máscaras com separadores, entidades RG/NOME/ENDERECO, seções 3, 7 e 9
- [ ] Conferir os offsets do exemplo da seção 7.1 (as posições do e-mail parecem erradas)
- [ ] Fechar as pendências da seção 6 do relatório: medir o RNF01 (500 ms) ou declarar como fora do escopo, e definir ou assumir como limitação as heurísticas de NOME e ENDERECO
- [ ] No relatório, corrigir a frase que diz que a rodada foi feita direto na `main` (o histórico mostra que entrou pelo PR #28) e conferir se o episódio do "bypass rules and merge" está citado no pilar da revisão humana
- [ ] Configurar nome e e-mail no Git (o commit de 15/10 aparece como "Seu Nome")
- [ ] Abrir o PR com critérios de aceitação e revisão de outro membro
- [ ] Montar o PDF de encerramento

**Entregável:** suíte 100% aprovada com cobertura, especificação As-Built e evidências finais para o PDF.

---

## 👤 Pedro Henrique Barbosa — Governança, Retrospectiva e Vídeo

**Branch:** `feature/governanca-final` (a `feature/governanca-sprint2` da Entrega 2 ainda não tem entrega concluída; verificar se o PR #29 já cobre parte dela)

**Pendências da Entrega 2 (nenhuma marcada até agora; entram no "Histórico Integrado de Versionamento" da Entrega 3):**
- [ ] Criar as issues da Sprint 2 (hoje o repositório só tem as issues #6 a #23, da Entrega 1) e atualizar o GitHub Project (issue #7)
- [ ] Escrever `docs/HISTORICO_SPRINTS.md` com o histórico de commits e sprints
- [ ] Escrever o Relato de Experiência, pessoal e na voz dele (serve de base para a retrospectiva)
- [ ] Revisar e aprovar pelo menos 2 PRs com comentários reais de code review

**Entrega 3:**
- [ ] Revisar e aprovar os PRs finais do Marcos e do João: ler o diff, rodar os testes, conferir os critérios de aceitação
- [ ] Decidir o PR #29: aprovar ou fechar com justificativa
- [ ] Deixar o repositório sem PRs abertos, issues finais fechadas e branches obsoletas removidas
- [ ] Retrospectiva final do grupo (`docs/RETROSPECTIVA.md`): eficácia dos agentes de IA no fluxo SDD, ganho de produtividade com números que o grupo consiga justificar, dificuldades superadas e lições de governança; cada integrante contribui com a própria experiência
- [ ] Vídeo de 3 a 5 minutos: organizar quem fala, mostrar o fluxo principal, a resolução do problema e a execução dos testes em tempo real; publicar o link
- [ ] Abrir o PR com critérios de aceitação e revisão de outro membro
- [ ] Montar o PDF de encerramento

**Entregável:** governança concluída, retrospectiva final e vídeo de demonstração publicado.

---

## Ordem sugerida (Entrega 3)

1. Pedro fecha primeiro as pendências de governança da Entrega 2, que não dependem de ninguém (issues, Project, histórico).
2. Marcos (ambiente de comando único) e João (As-Built e testes) trabalham em paralelo. A cobertura final do João usa o ambiente do Marcos já mergeado.
3. Pedro revisa os PRs conforme forem abertos.
4. Com tudo mergeado e a `main` limpa, Marcos cria a tag e a release `v1.0.0`.
5. Pedro grava o vídeo sobre a versão com a tag.
6. Reunião final: conferir README, especificação, relatório de testes e montar os PDFs.

## Checklist do PDF final (Sala Online — Entrega 3)
- [ ] Link direto para a Release `v1.0.0`
- [ ] Nomes completos + RAs de todos
- [ ] Relatório de execução dos testes aprovados e cobertura de código (screenshots/logs)
- [ ] Link do vídeo de demonstração
- [ ] Resumo executivo de encerramento e lições aprendidas
- [x] Análise comparativa e ético-técnica de IA (já concluída em `docs/RELATORIO_TESTES_E_ANALISE_IA.md`)