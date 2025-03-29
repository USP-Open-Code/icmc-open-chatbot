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

    async def invoke(self, message: str, model: ChatOpenAI | OllamaLLM):
        response = self.graph.invoke(
            {
                "messages": [
                    {"role": "user", "content": message}
                ],
                "model": model,
            }
        )
        return {
            "messages": response["messages"][-1].content,
        }

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
