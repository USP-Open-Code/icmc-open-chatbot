
from langchain_core.messages import ToolMessage, SystemMessage
from langchain_core.prompts import PromptTemplate

from .templates import AgentState, GradeDocument
from src.infrastructure.database import ChromaDB
from .prompts import (
    grader_prompt, agent_prompt, no_generation, generate_answer_prompt
)


class CustomToolNode:
    def __init__(self):
        self.db = ChromaDB()
        self.tools = {"retriever": ChromaDB().retrieve}

    def __call__(self, inputs: list):
        if messages := inputs.get("messages", []):
            message = messages[-1]
        else:
            raise ValueError("No messages found in inputs")

        for tool_call in message.tool_calls:
            tool_result = self.tools[tool_call["name"]].invoke(
                tool_call["args"]
            )

        if not isinstance(tool_call["args"], dict):
            raise TypeError("Tool call args must be a dictionary")

        query = tool_call["args"].get("query")
        docs = tool_result

        messages.append(
            ToolMessage(
                content="Documentos encontrados e adicionardos ao contexto",
                tool_call_id=tool_call["id"]
            )
        )

        return {
            "query": query,
            "docs": docs,
            "messages": messages
        }


def grade_documents(state: AgentState):
    queries = state["query"]
    messages = state.get("messages", [])
    docs_recuperados = state["docs"]
    LLM = state["model"]

    retrieval_grader_chain = (
        PromptTemplate.from_template(grader_prompt)
        | LLM.with_structured_output(GradeDocument)
    )

    filtered_docs = list()
    for d in docs_recuperados:
        score = retrieval_grader_chain.invoke(
            {
                "question": queries,
                "document": d.page_content,
                "message": messages}
        )
        if score.get("binary_score", None):
            filtered_docs.append(d)

    return {
        "docs": filtered_docs,
        "query": queries,
        "messages": messages
    }


def agent(state: AgentState):
    LLM = state["model"]
    agent_msg = PromptTemplate.from_template(agent_prompt)
    chain = agent_msg | LLM.bind_tools([ChromaDB().retrieve])

    return {
        "messages": [chain.invoke(input={"question": state["messages"][-1]})]
    }


def should_continue(state: AgentState):
    if state["messages"][-1].tool_calls:
        return "continue"
    return "end"


def generate(state: AgentState):
    LLM = state["model"]
    docs = state.get("docs", None)
    messages = state.get("messages", [])
    query = state.get("query", None)

    if len(docs) >= 1 and isinstance(messages[-1], ToolMessage):
        answer_chain = (
            PromptTemplate(
                input_variables=["question", "context", "message"],
                template=generate_answer_prompt
            )
            | LLM
        )

        result = answer_chain.invoke(
            {
                "query": query,
                "context": docs,
                "message": messages
            }
        )

        docs_context = [{
            "file_name": d.metadata["filePathField"],
            "page_content": d.page_content.replace("\n", "\n\n"),
        } for d in docs]

        return {
            "messages": result,
            "docs": docs_context
        }

    else:
        messages = [SystemMessage(content=no_generation)] + state["messages"]
        return {
            "messages": [LLM.invoke(messages)],
            "docs": []
        }
