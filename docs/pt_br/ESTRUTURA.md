# Estrutura

Este documento descreve a estrutura do projeto, detalhando os principais diretórios e arquivos.


## Diretórios e Principais Arquivos

- **.git/**: Diretório de controle de versão.
- **.env**: Arquivo de configuração de variáveis de ambiente.
- **docker/**: Contém arquivos relacionados à configuração do Docker.
- **.github/**: Arquivos de configuração para GitHub.
- **README.md**: Documento de introdução e instruções gerais do projeto.
- **run.py**: Script principal para execução do projeto.
- **boot.sh**: Script de inicialização.
- **pyproject.toml**: Arquivo com as dependências do projeto.
- **.gitignore**: Lista de arquivos e diretórios ignorados pelo Git.
- **LICENSE**: Arquivo de licença do projeto.
- **src/**: Diretório principal do código-fonte.
  - **main.py**: Arquivo de criação da API.
  - **api/**: Contém a lógica da API.
    - **routes/**: Definições de rotas da API.
    - **controllers/**: Controladores da API.
    - **models/**: Templates de dados da API.
  - **services/**: Funcionalidades da API.
    - **crag/**: Corrective RAG.
    - **document_reader/**: Serviço de leitura de documentos.
    - **llama_guard/**: Serviço de guardrails.
  - **infrastructure/**: Configurações e integrações de infraestrutura.
    - **config/**: Arquivos da API.
    - **database/**: Configurações de banco de dados.



## Árvore do Diretório

    .
    ├── .github
    │   └── pull_request_template.md
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── boot.sh
    ├── docker
    │   ├── Dockerfile
    │   └── docker-compose.yml
    ├── docs
    │   └── pt_br
    │       ├── API.md
    │       ├── CONFIGURACAO.md
    │       ├── CONTRIBUICAO.md
    │       ├── ESTRUTURA.md
    │       └── INSTALACAO.md
    ├── pyproject.toml
    ├── run.py
    └── src
        ├── api
        │   ├── controllers
        │   │   ├── __init__.py
        │   │   ├── crag.py
        │   │   ├── files.py
        │   │   └── guardrails.py
        │   ├── models
        │   │   ├── __init__.py
        │   │   ├── api.py
        │   │   └── files.py
        │   └── routes
        │       ├── __init__.py
        │       ├── crag.py
        │       └── files.py
        ├── infrastructure
        │   ├── config
        │   │   ├── __init__.py
        │   │   ├── llm.py
        │   │   └── settings.py
        │   └── database
        │       ├── __init__.py
        │       ├── chromadb
        │       │   └── connector.py
        │       └── mongodb
        │           ├── connector.py
        │           └── utils.py
        ├── main.py
        └── services
            ├── crag
            │   ├── __init__.py
            │   ├── graph.py
            │   ├── nodes.py
            │   ├── prompts.py
            │   └── templates.py
            ├── document_reader
            │   ├── __init__.py
            │   └── reader.py
            └── llama_guard
                ├── __init__.py
                └── llama_guard.py

