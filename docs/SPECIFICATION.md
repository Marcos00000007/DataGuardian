Set-Content -Path docs\SPECIFICATION.md -Encoding UTF8 -Value @'
# Especificação Técnica — Data Guardian
## Motor de Detecção, Classificação e Mascaramento de Dados Pessoais (LGPD Compliance Engine)

**Versão:** 1.0 (inicial)
**Status:** Em revisão pela equipe
**Fluxo:** Spec-Driven Development (SDD)

---

## 1. Contexto e Problema

A Lei Geral de Proteção de Dados (LGPD — Lei 13.709/2018) exige que empresas identifiquem, classifiquem e protejam dados pessoais em qualquer fluxo de informação (logs, formulários, e-mails, tickets de suporte, planilhas exportadas, etc.). Na prática, a maioria das empresas **não sabe onde seus dados pessoais estão espalhados**, o que gera risco de vazamento, multa regulatória e dano reputacional.

**Problema central:** dado um texto ou documento de entrada, não há forma automatizada, auditável e configurável de identificar quais trechos contêm dados pessoais, qual o nível de sensibilidade de cada um, e aplicar uma ação de proteção (mascaramento, remoção ou apenas alerta) de forma consistente.

**Público-alvo:** times de Engenharia, Compliance e Dados de empresas que processam dados de clientes (fintechs, e-commerces, healthtechs, SaaS B2B/B2C) e precisam demonstrar conformidade com a LGPD.

---

## 2. Objetivo do Sistema

Fornecer um serviço (API) que recebe um texto ou arquivo, e retorna:
1. As entidades de dados pessoais encontradas (com posição no texto);
2. A classificação de sensibilidade de cada entidade;
3. Uma versão do texto com mascaramento/redação aplicada, conforme política configurada;
4. Um log de auditoria da análise realizada (o que foi encontrado, quando, por qual política).

---

## 3. Escopo

### Dentro do escopo (v1)
- Detecção de: CPF, CNPJ, RG, e-mail, telefone (fixo/celular BR), CEP, cartão de crédito, nome completo (heurística simples), endereço (heurística simples).
- Validação de dígitos verificadores para CPF e CNPJ (reduzir falsos positivos).
- Classificação de sensibilidade em 3 níveis: **Baixa**, **Média**, **Alta** (dado sensível LGPD Art. 5º, II).
- Estratégias de mascaramento configuráveis: `MASK` (ex: `***.***.***-11`), `REDACT` (remoção total), `HASH` (substituição por hash irreversível).
- API síncrona via HTTP (REST), entrada em texto puro ou JSON.
- Log de auditoria estruturado (JSON) por requisição.

### Fora do escopo (v1) — candidatos a v2
- OCR de imagens/PDFs escaneados.
- Detecção via modelo de NLP/ML (v1 usa regras determinísticas + regex).
- Multi-idioma (v1 é BR/pt-BR apenas).
- Persistência de longo prazo dos dados analisados (v1 é *stateless* por requisição, exceto o log de auditoria).

---

## 4. Requisitos Funcionais

| ID | Descrição |
|----|-----------|
| RF01 | O sistema deve receber um texto via requisição HTTP POST e retornar as entidades de dado pessoal detectadas. |
| RF02 | O sistema deve indicar, para cada entidade detectada, o tipo (`CPF`, `CNPJ`, `EMAIL`, `TELEFONE`, `CEP`, `CARTAO_CREDITO`, `RG`, `NOME`, `ENDERECO`), a posição inicial/final no texto e o nível de sensibilidade. |
| RF03 | O sistema deve validar matematicamente CPF e CNPJ (dígitos verificadores) antes de classificá-los como positivos. |
| RF04 | O sistema deve aplicar uma estratégia de mascaramento configurável (`MASK`, `REDACT`, `HASH`) e retornar o texto tratado. |
| RF05 | O sistema deve permitir configurar, por requisição ou por perfil padrão, quais tipos de entidade devem ser detectados. |
| RF06 | O sistema deve gerar um log de auditoria por requisição contendo: timestamp, quantidade de entidades por tipo, política aplicada (sem armazenar o dado pessoal original em texto puro no log). |
| RF07 | O sistema deve expor um endpoint de *health check* para validação de disponibilidade do serviço. |
| RF08 | O sistema deve retornar erros estruturados (código + mensagem) para entradas inválidas (ex: payload vazio, tipo de entidade desconhecido na configuração). |

## 5. Requisitos Não-Funcionais

| ID | Descrição |
|----|-----------|
| RNF01 | **Desempenho:** processar textos de até 10.000 caracteres em menos de 500ms (ambiente local/dev). |
| RNF02 | **Determinismo:** a mesma entrada, com a mesma configuração, deve sempre produzir a mesma saída (importante para testabilidade). |
| RNF03 | **Privacidade by design:** nenhum dado pessoal detectado deve ser persistido em texto puro em logs, banco de dados ou arquivos temporários. |
| RNF04 | **Portabilidade:** o serviço deve rodar de forma idêntica em qualquer máquina via container Docker, sem dependências externas obrigatórias na v1. |
| RNF05 | **Testabilidade:** cada componente de detecção deve ser testável isoladamente (unidade), sem exigir subir o serviço HTTP completo. |
| RNF06 | **Extensibilidade:** adicionar um novo tipo de entidade não deve exigir alteração em mais de um módulo (baixo acoplamento). |

---

## 6. Regras de Negócio

- **RN01 — Validação de CPF:** um CPF só é considerado válido se passar no cálculo dos dois dígitos verificadores (módulo 11). CPFs com todos os dígitos iguais (ex: `111.111.111-11`) são inválidos mesmo que passem no cálculo, e devem ser descartados como falso positivo.
- **RN02 — Validação de CNPJ:** mesma lógica de dígito verificador (módulo 11 com pesos específicos), aplicada ao formato de 14 dígitos.
- **RN03 — Classificação de sensibilidade:**
  - **Alta:** CPF, RG, cartão de crédito (dado financeiro/documento único).
  - **Média:** e-mail, telefone, CNPJ.
  - **Baixa:** CEP, nome (isoladamente, sem outro dado associado).
- **RN04 — Prioridade de sobreposição:** se duas entidades detectadas se sobrepõem na mesma posição do texto, prevalece a de **maior sensibilidade**.
- **RN05 — Mascaramento por tipo:**
  - CPF/CNPJ → mantém os 2 últimos dígitos visíveis (ex: `***.***.***-11`).
  - E-mail → mantém domínio visível, mascara usuário (ex: `***@empresa.com`).
  - Cartão de crédito → mantém os 4 últimos dígitos.
- **RN06 — Log de auditoria não deve conter o dado original**, apenas metadados (tipo, quantidade, posição, política aplicada).

---

## 7. Contratos de Entrada e Saída (API)

### 7.1 `POST /v1/scan`

**Entrada:**
```json
{
  "text": "Meu CPF é 123.456.789-09 e meu email é ana@empresa.com",
  "config": {
    "entities": ["CPF", "EMAIL"],
    "strategy": "MASK"
  }
}
```

**Saída (200 OK):**
```json
{
  "findings": [
    {
      "type": "CPF",
      "value_masked": "***.***.***-09",
      "start": 10,
      "end": 24,
      "sensitivity": "ALTA",
      "valid": true
    },
    {
      "type": "EMAIL",
      "value_masked": "***@empresa.com",
      "start": 42,
      "end": 58,
      "sensitivity": "MEDIA",
      "valid": true
    }
  ],
  "sanitized_text": "Meu CPF é ***.***.***-09 e meu email é ***@empresa.com",
  "audit": {
    "timestamp": "2026-09-08T14:30:00Z",
    "total_findings": 2,
    "strategy_applied": "MASK"
  }
}
```

**Erro (400 Bad Request):**
```json
{
  "error": {
    "code": "INVALID_PAYLOAD",
    "message": "Campo 'text' é obrigatório e não pode ser vazio."
  }
}
```

### 7.2 `GET /v1/health`
**Saída (200 OK):** `{ "status": "ok" }`

---

## 8. Decomposição em Componentes (Unidades Testáveis)

- **Detector**: encontra candidatos a entidades via padrões (regex) por tipo.
- **Validator**: aplica regras matemáticas (RN01, RN02) para confirmar ou descartar candidatos.
- **Classifier**: atribui nível de sensibilidade (RN03) e resolve sobreposições (RN04).
- **Redactor**: aplica a estratégia de mascaramento configurada (RN05).
- **Audit Logger**: gera o registro de auditoria sem dado sensível (RN06).

Cada componente deve ser uma unidade isolada (módulo/classe/função pura sempre que possível), permitindo testes unitários independentes do servidor HTTP — atende ao RNF05.

---

## 9. Casos de Borda a Cobrir no Test Harness

- CPF/CNPJ com formatação diferente (com e sem pontuação).
- CPF com dígitos verificadores matematicamente válidos, mas sequência repetida (`000.000.000-00`).
- Texto com múltiplos dados do mesmo tipo.
- Entidades sobrepostas (ex: um número que parece telefone e também parte de um CPF).
- Texto vazio, texto somente com espaços, payload sem o campo `text`.
- Texto muito longo (checar RNF01 de desempenho).
- Configuração pedindo um tipo de entidade inexistente.
- Texto sem nenhum dado pessoal (resultado deve ser lista vazia, não erro).

---

## 10. Registro de Refinamento da Especificação

> Esta seção deve ser atualizada pela equipe conforme a especificação evoluir com base em testes, revisões e feedback — é um item obrigatório da entrega.

| Data | Alteração | Motivo | Responsável |
|------|-----------|--------|-------------|
| — | Versão inicial (v1.0) publicada | Baseline para início do desenvolvimento | — |
| 2026-09-08 | Nome do sistema definido como **Data Guardian** | Decisão da equipe sobre naming do produto | Equipe |
| 2026-09-09 | Stack definida: backend Python/FastAPI, frontend React+TS+Vite+Tailwind, infra Docker (ver ADR-0002) | Viabilizar implementação e demonstração visual do fluxo de scan | Marcos |
'@