from typing import List, Dict
from langchain_ollama import OllamaLLM
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END

from src.infrastructure.config import settings
from .templates import AgentState
from .nodes import (
    agent,
    should_continue,
    generate,
    grade_documents,
    CustomToolNode
)


class CRAG:
    def __init__(self):
        self.index_name = settings.INDEX_NAME
        self.build()

    async def invoke(
        self,
        messages: List[Dict[str, str]],
        model: ChatOpenAI | OllamaLLM
    ):
        try:
            response = self.graph.invoke(
                {
                    "messages": messages[-10:],
                    "model": model,
                }
            )
            return {"messages": response["messages"][-1].content}

        except Exception as e:
            raise ValueError(f"Error invoking CRAG: {e}")

    def build(self):
        try:
            builder = StateGraph(AgentState)
            builder.add_node("agent", lambda state: agent(state))
            builder.add_node("tools", CustomToolNode())
            builder.add_node("crag", grade_documents)
            builder.add_node("generate", generate)

            builder.add_edge(START, "agent")
            builder.add_conditional_edges(
                "agent",
                should_continue,
                {
                    "continue": "tools",
                    "end": END
                }
            )
            builder.add_edge("tools", "crag")
            builder.add_edge("crag", "generate")
            builder.add_edge("generate", END)
            self.graph = builder.compile()

        except Exception as e:
            raise ValueError("Error building graph") from e
