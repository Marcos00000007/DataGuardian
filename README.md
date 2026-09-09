Set-Content -Path README.md -Encoding UTF8 -Value @'
# Data Guardian

Motor de detecção, classificação e mascaramento de dados pessoais, criado para apoiar empresas na conformidade com a LGPD.

Dado um texto de entrada, o Data Guardian identifica dados pessoais (CPF, CNPJ, e-mail, telefone, etc.), classifica o nível de sensibilidade de cada um e aplica uma política de mascaramento configurável.

## Equipe

| Nome | RA | Frente |
|------|----|--------|
| Marcos André Camargo Belo | _22510865_ | Ambiente, Agentes de IA e Esqueleto do Código |
| João Paulo Rodrigues de Oliveira | _22508370_ | Test Harness e Evidências de Execução |
| Pedro Henrique Barbosa | _(preencher)_ | Repositório e Governança |

## Documentação

- Especificação Técnica completa: `docs/SPECIFICATION.md`
- Divisão de tarefas da sprint: `docs/DIVISAO_DE_TAREFAS.md`
- Decisões arquiteturais (ADRs): `docs/adr/`

## Stack

- Backend: Python 3.11 + FastAPI
- Frontend: React + TypeScript + Vite + Tailwind CSS
- Infraestrutura: Docker + Docker Compose

## Como rodar o projeto

Pré-requisito: Docker e Docker Compose instalados.