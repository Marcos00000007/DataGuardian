# Relatório de Testes, Re-especificação e Análise de IA

**Projeto:** Data Guardian
**Data da rodada:** 2026-10-15
**Responsável:** João Paulo Rodrigues de Oliveira
**Base de requisitos:** `docs/SPECIFICATION.md`

## 1. Resultado da suíte

A suíte foi completada com verificações comportamentais para os requisitos RF01–RF08, RN01–RN06 e casos de borda da seção 9. Foram removidos testes vazios que terminavam sem asserções. A cobertura desta rodada inclui validação de CPF/CNPJ, detecção configurável, offsets, classificação, estratégias de mascaramento, entradas inválidas, auditoria sem o valor original, sobreposição CPF/telefone e texto de 10.000 caracteres.

| Execução | Resultado | Observação |
|---|---:|---|
| `python -m pytest backend/tests/test_suite.py -q` | 40 aprovados | Suíte de integração/API após os ajustes |
| `python -m pytest backend/tests -q` | **45 aprovados** | Suíte completa local, Python 3.13.14 |
| Ambiente padronizado (Docker, Python 3.11.17) | **45 aprovados** | Suíte completa executada no container do backend |

Assim, a suíte teve 100% de aprovação (45/45) tanto localmente quanto no ambiente padronizado Python 3.11.17/Docker. O teste de 10.000 caracteres confirma o comportamento funcional, mas não constitui benchmark suficiente para certificar o limite de 500 ms do RNF01.

## 2. Achados e correções desta rodada

| Achado reproduzível | Evidência | Estratégia/correção |
|---|---|---|
| O harness anterior tinha muitos `pass` e um health check sem asserts; os testes passavam sem validar o requisito. | A primeira execução informava aprovação apesar dos casos vazios em `backend/tests/test_suite.py`. | Substituição por asserts de API e unidade; a suíte completa agora totaliza 45 testes reais. |
| RG, nome e endereço não eram detectados, embora constassem nos exemplos contratuais. | Três casos de detecção falharam no teste focado. | Inclusão dos padrões para os formatos explicitamente exemplificados. Nome retorna somente o trecho identificado, com offsets correspondentes. Heurísticas gerais seguem limitadas aos exemplos enquanto faltarem critérios de gramática. |
| A máscara de CPF removia pontuação (`************35`), diferente do exemplo de RF05 (`***.***.***-35`). | Assert de máscara falhou para CPF formatado. | Máscara agora substitui os dígitos preservando pontos, hífens e espaços; aplicado também a CNPJ e cartão. |
| Os erros não seguiam o contrato de RF08: payloads ausentes/nulos e tipo desconhecido retornavam 422; vazio retornava o envelope FastAPI `detail`. | Cinco asserts de resposta de erro falharam. | Normalização para HTTP 400 e `{ "error": { "code": "INVALID_PAYLOAD", "message": "..." } }`. Mensagem genérica evita repetir valores recebidos. |
| O arquivo da especificação terminava com um comando PowerShell literal e o marcador de here-string, não como Markdown. | Cabeçalho e final de `docs/SPECIFICATION.md`; o histórico contém correção parcial anterior, mas o wrapper de abertura continuava presente. | Remoção do wrapper, preservando o conteúdo normativo, e registro da higienização na seção 10. |

## 3. Loop de Re-especificação

O ciclo adotado nesta rodada é:

1. Executar testes rastreáveis a uma regra ou exemplo já escrito na especificação.
2. Reproduzir a falha e classificar sua origem: defeito de código, teste inválido ou requisito ambíguo.
3. Para requisito já explícito, corrigir a implementação e manter o contrato; não alterar a regra apenas para fazer o teste passar.
4. Para regra nova ou ambígua, registrar a decisão e o motivo na seção 10 de `SPECIFICATION.md` antes de implementar comportamento novo.
5. Reexecutar o teste focado, depois a suíte completa; fazer revisão humana das mudanças e dos diffs.

Nesta rodada, as correções de erro HTTP e máscara seguiram exemplos já existentes. O ajuste do detector implementou os formatos de RG, nome e endereço presentes na seção de escopo e no harness. A seção 10 registra os ajustes datados de 2026-10-15 e mantém explícita a ambiguidade das heurísticas de nome/endereço: não há gramática, fronteira de entidade ou critério para falsos positivos definido. O comportamento foi limitado aos exemplos, sem alegar resolver essa ambiguidade.

## 4. Comparação de ferramentas de IA

Comparação qualitativa baseada nos recursos descritos nas documentações oficiais consultadas em 2026-10-15. Não é benchmark independente de precisão; qualidade final depende do modelo selecionado, contexto, permissões, testes e revisão do desenvolvedor.

| Ferramenta | Pontos fortes observáveis | Limitações / cuidados | Impacto potencial na qualidade |
|---|---|---|---|
| **Claude Code** | CLI que lê e edita o repositório, executa comandos; integra-se também a IDE, desktop e web; oferece instruções de projeto, hooks e subagentes. | A superfície de execução e autonomia exige permissões deliberadas; tarefas feitas no terminal ainda podem alterar muitos arquivos ou executar comandos. Recursos e acesso variam por superfície/plano. | Bom para ciclos completos de implementação e validação. Hooks e instruções podem reforçar SDD, mas não substituem revisão do diff nem testes independentes. |
| **Codex CLI** | Fluxo local de terminal para inspecionar, editar e executar; oferece escolha de permissões/sandbox, scripts/CI e revisão de mudanças sem editar a árvore de trabalho. | O nível de acesso depende do modo configurado; revisão automatizada não garante detectar todos os defeitos. Uso de cloud transfere a tarefa para outro ambiente e exige avaliação de dados/contexto. | Permissões explícitas e revisão somente leitura ajudam a reduzir alterações não intencionais; qualidade aumenta quando o resultado é validado pelos testes do projeto. |
| **Cursor** | Agent dentro do editor com busca, leitura/edição, terminal, navegador e checkpoints locais; permite selecionar modelo e compor instruções/ferramentas. | Acesso a contexto e execução de ferramentas precisam ser limitados; checkpoint não substitui Git. A política de privacidade alerta que Inputs podem conter informações enviadas e que segurança absoluta não existe; verificar configurações, plano e termos aplicáveis. | Integração visual facilita inspecionar diffs e testar a interface; checkpoints ajudam a recuperar mudanças, mas não são uma aprovação técnica. |
| **Google Antigravity** | Plataforma orientada a agentes, com editor e superfície Manager para orquestrar execuções; pode planejar, executar e verificar tarefas por editor, terminal e navegador; gera artefatos revisáveis. | A execução assíncrona e multiagente amplia o alcance de erros e o contexto compartilhado; requer supervisão e entendimento das permissões e políticas do serviço. A fonte consultada descreve disponibilidade em public preview na publicação de lançamento. | Artefatos e walkthroughs podem tornar a revisão mais concreta; autonomia aumenta produtividade potencial e também a necessidade de verificar código, testes e ações antes de aceitar. |

Fontes oficiais: [Claude Code — visão geral](https://code.claude.com/docs/en/overview); [Codex CLI](https://learn.chatgpt.com/docs/codex/cli) e [permissões e segurança](https://learn.chatgpt.com/docs/agent-approvals-security); [Cursor Agent](https://cursor.com/docs/agent/overview) e [Política de Privacidade](https://cursor.com/privacy); [Google Antigravity — anúncio e fluxo de trabalho](https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/).

## 5. Discussão ética e segurança

### Alucinação e código inseguro ou destrutivo

Um modelo pode produzir APIs, campos, regras ou dependências que não existem no contrato, além de sugerir comandos destrutivos ou permissões excessivas. O risco concreto neste repositório é introduzir uma heurística não especificada para classificar nome/endereço como se fosse requisito aprovado. Mitigações: SDD como fonte da verdade, ambiente de execução restrito, revisar comandos antes de executá-los, testes positivos e negativos, análise do diff e aprovação humana. Não se deve aceitar um teste “verde” sem verificar que ele contém asserts úteis.

### Vazamento de dados e confidencialidade

Prompts, arquivos selecionados, logs e contexto do repositório podem ser enviados ao provedor do modelo conforme produto, plano e configurações. O sistema trata dados pessoais; portanto, usar dados sintéticos nos prompts e testes, remover tokens/segredos, minimizar contexto e conferir políticas de retenção, treinamento e controles organizacionais antes de conectar um repositório real. Não presumir que “modo privado” significa processamento local ou retenção zero. O texto bruto do usuário não deve ser copiado para relatórios, prompts compartilhados ou logs de auditoria.

### Propriedade intelectual do código gerado

Código gerado não dispensa verificar licenças, atribuições e compatibilidade com dependências ou trechos incorporados. Registrar a origem de componentes relevantes, revisar similaridade quando houver suspeita, usar dependências aprovadas e executar análise de licença/SBOM conforme a política da organização. A titularidade e as obrigações dependem dos termos aplicáveis e da jurisdição; este relatório não faz uma conclusão jurídica sobre autoria ou copyright.

### Revisão humana obrigatória no SDD

O agente pode propor e executar mudanças, mas a equipe é responsável por requisitos, segurança e merge. O fluxo deve ser: especificação aprovada → implementação → testes → revisão de diff e evidências → aprovação humana → merge. A equipe relata que houve uma situação em que o botão “bypass rules and merge” quase foi usado sem revisão. Esse relato é usado como exemplo prático informado pelo grupo, não como evento verificado por logs deste relatório: um bypass pode remover justamente os controles independentes que detectariam uma implementação incorreta. Nenhuma saída de IA ou suíte automatizada deve aprovar a própria alteração sem revisão humana.

## 6. Pendências e limites

- O branch indicado na tarefa (`feature/testes-finais-e2`) não existe no clone atual; esta rodada foi feita em `main`. Não foi criado nem trocado branch para evitar escolher uma base incorreta.
- Definir em refinamento futuro a gramática e os limites das heurísticas de NOME e ENDERECO; hoje os testes cobrem somente os exemplos explícitos.
- Medir formalmente RNF01 (10.000 caracteres em menos de 500 ms) em ambiente local/dev padronizado; o teste funcional não certifica o tempo.
