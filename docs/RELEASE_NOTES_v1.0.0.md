# Data Guardian v1.0.0

Primeira versão estável. Motor LGPD de detecção, classificação e mascaramento de dados pessoais, com API HTTP e interface de demonstração.

## O que está incluído

- **API** `POST /v1/scan` e `GET /v1/health` (FastAPI).
- **Detecção** de CPF, CNPJ, e-mail, telefone, CEP, cartão de crédito e RG; nome e endereço com heurísticas limitadas a formatos simples.
- **Validação** de CPF e CNPJ por dígito verificador (descarta falsos positivos).
- **Classificação** de sensibilidade (ALTA, MÉDIA, BAIXA) e resolução de sobreposições.
- **Mascaramento** configurável: `MASK`, `REDACT`, `HASH`.
- **Auditoria** sem o valor original do dado pessoal.
- **Interface** em React + TypeScript + Vite + Tailwind.
- **Empacotamento** com Docker Compose: aplicação e testes com comando único.

## Como usar

```bash
docker-compose up --build        # aplicação (http://localhost:5173)
docker-compose run --rm tests    # testes + cobertura
```

Detalhes no [README](../README.md).

## Qualidade

- Suíte de testes automatizados com 100% de aprovação (ver relatório de execução e cobertura anexado à entrega).
- Especificação técnica final em `docs/SPECIFICATION.md`.
- Quatro ADRs registrando as decisões de arquitetura.

## Mudanças desde a Entrega 2

- Erros de payload padronizados em HTTP 400 (`INVALID_PAYLOAD`).
- Suíte reescrita com asserts reais; cobertura de código medida.
- Imagem Docker do backend inclui dependências de teste; serviço `tests` no Compose; portas configuráveis (ADR-0004).
- `__pycache__` removido do versionamento.
- Versão da API atualizada para `1.0.0`.

## Limitações conhecidas

- Nome e endereço: heurísticas simples, fora do formato esperado podem não ser detectados.
- `HASH` usa SHA-256 truncado em 10 caracteres hexadecimais e sem sal; não impede reversão por força bruta em dados de baixa entropia.
- CORS aberto (`*`) e sem autenticação: adequado à demonstração, não a produção.
- Requisito de desempenho de 500 ms (RNF01) verificado apenas de forma funcional, sem medição formal.

## Equipe

Marcos André Camargo Belo (RA 22510865) · João Paulo Rodrigues de Oliveira (RA 22508370) · Pedro Henrique Barbosa (RA 22503467)