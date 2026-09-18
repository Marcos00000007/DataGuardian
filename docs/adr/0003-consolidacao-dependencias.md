# ADR-0003: Consolidação das dependências Python em um único arquivo

**Status:** Aceita
**Data:** 2026-09-18

## Contexto

Durante a preparação da Entrega 2, foi identificado um `requirements.txt` duplicado na raiz do repositório, gerado por um `pip freeze` executado no PowerShell sem especificar o encoding — o arquivo ficou em UTF-16 e ilegível como texto puro em outras ferramentas (GitHub, editores configurados para UTF-8). Já existia `backend/requirements.txt` (dependências de execução) e `backend/requirements-dev.txt` (dependências de teste), ambos em UTF-8 e funcionais.

## Decisão

Remover o `requirements.txt` da raiz e manter as dependências centralizadas em `backend/requirements.txt` (produção) e `backend/requirements-dev.txt` (desenvolvimento/testes), que é onde o `Dockerfile` do backend já lê as dependências.

## Motivos

- Evita duas fontes de verdade divergentes para as mesmas dependências.
- Elimina o arquivo com encoding incorreto, que quebraria `pip install -r requirements.txt` em ambientes que esperam UTF-8.
- Mantém a convenção já usada pelo `Dockerfile` do backend (RNF04 — portabilidade via Docker).

## Consequências

- Qualquer novo pacote Python deve ser adicionado em `backend/requirements.txt` (ou `-dev.txt` se for só de teste), nunca em um arquivo na raiz.
- Scripts ou CI que porventura referenciem `requirements.txt` na raiz precisam ser atualizados para `backend/requirements.txt`.
