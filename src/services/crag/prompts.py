agent_prompt = """
    Gere uma consulta para a vector store com base na pergunta do usuario:
    {question}

    Para ajudar a responder a pergunta, considere as seguintes ferramemntas:
        - Document Retriever: Consulta a vector store para consultar os
        documentos.

    OBS:
        É OBRIGATÓRIO USAR A FERRAMENTA Document Retriever.
    """


grader_prompt = """
    Avalie os arquivos recuperados com base na pergunta do usuario:
    {question}
    {context}
    {message}
"""


no_generation = """
    Informe ao usuario que não foi possivel gerar uma resposta para 
    a sua pergunta.
"""


generate_answer_prompt = """
    Escreva uma resposta para a pergunta do usuario com base nos
    arquivos recuperados:
    {question}
    {context}
    {message}
"""
