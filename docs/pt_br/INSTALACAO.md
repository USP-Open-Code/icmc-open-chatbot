# Guia de Instalação

## Pré-requisitos

- Docker 27.5.1 ou superior
- Docker Compose 2.32.4 ou superior
- Git
- Ollama 0.6.2 ou superior
- Python 3.13 ou superior (para desenvolvimento local)
- Poetry 2.0.1 ou superior (para desenvolvimento local)

## Instalação com Docker (Recomendado)

1. Clone o repositório:
   ```bash
   git clone https://github.com/CuriousGu/CRAG_Python_API.git
   ```

2. Configure as variáveis de ambiente:
   ```bash
   vim .env
   ```

3. Inicie os serviços:
   ```bash
   docker-compose -f docker/docker-compose.yml --env-file .env up --build
   ```

## Instalação para Desenvolvimento Local

1. Clone o repositório:
   ```bash
   git clone https://github.com/CuriousGu/CRAG_Python_API.git
   ```

2. Configure o ambiente virtual e instale as dependências:

   **Windows**
   ```bash
   python -m venv .venv
   .venv/Scripts/activate
   poetry lock
   poetry install
   ```

   **Linux ou MAC**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   poetry lock
   poetry install
   ```


3. Configure as variáveis de ambiente:
   ```bash
   vim .env
   ```

4. Inicie o MongoDB e o ChormaDB:
   ```bash
   docker-compose -f docker/docker-compose.yml --env-file .env up mongodb chroma -d
   ```

5. Execute a aplicação:
   ```bash
   python run.py
   ```


## Verificação da Instalação

Para verificar se a instalação foi bem-sucedida:

1. Acesse a documentação da API pelo navegador:
   ```
   http://localhost:9876/docs
   ```

2. Verifique os logs dos containers:
   ```bash
   docker-compose -f docker/docker-compose.yml logs -f
   ```

### Suporte

Para suporte adicional:
- Abra uma issue no GitHub
- Entre em contato através do email: gustavo_ortega@usp.br
