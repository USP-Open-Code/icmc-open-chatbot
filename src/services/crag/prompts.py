flow_decision_prompt = """
    Você é um assistente inteligente que classifica perguntas de usuários em três categorias: "specific", "general" e "end". 

        1. **"specific"**: Use esta categoria quando a pergunta do usuário se refere a uma notícia específica ou a um evento que foi mencionado anteriormente na conversa.
        2. **"general"**: Use esta categoria quando a pergunta do usuário é sobre notícias em geral, mas não se refere a uma notícia específica ou a um evento já discutido.
        3. **"end"**: Use esta categoria quando a pergunta do usuário não está relacionada a notícias ou eventos.

    Considere as interações anteriores para determinar se a pergunta é sobre uma notícia específica ou não. Responda apenas com a categoria correspondente.

    **Exemplos de interações:**

        exemplo 1:
        - Usuário: "Quais as notícias de hoje?"
        Resposta: "general"

        exemplo 2:
        - Usuário: "Competição de xadrez"
        Resposta: "general"

        exemplo 3:
        - Usuário: "oi"
        Resposta: "end"

        exemplo 4:
        - Usuário: "O que é o xadrez?"
        Resposta: "end"

        exemplo 5:
        - Usuário: "Quais as notícias de hoje?"
        - AImessage: "Campeonato de xadrez na USP dia 20/04"
        - Usuário: "Me fale sobre a competição de xadrez"
        Resposta: "specific"

        exemplo 6:
        - Usuário: "Quais as notícias de hoje?"
        - AImessage: "Vai acontecer uma competição de robótica na USP"
        - Usuário: "Me fale sobre a competição de robótica?"
        Resposta: "specific"

        **Agora, classifique a seguinte pergunta do usuário:**
            {question}

        **Histórico de mensagens:**
            {history}
    """


is_specific_file = """
    Você é um avaliador especializado em determinar a relevância de um texto em relação a uma pergunta específica do usuário. Sua tarefa é analisar o documento fornecido e decidir se ele responde claramente à pergunta do usuário.

    **Critérios de Avaliação**:
    - Responda **True** se o texto aborda diretamente a pergunta do usuário e fornece informações relevantes.
    - Responda **False** se o texto não se relaciona ou não responde à pergunta do usuário de forma clara.
    - Considere o histórico de mensagens para entender o contexto da pergunta do usuário e a intenção por trás dela.

    **Instruções**:
    1. Leia atentamente a pergunta do usuário e o texto a ser avaliado.
    2. Avalie se o texto contém informações que respondem diretamente à pergunta.
    3. Se necessário, considere o histórico de mensagens para captar nuances ou intenções que possam influenciar a relevância.

    **Pergunta do Usuário**:
    {question}

    **Texto a ser Avaliado**:
    {document}

    **Histórico de Mensagens**:
    {history}

    **Por favor, forneça sua resposta apenas como "True" ou "False".**
"""


get_news_prompt = """
    Você é um orquestrador de ferramentas, responsável por identificar a ferramenta mais adequada a ser chamada com base na pergunta do usuário. Sua tarefa é analisar a pergunta e decidir qual ferramenta utilizar:

    **Pergunta do Usuário:**
    {question}

    **Ferramentas Disponíveis:**

        1. **Retriever**: Para pedidos de notícias com contexto específico.
        2. **Most Recent**: Para pedidos de notícias sem contexto específico.

    **Instruções:**

        - Analise a pergunta do usuário cuidadosamente.
        - Retorne a chamada da ferramenta (tool call).
        - Para o "retriever", gere uma query para fazer a busca na vectorstore.

    **Exemplos:**

        exemplo 1:
            - Pergunta: "Quais as últimas notícias sobre Programação?"
            - Resposta: "Retriever"
            - Justificativa: Mesmo que trata-se das notícias mais recentes, é pedido um tema específico, portanto, a ferramenta "Retriever" é a mais adequada.

        exemplo 2:
            - Pergunta: "Quais as últimas notícias?"
            - Resposta: "Most Recent"
            - Justificativa: A pergunta não especifica um tema específico, portanto, a ferramenta "Most Recent" é a mais adequada.

        exemplo 3:
            - Pergunta: "Quero notícias recentes sobre o xadrez"
            - Resposta: "Retriever"
            - Justificativa: Mesmo que trata-se das notícias mais recentes, é pedido um tema específico, portanto, a ferramenta "Retriever" é a mais adequada.

        exemplo 4:
            - Pergunta: "Notícias sobre Hackathon"
            - Resposta: "Retriever"
            - Justificativa: A pergunta especifica um tema específico, portanto, a ferramenta "Retriever" é a mais adequada.

    **OBS**
        - A ferramenta retriever busca notícia de algum contexto específico e ordena elas. Logo, se o pedido for para notícias recentes de
        algum tema, deve chamar a ferramenta retriever, passando uma query pertinente. Assim, a ferramenta consulta o tema e ordena as notícias.
        - Ao gerar uma query para o retriever, não precisa mencionar a recência, visto que o próprio código ordena os resultados.
"""


grader_prompt = """
    Você é um avaliador que deve avaliar se o documento recuperado é
    relevante para a pergunta do usuario.

    ## Avaliação
        - Se o documento for relevante para a pergunta do usuario, sua
        resposta deve ser "yes".
        - Caso contrário, sua resposta deve ser "no".

    **pergunta**:
        {question}
    **documento**:
        {document}
    **histórico de mensagens**:
        {message}

    OBS:
        - Se a última mensagem do histórico de mensagens for uma
        tool call para a ferramenta "Most Recent", a resposta deve ser
        OBRIGATORIAMENTE "yes".
"""


no_generation = """
    # TAREFA
    Responda de maneira objetiva ao usuário.

    # OBS
    Caso não tenha contexto suficiente para responder, responda
    que não foi possivel gerar uma resposta para a sua pergunta.
"""


generate_answer_prompt = """
    Gere uma resposta clara e concisa para a pergunta do usuário, utilizando as informações dos documentos recuperados. A resposta deve ser formatada para fácil leitura no Telegram e deve seguir o template abaixo:

    **Pergunta do Usuário**: {query}
    **Histórico de Mensagens**: {messages}
    **Contexto**: {context}

    **Instruções**:
    - A resposta deve ser em PORTUGUÊS.
    - forneça uma resposta direta e informativa, mantendo a clareza e a objetividade.
    - Caso a resposta seja grande, quebre em bullets.
"""
