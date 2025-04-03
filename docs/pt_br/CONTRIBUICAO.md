# Guia de Contribuição

## Introdução

Agradecemos seu interesse em contribuir com o projeto CRAG API! Este documento fornece as diretrizes necessárias para contribuir de forma efetiva.

## Como Contribuir

### 1. Preparação do Ambiente

1. Faça um fork do repositório
2. Clone seu fork
3. Instale o Poetry (Gestão de dependências)
   ```bash
   pip install poetry
   ```
4. Configure o ambiente de desenvolvimento:

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

### 2. Commit e Push

1. Crie uma branch seguindo o padrão:
   ```bash
   git checkout -b tipo-de-alteracao/nome-da-feature
   ```
   Possibilidades:
   - `bugfix`: para correções de bugs
   - `feat`: para novas funcionalidades
   - `docs`: para alterações na documentação
   - `chore`: para tarefas de manutenção
   - `refactor`: para refatoração de código

2. Faça commits atômicos:
   ```bash
   git add .
   git commit -m "[feat] adiciona nova funcionalidade X"
   ```

3. Push para seu fork:
   ```bash
   git push origin tipo-de-alteracao/nome-da-feature
   ```

### 3. Pull Request

1. Abra um Pull Request no GitHub
2. Descreva as mudanças realizadas
3. Referencie issues relacionadas (caso existam)
4. Siga o template de Pull Request


## Padrões de Código

### Estilo

- Siga a [PEP 8](https://peps.python.org/pep-0008/) - Guia de estilo para código Python
- Use type hints para melhorar a legibilidade e manutenção do código
- Mantenha funções pequenas e focadas em uma única responsabilidade

### Commits

Seguimos o padrão [Conventional Commits](https://www.conventionalcommits.org/):

- `feat`: Nova funcionalidade
- `bugfix`: Correção de bug
- `docs`: Alterações na documentação
- `refactor`: Refatoração de código sem alteração de funcionalidade
- `chore`: Tarefas de manutenção, atualizações de dependências, etc.

## Processo de Review

1. Verificação automática:
   - Linting (verificação de estilo de código)
   - Testes unitários e de integração
   - Cobertura de código

2. Review manual:
   - Clareza do código e legibilidade
   - Qualidade da documentação
   - Performance e otimizações
   - Segurança e tratamento de erros


## Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a [Licença MIT](../../LICENSE).
