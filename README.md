# Bot de Notícias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-FF9900?style=for-the-badge&logo=LangChain&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-007ACC?style=for-the-badge&logo=langgraph&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FFA500?style=for-the-badge&logo=prisma&logoColor=white)
![Llama](https://img.shields.io/badge/Llama-FF6B6B?style=for-the-badge&logo=meta&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)

## Sobre o Projeto

É aplicação conversacional baseada em um grafo que utiliza a técnica de Retrieval-Augmented Generation (RAG), com um nó adicional de correção. Antes de gerar uma resposta com base em um documento semanticamente semelhante, o sistema avalia seu contexto, garantindo maior precisão e coerência.

O sistema adota uma arquitetura em camadas (Layered Architecture), utilizando FastAPI como framework principal para a API REST. O armazenamento é dividido entre ChromaDB, responsável pela gestão dos arquivos usados no RAG, e MongoDB, que armazena os logs da aplicação.

O processamento de linguagem natural é realizado por meio do LangChain e LangGraph, que orquestram os agentes e implementam a lógica baseada em grafos. Toda a infraestrutura é containerizada com Docker e Docker Compose, garantindo facilidade de implantação e escalabilidade.

A API e os containers já estão configurados. Para iniciar a aplicação, basta executar:

```bash
# BUILDAR E EXECUTAR O PROJETO
docker-compose -f docker/docker-compose.yml --env-file .env up --build
```
PS: Não se esqueça de alterar os [Prompts](src/services/crag/prompts.py).

## O grafo
<pre><code>```mermaid
graph TD
	__start__([<p>__start__</p>]):::first
	find_references(find_references)
	agent(agent)
	tools(tools)
	crag(crag)
	generate(generate)
	__end__([<p>__end__</p>]):::last
	crag -->generate;
	find_references --> generate;
	generate --> __end__;
	tools --> crag;
	__start__ -. &nbsp;general&nbsp; .-> agent;
	__start__ -. &nbsp;specific&nbsp; .-> find_references;
	agent -.&nbsp;continue&nbsp; .-> tools;
	agent -. &nbsp;end&nbsp; .-> __end__
```</code></pre>



## Autor

**[@CuriousGu](https://www.github.com/CuriousGu) 🇧🇷**

## Docs
1. [Estrutura](docs/pt_br/ESTRUTURA.md)
2. [Instalação](docs/pt_br/INSTALACAO.md)
3. [Configurações](docs/pt_br/CONFIGURACAO.md)
4. [API](docs/pt_br/API.md)
5. [Contribuição](docs/pt_br/CONTRIBUICAO.md)

## Licença

Este projeto está sob a licença MIT, sinta-se a vontade para usar. 

Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contatos
- Email: gustavo_ortega@usp.br
- Linkedin: [Gustavo M. Ortega](https://www.linkedin.com/in/gustavomendoncaortega/)

