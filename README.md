# CRAG API

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-FF9900?style=for-the-badge&logo=LangChain&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-007ACC?style=for-the-badge&logo=langgraph&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FFA500?style=for-the-badge&logo=prisma&logoColor=white)
![Llama](https://img.shields.io/badge/Llama-FF6B6B?style=for-the-badge&logo=meta&logoColor=white)

## Sobre o Projeto

CRAG API é uma API RESTful desenvolvida para gerenciamento e processamento de documentos utilizando tecnologias modernas de processamento de linguagem natural e armazenamento vetorial.

## Tecnologias Principais

- **Python**: Linguagem base do projeto
- **FastAPI**: Framework web para construção da API
- **MongoDB**: Banco de dados principal
- **ChromaDB**: Banco de dados vetorial para armazenamento de embeddings
- **LangChain**: Framework para desenvolvimento de aplicações com LLMs
- **LangGraph**: Framework para construção de grafos de processamento de linguagem natural
- **Docker**: Containerização da aplicação

## Requisitos

- Docker e Docker Compose
- Ollama (Opcional)


## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/crag-api.git
cd crag-api
```

2. Configure as variáveis de ambiente:
```bash
vim .env
# Edite o arquivo .env com suas configurações
```

3. Inicie os serviços com Docker Compose:
```bash
docker-compose --env-file .env -f docker/docker-compose.yml up --build
```

## Estrutura do Projeto

```
crag-api/
├── src/
│   ├── api/
│   │   ├── controllers/
│   │   │   ├── chat.py
│   │   │   ├── crag.py
│   │   │   ├── files.py
│   │   │   ├── guardrails.py
│   │   │   └── __init__.py
│   │   ├── models/
│   │   │   ├── api.py
│   │   │   ├── files.py
│   │   │   └── __init__.py
│   │   └── routes/
│   │       ├── chat.py
│   │       ├── crag.py
│   │       ├── files.py
│   │       └── __init__.py
│   ├── infrastructure/
│   │   ├── config/
│   │   │   ├── llm.py
│   │   │   ├── settings.py
│   │   │   └── __init__.py
│   │   └── database/
│   │       ├── chromadb/
│   │       │   ├── connector.py
│   │       │   └── utils.py
│   │       ├── mongodb/
│   │       │   ├── connector.py
│   │       │   ├── create_collection.js
│   │       │   └── utils.py
│   │       └── __init__.py
│   ├── services/
│   │   ├── crag/
│   │   │   ├── graph.py
│   │   │   ├── nodes.py
│   │   │   ├── prompts.py
│   │   │   ├── templates.py
│   │   │   └── __init__.py
│   │   ├── custom_chat/
│   │   │   ├── chat.py
│   │   │   ├── tools.py
│   │   │   └── __init__.py
│   │   ├── document_reader/
│   │   │   ├── reader.py
│   │   │   └── __init__.py
│   │   └── llama_guard/
│   │       ├── llama_guard.py
│   │       └── __init__.py
│   └── main.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── boot.sh
├── run.py
├── pyproject.toml
├── poetry.lock
├── LICENSE
└── README.md
```

## Uso

A API estará disponível em `http://localhost:8000` após a inicialização.

### Endpoints Principais

- `POST /api/v1/documents`: Upload de documentos
- `GET /api/v1/documents`: Listagem de documentos
- `GET /api/v1/documents/{id}`: Busca de documento específico
- `DELETE /api/v1/documents/{id}`: Remoção de documento

## Desenvolvimento

Para desenvolvimento local:

1. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autor

- **Gustavo Mendonça Ortega**

## Contato

Para mais informações ou suporte, entre em contato através do email: gustavo_ortega@usp.br