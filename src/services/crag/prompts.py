agent_prompt = """
    Gere uma consulta para a vector store com base na pergunta do usuario:
    {question}

    Para ajudar a responder a pergunta, considere as seguintes ferramentas:
        - Most Recent: Caso seja sobre os documentos mais recentes, use
        essa ferramenta para obter os documentos mais recentes.
        - Retriever: Consulta a vector store para buscar contexto
        sobre a questão, exceto se a pergunta for sobre os documentos
        mais recentes.
    """


grader_prompt = """
    Avalie os arquivos recuperados com base na pergunta do usuario,
    sendo que sua resposta deve ser "yes", caso relevante, ou "no":
    {question}
    {document}
    {message}

    OBS:
        - Se houver uma tool call para a ferramenta "Most Recent",
        a resposta deve ser OBRIGATORIAMENTE "yes".
"""


no_generation = """
    Informe ao usuario que não foi possivel gerar uma resposta para
    a sua pergunta.
"""


generate_answer_prompt = """
    Escreva uma resposta para a pergunta do usuario com base nos
    arquivos recuperados:
    {query}
    {context}
    {message}

    OBS:
        - A resposta deve ser gerada na mesma lingua da entrada abaixo:
            {query}
"""
