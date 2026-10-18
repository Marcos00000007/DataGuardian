# ADR-0004: Imagem única do backend e serviço de testes no Compose

**Status:** Aceita
**Data:** 2026-10-18

## Contexto

O comando de testes documentado no README (`docker-compose exec backend pytest -v`) não funcionava a partir de um clone limpo: o `Dockerfile` instalava apenas `requirements.txt` (fastapi, uvicorn, pydantic), enquanto `pytest` e `httpx` ficavam em `requirements-dev.txt`. Além disso, `exec` exige que o backend esteja no ar, o que falha quando a porta 8000 já está ocupada por outro programa (situação ocorrida na máquina de um integrante durante a homologação).

A Entrega 3 exige subir a aplicação e o test harness com comando único.

## Decisão

1. O `Dockerfile` do backend instala `requirements-dev.txt` (que inclui `requirements.txt`), produzindo uma única imagem usada pela API e pelos testes.
2. O `docker-compose.yml` ganha o serviço `tests`, no *profile* `test` (não sobe com `docker-compose up`), sem portas publicadas e com `pytest -v --cov=app --cov-report=term-missing` como comando. Execução: `docker-compose run --rm tests`.
3. As portas do host passam a ser configuráveis por `BACKEND_PORT` e `FRONTEND_PORT` (padrões 8000 e 5173), documentadas em `.env.example`.
4. O `CMD` do `Dockerfile` deixa de usar `--reload`; o modo de desenvolvimento com recarga fica apenas no `command` do serviço `backend` no Compose.
5. `PYTHONDONTWRITEBYTECODE=1` evita gerar `__pycache__` no volume montado, e `COVERAGE_FILE=/tmp/.coverage` mantém o arquivo de cobertura fora do repositório.

## Alternativas consideradas

- **Dois Dockerfiles (produção e teste):** isola melhor as dependências, mas duplica manutenção para um projeto desta escala.
- **Manter `exec` e documentar `pip install` antes:** não atende ao "comando único" e continua dependendo de o backend estar no ar.

## Consequências

- A imagem de execução carrega `pytest`, `httpx` e `pytest-cov` sem necessidade. Para um deploy de produção real, o ideal seria *multi-stage build* com um alvo de teste separado.
- Qualquer pessoa roda a suíte completa com um comando, sem instalar Python localmente.
- O README e a documentação de testes passam a refletir o comando que realmente funciona.