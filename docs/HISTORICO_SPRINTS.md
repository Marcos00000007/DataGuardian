# Histórico de Commits e Sprints

Este histórico resume a organização das entregas a partir dos commits locais e
das Issues e Pull Requests consultadas no GitHub em 2026-10-19. Os hashes
citados são marcos representativos, não uma lista exaustiva de commits.

## Como o trabalho foi organizado

- O desenvolvimento foi dividido em entregas e branches de funcionalidade.
- As Issues iniciais organizaram requisitos de documentação, infraestrutura,
  pipeline, interface e testes. Na consulta de 2026-10-19, as Issues disponíveis
  eram #6 a #23, todas fechadas. Elas cobrem a primeira etapa; não havia Issues
  identificadas como Sprint 2 nessa lista.
- As mudanças foram integradas por Pull Requests. O histórico contém PRs de
  fundação e testes (#1, #2, #24 e #25), da entrega intermediária (#26 e #28)
  e do empacotamento final (#31 e #32).
- O ciclo de testes da etapa final identificou ajustes de implementação e
  refinamentos de requisitos, registrados na seção 10 de
  [SPECIFICATION.md](./SPECIFICATION.md).

## Entrega 1 — fundação funcional e testes

**Período observado:** 2026-09-08 a 2026-09-10.

O trabalho começou pela especificação, decisões de arquitetura e infraestrutura.
Em seguida, os componentes do pipeline foram desenvolvidos separadamente —
Detector, Validator, Classifier, Redactor e Audit — e integrados à API e à
interface web. A suíte de testes e o ambiente de execução também foram
adicionados nessa etapa.

Marcos de commits:

- `4a85bab` — documentação inicial, especificação e ADRs.
- `5b519ef` — Dockerfile e Docker Compose para padronizar o ambiente.
- `b2be9d9`, `28d92a5`, `f54475f`, `7564ff1` e `9ae2498` — implementação dos
  componentes do pipeline.
- `04952cf` e `a5bc658` — endpoints da API e interface de scan.
- `2caebdd` — suíte inicial de 36 testes e GitHub Actions.

As Issues #6–#23 foram fechadas e cobriram desde governança e documentação até
testes de cenários principais e de borda.

## Entrega 2 — integração, publicação e análise crítica

**Período observado nos commits:** 2026-09-14 a 2026-10-15.

A divisão de tarefas da entrega foi registrada em `3de5ab0` e integrada pela
PR #26. A integração frontend-backend e a revisão de arquitetura foram
desenvolvidas na branch `feature/integracao-final-e2`. Os commits `a5da9ff` e
`696bdfb` registram, respectivamente, a correção da documentação e a conclusão
documentada da integração. O trabalho de testes finais e análise de IA aparece
em `ff29e9e`.

O registro de refinamentos baseado em testes está em
[SPECIFICATION.md](./SPECIFICATION.md). A relação de tarefas atribuídas aos
integrantes está em [DIVISAO_DE_TAREFAS.md](./DIVISAO_DE_TAREFAS.md).

## Entrega 3 — testes finais e empacotamento

**Período observado:** 2026-10-15 a 2026-10-18.

O fechamento do projeto reuniu a divisão de tarefas da etapa final, o registro
dos testes e o empacotamento da aplicação. Os commits `c8de845`, `765c87b` e
`dd93829` registram esses marcos. As PRs #31 e #32 aparecem no histórico de
integração dessa etapa.

## Pendências de governança verificáveis

Na consulta de 2026-10-19, a lista disponível de Issues continha somente as
Issues #6–#23, já fechadas; não foi possível confirmar Issues próprias da
Sprint 2 nem a organização de seus cards no GitHub Project. A divisão de
tarefas da entrega intermediária registra como pendentes a criação dessas
Issues, a atualização do Project e a revisão de pelo menos duas PRs. Essas
ações não são inferidas como concluídas apenas por existirem PRs ou commits.

## Relato de Experiência

Minha participação envolveu a organização das sprints, a revisão de Pull
Requests e a análise do trabalho realizado pelo João e pelo Marcos. Um dos
desafios foi a demora nas entregas. Conseguimos resolver as pendências com
bastante comunicação ao longo do trabalho.

Aprendi que, quando todos participam e contribuem, o processo fica mais
acelerado. A experiência também reforçou a importância de manter o diálogo
durante a organização e o acompanhamento das tarefas em grupo.
